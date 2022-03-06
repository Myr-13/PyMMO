#
# DONT TOUCH ANY LINES HERE
#

# Enums xd
# NetPack types
NETPACK_TYPE_PLAYERCONNECT = 0
NETPACK_TYPE_PLAYERDISCONNECT = 1
NETPACK_TYPE_PLAYERCHAT = 2
NETPACK_TYPE_PLAYERINPUT = 3

# Classes and packers
class NetPack_PlayerConnect:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERCONNECT
		self.name = ""
		
	def Pack(self):
		data = "{0}|{1}`".format(self.type, self.name)

		return str.encode(data)

class NetPack_PlayerDisconnect:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERDISCONNECT

	def Pack(self):
		data = "{0}`".format(self.type)

		return str.encode(data)

class NetPack_PlayerChat:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERCHAT
		self.player = ""
		self.text = ""
	
	def Pack(self):
		data = "{0}|{1}|{2}`".format(self.type, self.player, self.text)

		return str.encode(data)

class NetPack_PlayerInput:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERINPUT
		self.jump = 0
		self.move_dir = 0
		self.mouse_x = 1
		self.mouse_y = 0

	def Pack(self):
		data = "{0}|{1}|{2}|{3}|{4}`".format(self.type, self.jump, self.move_dir, self.mouse_x, self.mouse_y)

		return str.encode(data)
