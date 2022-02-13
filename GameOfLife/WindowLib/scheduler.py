import pygame

class Scheduler:
    def __init__(self, window):
        self.window = window
        self.commands = []
    
    def new_command(self, cmd):
        self.commands.append(cmd)
    
    def run(self):
        ended_commands = []
        for command in self.commands:
            command.execute()
        
            if command.is_finished():
                command.end()
                ended_commands.append(command)
        
        for command in ended_commands:
            self.commands.remove(command)
