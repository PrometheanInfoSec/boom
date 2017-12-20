#!/usr/bin/env python
import hashlib
import time
import socket
import threading
from subprocess import check_output

#Must be the same as the client
secret = "AAAA"

#buff sets how long (seconds) we go without an 
#authenticated message before execution
#There might be some slight lag between server and client
#And/or slight service interruption
#So keep this above 5 at least.
#You can make sure nobody can retrip the trigger with
#The safety word on the client side
buff = 10

#How often we check the last queue.  Basically adds to the buffer a tiny bit
checktime = 2

#List of commands to execute when the switch goes dark.
coms = ["echo 1","echo 2"]

HOST = ""
PORT = 1667

last = int(time.time())

first = True
executed = False

def initiate():
	print "Code recieved"
	print "Arming"
	t = threading.Thread(target=executioner)
        t.daemon=True
        t.start()

def execute():
	global executed
	if not executed:
		print "Executing"
		for com in coms:
			print check_output(com, shell=True)
		executed = True

def executioner():
	while True:
		if int(time.time()) > last + buff:
			execute()
		time.sleep(checktime)

def curhash():
	h = hashlib.md5(secret + str(int(time.time())/60)).hexdigest()
	return h

def check(data):
	global last
	global first
	data = data.split("\n")[0].split()[1].strip("/")
	if curhash() == data:
		if first:
			initiate()
			first = False
		last = int(time.time())


if __name__ == "__main__":


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST,PORT))
	s.listen(10)
	while True:
		con, addr = s.accept()
		data = con.recv(100)
		con.close()
		check(data)
