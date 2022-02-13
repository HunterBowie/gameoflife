import pygame
from .event import Event

class KeyPress(Event):
    def __init__(self, key, interface, on_held=False):
        super().__init__(interface)
        self.key = key
        self.on_held = on_held

    def eventloop(self, event):
        if event.type == pygame.KEYDOWN and not self.on_held:
            if event.key == self.key:
                self.trigger()
    
    def update(self):
        if pygame.key.get_pressed()[self.key] and self.on_held:
            self.trigger()