from bs4 import BeautifulSoup
import urllib.robotparser as robotparser
import urllib.request as urllib2
import time, traceback, re, sys, os
import sqlite3

crawler_name = 'jayCralwer'
mainpage = 'http://blog.daum.net/'
mainpath = 'C:/crawltest/'
rp = robotparser.RobotFileParser(mainpage +'robots.txt')
rp.read()

def isASCII(s):
    return all(ord(c) < 128 for c in s)

def canFetch(url):
    return rp.can_fetch(crawler_name, url)

def getContent(url, delay=1):
    'download the web document'

    time.sleep(delay)
    if not canFetch(url):
        print('[NOT FETCH]', url)
        return None

    try:
        print('URL : %s'%url)
        if not isASCII(url):
            print('URL not ascii : %s'%url)
            return None
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent',crawler_name)]
        contents = opener.open(url).read().decode('utf-8')
    except:
        traceback.print_exc()
        return None
    return contents

def getArticleInfo(soup):
    'get article info from daum blog'
    rBlog = re.compile('.+blog.daum.net/\w+/\d+.*?')
    URLs = soup('a', {'href':rBlog})
    return [u.get('href').split('?')[0] for u in URLs]

def getOwnArticles(contents):
    'get list of posts included in the blog'
    ret = []
    soup = BeautifulSoup(contents, 'html.parser')
    rBlog = re.compile('.+/BlogView.+')
    for u in soup('a', {'href':rBlog}):
        href = u.get('href')
        article = href.split('articleno=')[1].split('&')[0]
        if ret.count(article)<1:
            ret.append(article)
    return ret

def gatherNeighborInfo(soup):
    'get neighbor bloggers info'
    rBlog = re.compile('http://blog.daum.net/\w+')
    Neighbors = soup('a',{'href':rBlog})
    cnt = 0
    for n in Neighbors:
        url = n.get('href')
        blogname = url.split('/')[-1]
        if url and url.startswith('http://') and db.isCrawledURL(url) < 1:
            db.insertURL(url,1)
            url2 = getRedirectedURL(url)
            if not url2: continue
            re_url = 'http://blog.daum.net' + url2
            body = getContent(re_url, 0)
            if body:
                for u in getOwnArticles(body):
                    fullpath = 'http://blog.daum.net/'+blogname+'/'+u
                    cnt += db.insertURL(fullpath)
    if cnt > 0 :print('%d neighbor articles inserted'%cnt)

def getRedirectedURL(url):
    'get url of frame corresponding post'
    contents = getContent(url)
    if not contents: return None

    try:
        soup = BeautifulSoup(contents, 'html.parser')
        frame = soup('frame')
        src = frame[0].get('src')
    except:
        src = None
    return src

def getBody(soup,parent):
    'get the body!'

    rSrc = re.compile('.+/ArticleContentsView.+')
    iframe = soup('iframe', {'src':rSrc})
    if len(iframe) > 0:
        src = iframe[0].get('src')
        iframe_src = 'http://blog.daum.net'+src
        req = urllib2.Request(iframe_src)
        req.add_header('Referer', parent)
        body = urllib2.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(body, 'html.parser')
        return str(soup.body)
    else:
        print('Null contents')

        return ''
def parseArticle(url):
    'parse the blog and store it.'
    article_id = url.split('/')[-1]
    blog_id = url.split('/')[-2]
    newURL = getRedirectedURL(url)

    if newURL:
        try:
            os.mkdir(mainpath+blog_id)
        except:
            pass
        newURL = 'http://blog.daum.net'+newURL
        contents = getContent(newURL,0)
        if not contents:
            print('Null Contents...')
            db.updateURL(url,-1)
            return

        soup = BeautifulSoup(contents, 'html.parser')

        gatherNeighborInfo(soup)

        n=0
        for u in getArticleInfo(soup):
            n += db.insertURL(u)
        if n>0: print('inserted %d urls from %s'%(n,url))

        sp = contents.find('<title>')
        if sp>-1:
            ep = contents[sp+7:].find('</title>')
            title = contents[sp+7:sp+ep+7]
        else:
            title = ''

        contents = getBody(soup,newURL)

        pStyle = re.compile('<style(.*?)>(.*?)</style>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents = pStyle.sub('', contents)
        pStyle = re.compile('<script(.*?)>(.*?)</script>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents = pStyle.sub('',contents)
        pStyle = re.compile('<(.*?)>', re.IGNORECASE | re.MULTILINE | re.DOTALL)
        contents = pStyle.sub('', contents)

        try:
            fTXT = open(mainpath + blog_id + '/' + article_id + '.txt', 'w')
            fTXT.write(title+'\n')
            fTXT.write(contents)
            fTXT.close()
            
        except:
            traceback.print_exc()
        db.updateURL(url)

    else:
        print('Invalid blog article')
        db.updateURL(url, -1)

class DB:
    'SQLITE3 wrapper class'
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS urls(url text, state int);')
        self.cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS IDX001 ON urls(url);')
        self.cursor.execute('CREATE INDEX IF NOT EXISTS IDX002 ON urls(state);')

    def __del__(self):
        self.conn.commit()
        self.cursor.close()

    def insertURL(self,url,state = 0):
        try:
            self.cursor.execute("INSERT INTO urls VALUES('%s',%d);"%(url,state))
        except sqlite3.DatabaseError as e:
            print(e.with_traceback)
            return 0
        else:
            return 1

    def selectUncrawledURL(self):
        self.cursor.execute('SELECT * FROM urls where state = 0;')
        return [row[0] for row in self.cursor.fetchall()]

    def updateURL(self, url, state = 1):
        self.cursor.execute("UPDATE urls SET state = %d WHERE url = '%s';"%(state,url))

    def isCrawledURL(self, url):
        self.cursor.execute("SELECT COUNT(*) FROM urls WHERE url = '%s' and state = 1;"%url)
        ret = self.cursor.fetchone()
        return ret[0]

db = DB()

if __name__ == '__main__':
    print('starting crawl.py...')

    contents = getContent(mainpage)
    URLs = getArticleInfo(BeautifulSoup(contents, 'html.parser'))
    nSuccess = 0
    for u in URLs:
        nSuccess += db.insertURL(u)
    print('inserted %d new pages.'%nSuccess)

    while True:
        for u in db.selectUncrawledURL():
            print('downloading %s'%u)
            try:
                parseArticle(u)
            except:
                traceback.print_exc()
                db.updateURL(u,-1)
