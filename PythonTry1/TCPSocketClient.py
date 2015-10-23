
#NOT WORKING!!!

from socket import *
import sys

HOST = "127.0.0.1"
PORT = 11557;
BUFSIZE = 1024
ADDR = (HOST,PORT);

while True:
    print("While loop")
    sys.stdout.flush();
    tcpCliSock = socket(AF_INET,SOCK_STREAM);
    tcpCliSock.connect(ADDR);
    data = input(">");
    if not data:
        break;
    tcpCliSock.send(bytes(data+"\n","utf-8"));
    data2 = tcpCliSock.recv(BUFSIZE);
    if not data2:
        break;
    print(data2.decode("utf-8"));
    sys.stdout.flush();
    tcpCliSock.close();
#tcpCliSock.close();