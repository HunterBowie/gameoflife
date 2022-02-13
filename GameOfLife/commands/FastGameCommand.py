from ..WindowLib.commands import Command

class FastGameCommand(Command):
    def execute(self):
        self.interface.game.increase_speed()