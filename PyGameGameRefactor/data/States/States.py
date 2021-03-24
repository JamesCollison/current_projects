import pygame
from ..effects import *


class States:

    def __init__(self, sprite_groups):
        self.done = False
        self.previous = None
        self.next = None
        self.quit = False
        self.input_allowed = True
        self.screen = pygame.display.get_surface()
        self.sprite_groups = sprite_groups

    def startup(self):
        pass

    def get_event(self, event):
        pass

    def update(self, screen):
        pass

    def draw(self):
        pass

    def cleanup(self):
        pass

    def lock_input(self):
        self.input_allowed = False

    def unlock_input(self):
        self.input_allowed = True
