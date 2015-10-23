
#NOT WORKING!!!!

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
HOST = ''
PORT = 11557
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handler(self):
        print("...connected from:",self.client_address);
        self.wfile.write(ctime(),self.rfile.readline().strip());

tcpServ = TCP(ADDR, MyRequestHandler)
print("waiting for connection...");
tcpServ.serve_forever();