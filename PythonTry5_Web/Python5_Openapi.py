import http.client

server = "http://openapi.naver.com"
regKey = "5663b48ac8e00284d2bc2904ea9d0681"
conn = http.client.HTTPConnection("openapi.naver.com")


def getBookDataFromISBM(isbn):
    global server, regKey, conn
    if conn is None:
        connectOpenAPIServer()
    uri = userURIBuilder
