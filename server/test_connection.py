from socket import socket
from time import sleep

NETPACK_TYPE_PLAYERDISCONNECT = 1

def main():
	sock = socket()
	sock.connect(("localhost", 3030))

	sock.send(str.encode("0`"))
	sock.send(str.encode("1`"))
	
	data = sock.recv(1024).decode()
	print(data)

	sock.close()

main()