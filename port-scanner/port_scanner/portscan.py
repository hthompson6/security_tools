import optparse
import socket
from socket import *

def connScan(target):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort)
        connSkt.send('ViolentPython\r\n')
        results
