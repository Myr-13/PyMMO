from logging.logging import Logger
from logging.console_logging import ConsoleLogger
import threading as th
from server.GLOBAL import PACK_END

from server.net.netserver import NetServer
from server.net.netconnection import NetConnection
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
		self.parser = Parser(self.logger)
		
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
			for connection in list(self.netserver.connections.values()):
				connection: NetConnection = connection
				data = bytearray()

				try:
					data = connection.recive_all(PACK_END, 1)
				except:
					connection.disconnect()
					continue
				
				if not data or len(data) == 0:
					continue
				
				string = str(data, 'utf8')[:-len(PACK_END)]
				self.parser.parse(connection, string)

	def connections_loop_start(self):
		thread = th.Thread(target=self.connections_loop)
		thread.start()

	def connections_loop(self):
		while self.is_running:
			self.netserver.accept()
