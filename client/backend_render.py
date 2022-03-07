import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def rect_trans(win : pygame.Surface, color : tuple, x : int, y : int, w : int, h : int):
	s = pygame.Surface((w, h))
	s.set_alpha(color[3])
	s.fill((color[0], color[1], color[2]))
	win.blit(s, (x, y))
