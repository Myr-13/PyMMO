from logging.logging import Logger
from logging.console_logging import ConsoleLogger
from socket import socket
import threading as th


class Server():
	# For vscode
	connections: list
	addresses: list

	is_running: bool

	logger: Logger

	def __init__(self, debug = False):
		self.socket = socket()
		self.logger = ConsoleLogger()
		self.debug = debug

		self.addresses = []
		self.connections = []

	def Run(self, port: int):
		if self.socket:
			self.logger.log("Starting server on port {0}".format(port))
		self.is_running = True

		self.socket.bind(("", port))
		self.socket.listen(1)

		self.connections_loop_start()
		self.main_loop_start()

	def main_loop_start(self):
		thread = th.Thread(target=self.main_loop)
		thread.start()

	def main_loop(self):
		while self.is_running:
			for i in range(len(self.connections)):
				try:
					data = self.connections[i].recv(1024)

					if not data:
						continue
					
					string = data.decode()
					print("From {address} resolved: {text}".format(address = self.addresses[i], text = string))
				except:
					try:
						self.connections.pop(i)
						self.addresses.pop(i)
					except:
						pass

					self.logger.log("User disconnected")

	def connections_loop_start(self):
		thread = th.Thread(target=self.connections_loop)
		thread.start()

	def connections_loop(self):
		while self.is_running:
			connection, address = self.socket.accept()

			self.addresses.append(address)
			self.connections.append(connection)

			self.logger.log("New connections from: {}".format(address))
