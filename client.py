from logging.console_logging import ConsoleLogger
import netclient
import protocol
from utilsclient import *

import threading as th
import sys
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide" # Disable this fucking pygame support message
import pygame

# Initing modules
pygame.init()

class GameClient:
	def __init__(self, debug = True, winmode = True):
		self.debug = debug
		self.logger = ConsoleLogger()

		self.net_client = netclient.NetClient()

		self.winmode = winmode
		if winmode:
			self.win = pygame.display.set_mode((1200, 720))
		self.fpslock = 60
		self.fpsclock = pygame.time.Clock()

	def OnKeyEvent(self, event):
		if event.event_type == "down":
			if event.name == "enter":
				self.net_client.Send(str.encode(self.text))
			else:
				self.text += event.name

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
		self.win.fill(COLOR_BLACK)
		# Drawing here xd

		pygame.draw.rect(self.win, COLOR_WHITE, (0, 0, 20, 20))

		# Drawing not here xd
		pygame.display.update()

	def RunMain(self):
		while True:
			self.OnTick()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.OnShutdown()

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
		
		pygame.quit() # Closing pygame
		sys.exit() # Выйди нахуй блять
