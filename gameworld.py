from vmath import *

# Entity
class Entity:
	def __init__(self, world, x = 0, y = 0):
		self.pos = vec2(x = x, y = y)
		self.type = ""
		self.world = world

	def NetworkClipped(self, pos : vec2) -> bool:
		if distance(pos, self.pos) < 1000:
			return True
		return False

	def NetTick(self, net):
		for ent in self.world.GetCharacters():
			if not self.NetworkClipped(ent.pos):
				continue

# Map items
TILE_AIR = 0
TILE_SOLID = 1

# Game world
class GameWorld:
	def __init__(self):
		self.entities = []
		self.tiles = []
		self.wight = 0
		self.height = 0
		self.lock_w = False

	def LoadFromFile(self, file_path):
		f = open(file_path, "r")
		data = f.read()
		f.close()
		data2 = ""
		data3 = []

		for ch in data:
			if ch != "\n":
				if not self.lock_w:
					self.wight += 1
				data2 += ch
			else:
				self.lock_w = True
				self.height += 1

		for a in data2:
			data3.append(int(a))

		self.tiles = tuple(data3)

	def GetCharacters(self):
		chrs = []
		for ent in self.entities:
			if ent.type == "character":
				chrs.append(ent)

		return chrs

	# ===> Base
	def OnTick(self):
		pass

	def OnNetTick(self, net_server):
		for conn in net_server.connections:
			for ent in self.entities:
				ent.NetTick(conn)
