from socket import socket

NETPACK_TYPE_PLAYERDISCONNECT = 1

sock = socket()
sock.connect(("localhost", 3030))

sock.send(str.encode(str(NETPACK_TYPE_PLAYERDISCONNECT) + "|Hello∉"))

sock.close()
input()