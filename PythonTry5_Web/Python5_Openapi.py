import http.client

def getBookDataFromISBM(isbn):
    global server, regKey, conn
    if conn is None:
        connectOpenAPIServer()
    uri = userURIBuilder


server = "http://openapi.naver.com"
regKey = "5663b48ac8e00284d2bc2904ea9d0681"
conn = http.client.HTTPConnection("openapi.naver.com")

part1 = "/search?key="
part2 = "&query=love&display=10&start=1&target=book"
q = part1+regKey+part2

conn.request("GET", q)
response = conn.getresponse()
print(response.status,response.reason)
byte = response.read()
print(response.getheader("Content-Length"))
print(byte.decode("utf-8"))

