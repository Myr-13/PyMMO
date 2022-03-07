from logging.console_logging import ConsoleLogger
import client.netclient as netclient
import protocol
from client.utilsclient import *
from client.controls import Controls
from client.ui import UI
from client.menus import Menus

import threading as th
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import sys

# Initing modules
pygame.init()

# Client states
CLIENT_STATE_INMENUS = 0
CLIENT_STATE_INGAME = 1

class GameClient:
	def __init__(self, debug = True):
		self.debug = debug
		self.state = CLIENT_STATE_INMENUS

		# Display
		self.win = pygame.display.set_mode((1200, 720))
		self.fps = 60
		self.fpsclock = pygame.time.Clock()

		# Components
		self.controls = Controls()
		self.ui = UI(self.win)
		self.menus = Menus(self.win, self.ui)
		self.logger = ConsoleLogger()

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
		#self.controls.OnNetTick(self.net_client)
		pass

	def RunNetLoop(self):
		a = th.Thread(target = self.RecieveNetData)
		a.start()

	def Connect(self, ip, port):
		# Connection to server and send player info
		if self.debug:
			self.logger.log("Connecting to {addr}:{port}".format(addr = ip, port = port))
		self.net_client.Connect(ip, port)

	# ===> Main
	def OnTick(self):
		self.OnRender()
		self.NetTick()

		# Tick components
		self.menus.OnTick()

		# Lock fps
		self.fpsclock.tick(self.fps)

	def OnRender(self):
		self.win.fill(COLOR_BLACK)
		# Draw your fucking graphic here

		# Render components
		self.menus.OnRender()

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
		# > Init keyboard input
		if self.debug:
			self.logger.log("Running client with graphics")

		# > Initing components
		if self.debug:
			self.logger.log("Running components")

		# Button functions
		def OnPlayButton():
			self.Connect("localhost", 3030)
			self.state = CLIENT_STATE_INGAME
			self.ui.ClearButtons()

		self.menus.OnInit(OnPlayButton, self.OnShutdown)

		# > Main
		if self.debug:
			self.logger.log("Starting main loop")
		self.RunMain()

	def OnShutdown(self):
		if self.debug:
			self.logger.log("Shuting down client")

		if self.state == CLIENT_STATE_INGAME:
			if self.debug:
				self.logger.log("Send disconnect packet")
			self.net_client.Send(protocol.NetPack_PlayerDisconnect().Pack()) # Send disconnect packet
			if self.debug:
				self.logger.log("Closing connection")
			self.net_client.Close() # Closing socket
		
		pygame.quit()
		sys.exit() # Выйди нахуй блять
