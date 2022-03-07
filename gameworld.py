class Entity:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.type = ""

    def NetTick(self, net_server):
        pass

class GameWorld:
    def __init__(self):
        self.entities = []
        self.tiles = []
