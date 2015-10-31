import formatter
import html
import http
import os
import io
import sys
import urllib
import urllib.parse as urlparse

class Retriever(object):
    __slots__ = ('url', 'file')
    def __init__ (self, url):
        self.url, self.file = self.get_file(url)

    def get_file(self, url, default='index.html'):
        'Create usable local filename from URL'
        parsed = urlparse.urlparse(url)
        host = parse[1].split('@')[-1].split(':')[0]
        filepath = '%s%s'%(host,parsed[2])
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url, filepath

    def download(self):
        'Download URL to specific name file'
        try:
            retval = urllib.urlretrieve(self.url, self.file)
        except(IOError, http.client.InvalidURL) as e:
            retval = (('*** ERROR : bad URL "%s": %s' %(self.url,e)),)
        return retval

    def parse_links(self):
        'Parse out the links found in downloaded HTML file'
        f = open(self.file, 'r')
        data = f.read()
        f.close()
        # parser = html.parser.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(io.BytesIO.
        parser = html.parser.HTMLParser()
        parser.feed(data)
        parser.close()
        return parser.anchorlist

    
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