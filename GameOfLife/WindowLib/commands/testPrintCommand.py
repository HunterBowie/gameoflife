import pygame
from .command import Command

class TestPrintCommand(Command):
    def __init__(self, window, msg):
        super().__init__(window)
        self.msg = msg
    
    def execute(self):
        print(f"--- {self.msg} ---")