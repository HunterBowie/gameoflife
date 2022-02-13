from ..WindowLib.commands import Command

class GenGameCommand(Command):
    def execute(self):
        self.interface.grid.generate_random_grid()