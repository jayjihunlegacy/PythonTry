from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime
import sys
HOST = '175.198.72.171'
PORT = 11557
ADDR = (HOST,PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print("...connected from:",self.client_address);
        self.wfile.write(self.rfile.readline().strip());

tcpServ = TCP(ADDR, MyRequestHandler)

print("waiting for connection...",end=' ');
sys.stdout.flush();
tcpServ.serve_forever();