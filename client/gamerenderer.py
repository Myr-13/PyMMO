from client.utilsclient import *
from client.backend_render import *

from gameworld import *

import pygame

class GameRenderer:
	def __init__(self, win : pygame.Surface):
		self.win = win

	def OnRender(self, world : GameWorld):
		# Render tiles
		for x in range(world.wight):
			for y in range(world.height):
				if world.tiles[x + y * world.wight] == TILE_SOLID:
					pygame.draw.rect(self.win, COLOR_WHITE, (x * 16, y * 16, 16, 16))
