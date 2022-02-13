from .WindowLib.timer import Timer
from .Constants import Constants
from .Grid import Grid

class Game:
    def __init__(self, interface):
        self.interface = interface
        self.running = False
        self.timer = Timer()
        self.delay = Constants.GAME_START_DELAY
    
    def update(self):
        

        if self.running:
            if self.timer.ticks_passed(self.delay):
                
                self.timer.time_passed_reset()
                new_grid = self.interface.grid.copy()
                
                for row in range(self.interface.grid.rows):
                    for col in range(self.interface.grid.cols):
                        living = self.interface.grid.get_cell(row, col)
                        living_adjacent = self.interface.grid.num_living_adjacent_cells(row, col)

                        if living:
                            if living_adjacent in (2, 3):
                               new_grid.set_cell(row, col, True)
                        else:
                            if living_adjacent == 3:
                                new_grid.set_cell(row, col, True)
                
                self.interface.grid = new_grid
                
        
    
    def increase_speed(self):
        self.delay -= Constants.GAME_DELAY_CHANGE
        if self.delay < 0:
            self.delay = 0

    def decrease_speed(self):
        self.delay += Constants.GAME_DELAY_CHANGE
        if self.delay > Constants.GAME_DELAY_MAX:
            self.delay = Constants.GAME_DELAY_MAX

    
    def run(self):
        self.running = True
    
    def pause(self):
        self.running = False