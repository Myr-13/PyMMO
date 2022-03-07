from client.utilsclient import *

class Menus:
	def __init__(self, win, ui):
		self.in_game = False
		self.win = win
		self.ui = ui

	def OnInit(self, play_func, exit_func):
		self.ui.CreateButton((20, 20), (120, 35), COLOR_WHITE, play_func)
		self.ui.CreateButton((20, 70), (120, 35), COLOR_WHITE, exit_func)

	def OnTick(self):
		self.ui.OnTick()

	def OnRender(self):
		self.ui.OnRender()
