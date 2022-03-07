from client.utilsclient import *
from client.backend_render import *

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

class Menus:
	def __init__(self, win, ui):
		self.in_game = False
		self.pause = False
		self.win : pygame.Surface = win
		self.ui = ui

	def OnInput(self, key, state):
		if key == pygame.K_ESCAPE:
			if state == 1: # if state == CLIENTSTATE_INGAME
				self.pause = not self.pause

				self.ui.CreateButton((self.win.get_width() - 120, 20), (100, 35), COLOR_WHITE, self.disconnect_func)

	# ===> Base
	def CreateBaseMenu(self):
		self.ui.CreateButton((20, 20), (120, 35), COLOR_WHITE, self.play_func)
		self.ui.CreateButton((20, 70), (120, 35), COLOR_WHITE, self.exit_func)

	def OnInit(self, play_func, exit_func, disconnect_func):
		self.play_func = play_func
		self.exit_func = exit_func
		self.disconnect_func = disconnect_func

		self.CreateBaseMenu()

	def OnTick(self):
		self.ui.OnTick()

	def OnRender(self):
		self.ui.OnRender()

		if self.pause:
			rect_trans(self.win, (100, 100, 100, 150), 0, 0, self.win.get_width(), 100)
