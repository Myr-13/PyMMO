#
# DONT TOUCH ANY LINES HERE
#

# Tipo enum xd
NETPACK_TYPE_PLAYERCONNECT = 0
NETPACK_TYPE_PLAYERDISCONNECT = 1
NETPACK_TYPE_PLAYERCHAT = 2

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
