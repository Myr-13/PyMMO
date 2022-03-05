from logging.console_logging import ConsoleLogger
import client.netclient as netclient
import protocol
from client.utilsclient import *

import threading as th
import sys

class GameClient:
	def __init__(self, debug = True):
		self.debug = debug
		self.logger = ConsoleLogger()

		self.net_client = netclient.NetClient()

	def OnNetTick(self):
		# Recv
		data = self.net_client.Recv()

		if data:
			print("[SERVER]: " + data.decode())

	def RunNetLoop(self):
		while True:
			self.OnNetTick()

	def OnTick(self):
		self.OnRender()

	def OnRender(self):
		pass

	def RunMain(self):
		while True:
			self.OnTick()

	def Run(self):
		# Init keyboard input
		self.logger.log("Running client with graphics")

		# Connection to server and send player info
		if self.debug:
			self.logger.log("Connecting to {addr}:{port}".format(addr = "localhost", port = 3030))
		self.net_client.Connect("localhost", 3030)

		# Main
		if self.debug:
			self.logger.log("Running main loop")
		self.RunMain()

	def OnShutdown(self):
		if self.debug:
			self.logger.log("Shuting down client")

		if self.debug:
			self.logger.log("Send disconnect packet")
		self.net_client.Send(protocol.NetPack_PlayerDisconnect().Pack()) # Send disconnect packet
		if self.debug:
			self.logger.log("Closing connection")
		self.net_client.Close() # Closing socket
		
		sys.exit() # Выйди нахуй блять
