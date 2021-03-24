import sys
from data.Widgets.Button import Button
from .States import *


class Menu(States):
    def __init__(self, sprite_groups):
        States.__init__(self, sprite_groups)
        self.next = "game"
        self.buttons = None
        self.button_maker = None

        self.make_buttons()
        self.done_flag = False

        self.transition_speed = 2
        self.fade_color = pygame.Color("black")

    def make_buttons(self):
        button_text = ["new game", "load game", "quit"]
        button_commands = [self.new_game_clicked, self.load_game_clicked, self.quit_clicked]
        self.button_maker = MenuButtons(self.screen, button_text, button_commands)
        self.buttons = self.button_maker.get_buttons()

    def get_event(self, event):
        if self.input_allowed:
            if event.type == pygame.KEYDOWN:
                pass
            self.get_button_event(event)

    def get_button_event(self, event):
        for button in self.buttons:
            button.get_event(event)

    def update(self, screen):
        self.update_buttons()
        self.fill_screen()
        self.update_screen_transition()
        self.check_if_state_done()

    def check_if_state_done(self):
        if self.done_flag and not len(self.sprite_groups["transitions"]):
            self.state_done()

    def state_done(self):
        self.done = True
        self.fade_in()

    def update_screen_transition(self):
        self.sprite_groups["transitions"].update()

    def fill_screen(self):
        self.screen.fill("pink")  # TODO

    def update_buttons(self):
        for button in self.buttons:
            button.update()

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)

    def cleanup(self):
        self.done_flag = False
        self.unlock_input()

    def new_game_clicked(self):
        self.next = "game"
        self.lock_input()
        self.fade_out()
        self.done_flag = True

    def load_game_clicked(self):
        self.next = "save_menu"
        # load settings -> game state
        self.done = True

    def quit_clicked(self):
        self.done = True
        # self.next = exit
        # save settings -> quit state
        pygame.quit()
        sys.exit()

    def fade_out(self):
        FadeOut(self.fade_color, self.transition_speed, self.screen, self.sprite_groups["transitions"])

    def fade_in(self):
        FadeIn(self.fade_color, self.transition_speed * 2, self.screen, self.sprite_groups["transitions"])


class MenuButtons:
    def __init__(self, screen, button_text, commands):
        self.button_width = 250
        self.button_height = 50
        self.button_spacer = self.button_height * 1.5
        self.button_pos_x = screen.get_width() / 2 - self.button_width / 2
        self.button_pos_y = screen.get_height() / 4
        self.button_text = button_text
        self.commands = commands
        self.color = "white"
        self.border_color = "pink"
        self.border_hover_color = "purple"
        self.border_width = 15
        self.buttons = []
        self.make_buttons()

    def make_buttons(self):
        self.buttons = [
            Button((self.button_pos_x, self.button_pos_y + self.button_spacer * index, self.button_width,
                    self.button_height),
                   self.commands[index], text=self.button_text[index], color=self.color,
                   border_color=self.border_color, border_hover_color=self.border_hover_color,
                   border_width=self.border_width)
            for index, button_text in enumerate(self.button_text)
        ]

    def get_buttons(self):
        return self.buttons

    def __repr__(self):
        return [1, 2, 3]
