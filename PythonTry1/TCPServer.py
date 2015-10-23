from socket import *;
import sys
from time import ctime

print("Start");

HOST = ""
PORT = 11557;
BUFSIZE = 10;
ADDR = (HOST,PORT);

tcpSerSock = socket(AF_INET,SOCK_STREAM);
tcpSerSock.bind(ADDR);
tcpSerSock.listen(5);

nums = 0;

while True:
    print();
    print("Waiting for connection...", end=" ");
    sys.stdout.flush();
    tcpCliSock, addr = tcpSerSock.accept();
    print("...connected from:",addr);

    while True:
        data = tcpCliSock.recv(BUFSIZE);
        print(data.decode("utf-8"),end="");
        sys.stdout.flush();
        if not data:
            break;
        tcpCliSock.send(bytes("[%s] %s" % (ctime(),data.decode("utf-8")),"utf-8"));
        

    tcpCliSock.close();
    nums+=1

    if nums==10:
        break;

tcpSerSock.close();