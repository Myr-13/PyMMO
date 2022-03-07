from vmath import *

class Entity:
	def __init__(self, server, x = 0, y = 0):
		self.pos = vec2(x = x, y = y)
		self.type = ""
		self.server = server

	def NetworkClipped(self, pos):
		pass

	def NetTick(self, client_id):
		pass

class GameWorld:
	def __init__(self):
		self.entities = []
		self.tiles = []

	def LoadFromFile(self, file_path):
		pass