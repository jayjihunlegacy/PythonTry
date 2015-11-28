from socket import *
import sys

HOST = "127.0.0.1";
PORT = 11557
BUFSIZE = 1024
ADDR = (HOST,PORT);
udpCliSock = socket(AF_INET,SOCK_DGRAM);


def call():
    trynum = 1
    while True:
        #go = input(">>")
        data = "Try : "+str(trynum)
        trynum += 1
        udpCliSock.sendto(bytes(data,"utf-8"),ADDR);
        if trynum>10:
            break
    udpCliSock.close();


call()