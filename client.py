from distutils.log import Log
from colorama import Fore
import threading as th
import keyboard as kb
import datetime
import colorama

import netclient

# Initing modules
colorama.init(convert = True)

class GameClient:
	def __init__(self, debug = True):
		self.debug = debug
		self.net_client = netclient.NetClient()
		self.text = ""

	def Log(self, text):
		print(Fore.WHITE + "[{time}][LOG]: {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text = text))

	def LogWarn(self, text):
		print(Fore.YELLOW + "[{time}][WARN]: {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text = text))

	def LogError(self, text):
		print(Fore.RED + "[{time}][ERROR]: {text}".format(time = datetime.datetime.now().strftime("%H:%M:%S"), text = text))

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

	def OnTick(self):
		self.OnNetTick()

	def RunMain(self):
		while True:
			self.OnTick()

	def OnRun(self):
		# Init keyboard input
		if self.debug:
			self.Log("Initing keyboard...")
		kb.hook(self.OnKeyEvent)

		# Connection to server and send player info
		if self.debug:
			self.Log("Connecting to {addr}:{port}".format(addr = "localhost", port = 3030))
		self.net_client.Connect("localhost", 3030)

		# Main
		a = th.Thread(target = self.RunMain)
		a.start()
