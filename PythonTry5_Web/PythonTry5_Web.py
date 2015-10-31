import urllib.parse
import urllib.request as url

urlstr = "http://www.naver.com";

'''
# 1. url parse.
urltup = urllib.parse.urlparse(urlstr);
print(urltup);
'''

'''
# 2. HTML read
naverContact = urllib.request.urlopen(urlstr);

naverHTML = naverContact.readlines();

for line in naverHTML:
    if line.decode('utf-8').startswith("<p>"):
        print(line.decode('utf-8'));
    

naverContact.close();
'''

# 3. download HTML file
def hooker(a,b,c):
    print("HI!");
print(url.urlretrieve(urlstr, "C://a.txt", hooker));

