

class Triggerable:
    def __init__(self, interface):
        self.interface = interface
        self.commands = []

    def set_commands(self, cmds):
        self.commands = cmds
    
    def trigger(self):
        for cmd in self.commands:
            self.interface.window.scheduler.new_command(cmd)

