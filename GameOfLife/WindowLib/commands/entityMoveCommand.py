from shutil import move
from .command import Command

class EntityMoveCommmand(Command):
    def __init__(self, window, entity, move_x, move_y):
        super().__init__(window)
        self.entity = entity
        self.move_x = move_x
        self.move_y = move_y
    
    def execute(self):
        self.entity.move(self.move_x, self.move_y)
    
    def is_finished(self):
        return True