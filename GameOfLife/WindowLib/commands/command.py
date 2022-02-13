import pygame

class Command:
    def __init__(self, interface):
        self.interface = interface
    
    def execute(self):
        pass

    def end(self):
        pass

    def is_finished(self):
        return True

        