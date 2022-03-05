import socket

class NetClient:
	def __init__(self):
		self.sock = socket.socket()

	def Connect(self, addr, port):
		self.sock.connect((addr, port))

	def Recv(self, size = 1024):
		return self.sock.recv(size)

	def Send(self, text):
		self.sock.send(text)
