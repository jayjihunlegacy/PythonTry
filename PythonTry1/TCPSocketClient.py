from socket import *
import sys
from time import sleep

HOST = "175.198.72.171"
PORT = 11557;
BUFSIZE = 1024
ADDR = (HOST,PORT);
keepgoing = True


while True:
    sys.stdout.flush();
    tcpCliSock = socket(AF_INET,SOCK_STREAM);
    tcpCliSock.connect(ADDR);
    data = input(">");
    if not data:
        break;

    tcpCliSock.send(bytes(data+"\n","utf-8"));
    print("g1")
    data2 = tcpCliSock.recv(BUFSIZE);
    print("g2")
    while keepgoing:
        data = tcpCliSock.recv(BUFSIZE)
        if data:
            print(data.decode('utf-8'))