from client.backend_render import *

class Button:
	def __init__(self, x, y, w, h, color, func):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.color = color
		self.func = func
		self.mouse_hold = False

class UI:
	def __init__(self, win):
		self.win = win
		self.buttons = []

	# ===> Buttons
	def CreateButton(self, pos : tuple, size : tuple, color : tuple, func):
		self.buttons.append(Button(pos[0], pos[1], size[0], size[1], color, func))

	def ClearButtons(self):
		self.buttons.clear()

	# ===> Base
	def OnTick(self):
		mouse_pos = pygame.mouse.get_pos()
		is_click = pygame.mouse.get_pressed()[0]

		if not is_click:
			self.mouse_hold = False

		for button in self.buttons:
			rect = pygame.Rect(button.x, button.y, button.w, button.h)

			if rect.collidepoint(mouse_pos) and is_click and not self.mouse_hold:
				button.func()

		if is_click:
			self.mouse_hold = True

	def OnRender(self):
		for button in self.buttons:
			rect_trans(self.win, button.color, button.x, button.y, button.w, button.h)
