from .States import *


class SaveMenu(States):
    def __init__(self, sprite_groups):
        States.__init__(self, sprite_groups)
        self.next = "game"

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.done = True

    def update(self, screen):
        self.screen.fill("blue")

    def draw(self):
        pass

