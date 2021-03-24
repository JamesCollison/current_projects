import pygame


class StateController:
    def __init__(self, **settings):
        self.size = None
        self.fps = None
        self.state_dict = None
        self.state_name = None
        self.state = None

        self.sprite_groups = None

        self.__dict__.update(settings)
        self.done = False
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        pygame.font.init()

    def setup_sprite_groups(self, sprite_groups):
        self.sprite_groups = sprite_groups

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def flip_state(self):
        self.state.done = False
        previous, self.state_name = self.state_name, self.state.next
        self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup()
        self.state.previous = previous

    def update(self):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen)

    def draw(self):
        self.state.draw()

    def transition_state(self):
        self.sprite_groups["transitions"].update()
        self.sprite_groups["transitions"].draw(self.screen)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.state.get_event(event)

    def main_game_loop(self):
        while not self.done:
            self.clock.tick(self.fps)
            self.event_loop()
            self.update()
            self.draw()
            self.transition_state()
            pygame.display.update()
