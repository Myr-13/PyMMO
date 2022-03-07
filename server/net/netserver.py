from socket import socket

from logging.logging import Logger

class NetServer:
	socket: socket
	connections: list
	addresses: list

	logger: Logger

	def __init__(self, logger: Logger):
		self.logger = logger

		self.socket = socket()

		self.addresses = []
		self.connections = []

	def start(self, address: str = "", port: int = 3030):
		self.socket.bind((address, port))
		self.socket.listen(1)

		self.logger.log("Server started at {address}:{port}".format(address = "localhost" if address == "" else address, port = port))

	def close(self):
		self.socket.close()

	def disconnect(self, id):
		self.connections.pop(id)
		self.addresses.pop(id)

	def accept(self):
		connection, address = self.socket.accept()

		self.addresses.append(address)
		self.connections.append(connection)

		self.logger.log("New connections from: {}".format(address))

	def recive(self, connection_id: int, size: int = 1024):
		return self.connections[connection_id].recv(size)

	def send(self, data):
		self.socket.send(data)
