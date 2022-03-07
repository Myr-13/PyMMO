from logging.logging import Logger
from logging.console_logging import ConsoleLogger
import threading as th

from server.net.netserver import NetServer
from server.parser import Parser

BUFFER_SIZE = 1024

class Server():
	is_running: bool
	debug: bool

	logger: Logger
	netserver: NetServer

	parser: Parser

	def __init__(self, debug = False):
		self.debug = debug

		self.logger = ConsoleLogger()
		self.netserver = NetServer(self.logger)
		self.parser = Parser(self, self.logger)
		
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
					data = bytearray()

					while True:
						chunk = self.netserver.recive(i, BUFFER_SIZE)
						if not chunk:
							break
						data += chunk
						print(data[-3:-1: 1].decode())

						if data[-4:-1: 1].decode() == "\xe2\x88\x89":
							print("ended")
							break

					if not data or len(data) == 0:
						continue
					
					print(data)

					string = str(data, 'utf8')
					
					self.parser.parse(string)
					# print("From {address} resolved: {text}\nWith size: {size}".format(address = self.netserver.addresses[i], text = string, size = len(data)))
				except:
					try:
						self.netserver.disconnect(i)
					except:
						pass

					self.logger.log("User disconnected")

	def connections_loop_start(self):
		thread = th.Thread(target=self.connections_loop)
		thread.start()

	def connections_loop(self):
		while self.is_running:
			self.netserver.accept()

	def disconnect(self, id):
		self.netserver.disconnect(id)
