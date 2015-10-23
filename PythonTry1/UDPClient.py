from socket import *
import sys

HOST = "127.0.0.1";
PORT = 11558
BUFSIZE = 1024
ADDR = (HOST,PORT);
udpCliSock = socket(AF_INET,SOCK_DGRAM);

while True:
    data = input(">");
    if not data:
        break;
    udpCliSock.sendto(bytes(data,"utf-8"),ADDR);
    data, ADDR = udpCliSock.recvfrom(BUFSIZE);
    if not data:
        break;
    print(data.decode("utf-8"));
    sys.stdout.flush();

udpCliSock.close();