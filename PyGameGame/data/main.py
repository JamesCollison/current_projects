import pygame
import sys
from data.States.StateController import StateController
from data.States.Menu import Menu
from data.States.Game import Game
from data.States.MenuSettings import MenuSettings
from data.States.SaveMenu import SaveMenu
from data.Settings import *


settings = {
    "size": RESOLUTION,
    "fps": FPS
}

app = StateController(**settings)

sprite_groups = {
    "effects": pygame.sprite.Group(),
    "transitions": pygame.sprite.Group(),
}

state_dict = {
    "menu": Menu(sprite_groups),
    "game": Game(sprite_groups),
    "menu_settings": MenuSettings(sprite_groups),
    "save_menu": SaveMenu(sprite_groups),
}

app.setup_sprite_groups(sprite_groups)
app.setup_states(state_dict, 'menu')
app.main_game_loop()
pygame.quit()
sys.exit()
