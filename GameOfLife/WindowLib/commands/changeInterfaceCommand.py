import pygame
from .command import Command

class ChangeInterfaceCommand(Command):
    def __init__(self, window, interface):
        super().__init__(window)
        self.interface = interface
    
    def execute(self):
        self.window.set_interface(self.interface(self.window))