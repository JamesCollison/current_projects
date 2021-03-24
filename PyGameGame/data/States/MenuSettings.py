from .States import *


class MenuSettings(States):
    def __init__(self, sprite_groups):
        States.__init__(self, sprite_groups)
        self.next = "menu"

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.done = True

    def update(self, screen):
        self.screen.fill("red")

    def draw(self):
        pass