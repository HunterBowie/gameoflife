import pygame
from .WindowLib.window import Window
from .WindowLib.colors import Colors
from .GameController import GameController
from .Constants import Constants


class GameWindow(Window):
    def __init__(self):
        super().__init__(Constants.SCREEN_SIZE)
        self.set_caption("Game of Life")
        self.set_icon(Constants.GAME_ICON)
        self.bg_color = Colors.WHITE
        self.set_interface(GameController)
        

        