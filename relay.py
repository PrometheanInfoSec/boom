#!/usr/bin/env python

import socket

HOST = ""
PORT = 1667

#List of urls to forward to
targets = [
		("www.google.com",80)
		]

def forward(data):
	print data
	for target in targets:
		print "\t", target
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(target)
		s.sendall(data)
		s.close()


if __name__ == "__main__":


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST,PORT))
        s.listen(10)
        while True:
                con, addr = s.accept()
                data = con.recv(100)
                con.close()
                forward(data)

