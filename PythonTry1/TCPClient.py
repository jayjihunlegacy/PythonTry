from socket import *
import sys

HOST = "127.0.0.1"
PORT = 11557;
BUFSIZE = 1024
ADDR = (HOST,PORT);

tcpCliSock = socket(AF_INET,SOCK_STREAM);
tcpCliSock.connect(ADDR);

while True:
    data = input(">");
    if not data:
        break;
    tcpCliSock.send(bytes(data,"utf-8"));
    data2 = tcpCliSock.recv(BUFSIZE);
    if not data2:
        break;
    print(data2.decode("utf-8"));
    sys.stdout.flush();
tcpCliSock.close();