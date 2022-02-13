from ..WindowLib.commands import Command

class SlowGameCommand(Command):
    def execute(self):
        self.interface.game.decrease_speed()