import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

pygame.init()

class UI:
    def __init__(self, win : pygame.Surface):
        self.win = win
        self.buttons = []

    def CreateButton(self, pos, size, color, func):
        self.buttons.append([pos, size, color, func])

    def OnTick(self):
        pass

    def OnRender(self):
        pass
