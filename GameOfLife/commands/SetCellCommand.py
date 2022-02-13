import pygame
from ..WindowLib.commands import Command

class SetCellCommand(Command):
    def __init__(self, interface, living):
        super().__init__(interface)
        self.living = living

    def execute(self):
        mouse_pos = pygame.mouse.get_pos()
        row, col = self.interface.grid.translate_mouse_pos(mouse_pos)
        self.interface.grid.set_cell(row, col, self.living)