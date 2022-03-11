# baseado no código desenvolvido no livro Violent Python
# https://github.com/tanc7/hacking-books/blob/master/Violent%20Python%20-%20A%20Cookbook%20for%20Hackers%2C%20Forensic%20Analysts%2C%20Penetration%20Testers%20and%20Security%20Engineers.pdf

from ast import parse
import optparse
import socket
from socket import *


def portScan(tgtHost, tgtPortStart, tgtPortEnd):
    # tenta transformar o IP address no hostname utilizado
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve '%s' : Unknown host" %tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\nScan Results for: " + tgtName[0])
    except:
        print("\nScan Results for: " + tgtIP)

    setdefaulttimeout(1)

    for port in range(tgtPortStart, tgtPortEnd):
        try:
            connSkt = socket(AF_INET, SOCK_STREAM)
            connSkt.connect((tgtHost, port))
            # connSkt.send('ViolentPython\r\n')
            results = connSkt.recv(100)
            print('%d/ open'% port)
            print(str(results))
            connSkt.close()
        
        except:
            # print('%d/ closed'% port)
            pass
        
        # print("\n")

def main():
    
    ip_address = input("Please type the IP ADDRESS: ")
    range_port_start = input("Please type the first port: ")
    range_port_end = input("Please type the last port: ")

    portScan(ip_address, int(range_port_start), int(range_port_end))

main()