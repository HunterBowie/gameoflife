import pygame
from .WindowLib.colors import Colors


class Constants:
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 700
    SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT
    
    GAME_ICON = pygame.Surface((50, 50))
    GAME_ICON.fill(Colors.BLACK)

    OCCUPIED_COLOR = Colors.BLACK
    EMPTY_COLOR = Colors.WHITE

    GRID_RECT = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-120)

    GAME_DELAY_CHANGE = 25
    GAME_DELAY_MAX = 500
    GAME_START_DELAY = 250