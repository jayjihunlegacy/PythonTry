from socket import *
from time import ctime
import sys

HOST = ""
PORT = 11558
BUFSIZE = 1024
ADDR = (HOST,PORT)
udpSerSock = socket(AF_INET,SOCK_DGRAM);
#print("My Address :",ADDR);
udpSerSock.bind(ADDR);

while True:
    print("Waiting for message...",end="");
    sys.stdout.flush();
    data,addr = udpSerSock.recvfrom(BUFSIZE);
    byte_to_send = bytes("{}{}".format(ctime(),data.decode("utf-8")),"utf-8");
    udpSerSock.sendto(byte_to_send,addr);
    print("...received from and returned to:",addr);
    sys.stdout.flush();

udpSerSock.close();