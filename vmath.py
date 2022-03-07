from math import sqrt, pow

class vec2:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def ToTuple(self):
		return (self.x, self.y)

def length(v : vec2):
	return sqrt(pow(v.x, 2) + pow(v.y, 2))

def normalize(v : vec2):
	l = length(v)
	return vec2(v.x / l, v.y / l)

def distance(a : vec2, b : vec2):
	return length(vec2(a.x - b.x, a.y - b.y))
