from ..WindowLib.commands import Command

class ClearGameCommand(Command):
    def execute(self):
        self.interface.grid.generate_empty_grid()