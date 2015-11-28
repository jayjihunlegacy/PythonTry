import http.server
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        from urllib.parse import urlparse
        import sys
        parts = urlparse(self.path)
        print(self.path)
        print(parts)
        print("Request arrived.")


def startWebService():
    try:
        server = http.server.HTTPServer(('localhost',80),MyHandler)
        print("started http server....")
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutdown web server")
        server.socket.close()

startWebService()