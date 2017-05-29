import optparse
import socket
from socket import *


def connScan(target):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((target.host, target.port))
        sock.send('ping\r\n')
        results = recv(512)
        print('[+] TCP OPEN: {0}').fomrat(target.host)
        sock.close()
    except socket.error as msg:

def portScan(target):
    try:
        targetIP = gethostbyname(target.host)
    except socket.error as msg:
        print
