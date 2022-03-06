import socket

class NetClient:
	def __init__(self):
		self.sock = socket.socket()
		self.sock.setblocking(True)

	def Connect(self, addr, port):
		self.sock.connect((addr, port))
		self.sock.setblocking(0)

	def Recv(self, size = 1024):
		return self.sock.recv(size)

	def Send(self, text):
		self.sock.send(text)

	def Close(self):
		self.sock.close()
