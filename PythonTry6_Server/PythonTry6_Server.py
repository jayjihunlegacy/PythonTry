import http.server
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys
        parts = urlparse(self.path)
        print(self.path)
        print(parts)
        keyword, value = parts.query.split('=',1)

        if keyword == "title":
            print("Title request.")
        else:
            print("requested :",keyword)


def startWebService():
    try:
        server = http.server.HTTPServer(('localhost',8080),MyHandler)
        print("started http server....")
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()

startWebService()