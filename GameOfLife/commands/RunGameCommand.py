from ..WindowLib.commands import Command

class RunGameCommand(Command):
    def execute(self):
        self.interface.game.run()