from ..WindowLib.commands import Command

class PauseGameCommand(Command):
    def execute(self):
        self.interface.game.pause()