from logging.console_logging import ConsoleLogger
import client.netclient as netclient
import protocol
from client.utilsclient import *
from client.controls import Controls

import threading as th
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sys

# Initing modules
pygame.init()

class GameClient:
	def __init__(self, debug = True):
		self.debug = debug
		self.logger = ConsoleLogger()

		self.win = pygame.display.set_mode((1200, 720))
		self.fps = 60
		self.fpsclock = pygame.time.Clock()

		self.controls = Controls()

		self.net_client = netclient.NetClient()

	# ===> Network
	def RecieveNetData(self):
		while True:
			data = None
			# Recv
			try:
				data = self.net_client.Recv()
			except:
				self.logger.warn("Not recv data")

			if data:
				print("[SERVER]: " + data.decode())

	def NetTick(self):
		# Send
		self.controls.OnNetTick(self.net_client)

	def RunNetLoop(self):
		a = th.Thread(target = self.RecieveNetData)
		a.start()

	# ===> Main
	def OnTick(self):
		self.OnRender()
		self.NetTick()

		# Lock fps
		self.fpsclock.tick(self.fps)

	def OnRender(self):
		self.win.fill(COLOR_BLACK)
		# Draw your fucking graphic here

		pygame.draw.rect(self.win, COLOR_WHITE, (0, 0, 20, 20))

		# Draw your fucking graphic NOT here
		pygame.display.update()

	def RunMain(self):
		# Starting net
		self.RunNetLoop()

		while True:
			self.OnTick()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.OnShutdown()

	# ===> Run & Shutdown
	def Run(self):
		# Init keyboard input
		self.logger.log("Running client with graphics")

		# Connection to server and send player info
		if self.debug:
			self.logger.log("Connecting to {addr}:{port}".format(addr = "localhost", port = 3030))
		self.net_client.Connect("localhost", 3030)

		# Main
		if self.debug:
			self.logger.log("Starting main loop")
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
		
		pygame.quit()
		sys.exit() # Выйди нахуй блять
