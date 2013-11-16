#! /usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 13000))
s.listen(1)

try:
    while True:
        comm, addr = s.accept()
        while True:
            data = comm.recv(1024)

            if not data:
                comm.close()
                break

            print "[%s] %s" % (addr[0], data)

finally:
    s.close()
