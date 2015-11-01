import formatter
from html.parser import HTMLParser as hP
import http
import os
import io
import sys
import urllib.request
import urllib.parse as urlparse
import codecs

class MyHTMLParser(hP):
    def handler_starttag(self,tag,attrs):
        print("Start tag :",tag)
    def handle_endtag(sef,tag):
        print("End tag :",tag)
    def handle_data(self,data):
        print("Data :",data)

def debug(str):
    print("[DEBUG]",str)

class Retriever(object):
    __slots__ = ('url', 'file')
    def __init__ (self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        'Create usable local filename from URL'
        parsed = urlparse.urlparse(url)
        host = parsed[1].split('@')[-1].split(':')[0]
        debug("Host : "+host)
        filepath = '%s%s'%(host,parsed[2])

        if not os.path.splitext(parsed[2])[1]:
            filepath = os.path.join(filepath,default)

        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)

        baseDir = "C:/crawltest/"
        filepath = baseDir +filepath
        print("[DEBUG] file path :",filepath)
        
        return url, filepath

    def download(self):
        'Download URL to specific name file'
        print(self.url,self.file)
        try:
            retval = urllib.request.urlretrieve(self.url, self.file)
        except(IOError, http.client.InvalidURL) as e:
            retval = (('*** ERROR : bad URL "%s": %s' %(self.url,e)),)
        print(retval)
        return retval

    def parse_links(self):
        'Parse out the links found in downloaded HTML file'
        f = codecs.open(self.file, 'r',"utf-8")
        data = f.readlines()
        f.close()
        
        parser = hP()
        for line in data:
            parser.feed(line)
               
        parser.close()
        return parser.

    
class Crawler(object):
    count = 0
    
    def __init__(self,url):
        self.q = [url]
        self.seen = set()
        parsed = urlparse.urlparse(url)
        host = parsed[1].split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])

    def get_page(self,url,media=False):
        'Donwload page & parse links, add to queue if nec'
        r=Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print(fname, ": skipping parse")
            return
        Crawler.count += 1
        print("\n(",Crawler.count,")")
        print("Url:",url)
        print("File:",fname)
        self.seen.add(url)
        
        ftype = os.path.splitext(fname)[1]
        print("FType : ",ftype)
        if ftype not in ('.htm','.html'):
            return

        for link in r.parse_links():
            if link.startswith('mailto:'):
                print("...discarded, mailto link")
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3', '.mp4', '.m4v', '.wav'):
                    print("...discarded, media file")
                    continue
            if not link.startswith("http://"):
                link = urlparse.urljoin(url,link)
            print("*",link,end=" ")

            if link not in self.seen:
                if self.dom not in link:
                    print("... discarded, not in domain")
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print("... new, added to Q")
                    else:
                        print("...discarded, already in Q")
            else:
                print("...discarded, already processed.")

    def go(self,media = False):
        "Process next page in queue (if any)"
        while self.q:
            url = self.q.pop()
            self.get_page(url,media)

def main():
    '''
    if len(sys.argv) >1 :
        url = sys.argv[1]
    else:
        try:
            url = input("Enter starting URL: ")
        except(KeyboardInterrupt, EOFError):
            url = ""
            '''
    url = "www.naver.com"
    print("URL :",url)
    if not url:
        return
    if not url.startswith("http://") and not url.startswith("ftp://"):
        url = "http://%s/"%url
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()