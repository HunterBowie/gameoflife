import pygame
from .event import Event

class MouseHover(Event):
    def __init__(self, rect, interface):
        super().__init__(interface)
        self.rect = rect
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.trigger()
