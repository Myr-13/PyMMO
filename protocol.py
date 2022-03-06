#
# DONT TOUCH ANY LINES HERE
#

# Consts
PACKET_DELEMITER = "|"

# Enums xd
# NetPack types
NETPACK_TYPE_PLAYERCONNECT = 0
NETPACK_TYPE_PLAYERDISCONNECT = 1
NETPACK_TYPE_PLAYERCHAT = 2
NETPACK_TYPE_PLAYERINPUT = 3

# Player flags
PLAYERFLAG_NONE = 0
PLAYERFLAG_CHAT = 1
PLAYERFLAG_MENUS = 2

# Classes and packers
class NetPack_PlayerConnect:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERCONNECT
		self.name = ""
		
	def Pack(self):
		data = "{0}|{1}".format(self.type, self.name)

		return str.encode(data)

class NetPack_PlayerDisconnect:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERDISCONNECT

	def Pack(self):
		data = "{0}".format(self.type)

		return str.encode(data)

class NetPack_PlayerChat:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERCHAT
		self.player = ""
		self.text = ""
	
	def Pack(self):
		data = "{0}|{1}|{2}".format(self.type, self.player, self.text)

		return str.encode(data)

class NetPack_PlayerInput:
	def __init__(self):
		self.type = NETPACK_TYPE_PLAYERINPUT
		self.moveDir = 0
		self.mouseX = 1
		self.mouseY = 0
		self.jump = 0
		self.playerFlag = PLAYERFLAG_NONE

	def Pack(self):
		data = "{0}|{1}|{2}|{3}|{4}|{5}".format(self.type, self.moveDir, self.mouseX, self.mouseY, self.jump, self.playerFlag)

		return str.encode(data)
