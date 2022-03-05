from logging.logging import Logger
from logging.console_logging import ConsoleLogger

from socket import socket
import threading as th

from server.netserver import NetServer

BUFFER_SIZE = 1024

class Server():
	# For vscode
	is_running: bool
	debug: bool

	logger: Logger
	netserver: NetServer

	def __init__(self, debug = False):
		self.logger = ConsoleLogger()
		self.netserver = NetServer(self.logger)
		self.debug = debug

	def run(self, port: int):
		self.is_running = True

		self.netserver.start(port=port)
		self.connections_loop_start()
		self.main_loop_start()

	def main_loop_start(self):
		thread = th.Thread(target=self.main_loop)
		thread.start()

	def main_loop(self):
		while self.is_running:
			for i in range(len(self.netserver.connections)):
				try:
					'''data = bytearray()

					while True:
						chunk = self.netserver.recive(i, BUFFER_SIZE)
						if not chunk:
							break
						data += chunk'''
					
					data = self.netserver.recive(i, BUFFER_SIZE)
					
					if not data or len(data) == 0:
						continue

					string = str(data, 'utf8')
					print("From {address} resolved: {text}\nWith size: {size}".format(address = self.netserver.addresses[i], text = string, size = len(data)))

					sp = string.split("|")
					if sp[0] == "1":
						self.netserver.kick(i)

						self.logger.log("User disconnected")
				except:
					try:
						self.netserver.kick(i)
					except:
						pass

					self.logger.log("User disconnected")

	def connections_loop_start(self):
		thread = th.Thread(target=self.connections_loop)
		thread.start()

	def connections_loop(self):
		while self.is_running:
			self.netserver.accept()
