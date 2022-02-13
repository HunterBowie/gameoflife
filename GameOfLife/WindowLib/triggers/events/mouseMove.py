import pygame
from .event import Event

class MouseMove(Event):
    def __init__(self, interface):
        super().__init__(interface)
        self.init = True
        self.mouse_pos = (0, 0)
    
    def update(self):
        pos = pygame.mouse.get_pos()
        if self.init:
            self.mouse_pos = pos
            self.init = False
        
        else:
            if pos != self.mouse_pos:
                self.mouse_pos = pos
                self.trigger()
    
    def get(self):
        return self.mouse_pos