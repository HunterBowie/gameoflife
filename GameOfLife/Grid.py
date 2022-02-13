from .Constants import Constants
import random, pygame

class Grid:
    def __init__(self, x, y, width, height, cell_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rows = self.height//self.cell_size
        self.cols = self.width//self.cell_size
        self.generate_empty_grid()
    
    def get_adjacent_cells(self, row, col):
        adjacent_cells = []

        adjacent_cells.append((row-1, col))
        adjacent_cells.append((row+1, col))
        adjacent_cells.append((row, col-1))
        adjacent_cells.append((row, col+1))
        adjacent_cells.append((row-1, col+1))
        adjacent_cells.append((row+1, col+1))
        adjacent_cells.append((row+1, col-1))
        adjacent_cells.append((row-1, col-1))

        checked_adjacent_cells = []
        for cell_pos in adjacent_cells:
            if cell_pos[0] < 0:
                continue
            if cell_pos[0] > self.rows-1:
                continue
            if cell_pos[1] < 0:
                continue
            if cell_pos[1] > self.cols-1:
                continue

            checked_adjacent_cells.append(cell_pos)
        return [self.grid[row][col] for row, col in checked_adjacent_cells]
    
    def num_living_adjacent_cells(self, row, col):
        adjacent_cells = self.get_adjacent_cells(row, col)
        living = 0
        for cell in adjacent_cells:
            if cell:
                living += 1
        return living
    
    def generate_random_grid(self):
        self.grid = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                if random.randint(0, 1):
                    new_row.append(True)
                else:
                    new_row.append(False)
            self.grid.append(new_row)
    
    def render(self, screen):
        x = self.x
        y = self.y

        for row in range(self.rows):
            for col in range(self.cols):
                occupied = self.grid[row][col]
                surf = pygame.Surface((self.cell_size, self.cell_size))
                if occupied:
                    surf.fill(Constants.OCCUPIED_COLOR)
                else:
                    surf.fill(Constants.EMPTY_COLOR)
                
                screen.blit(surf, (x, y))
                x += self.cell_size
            y += self.cell_size
            x = self.x
        
    def translate_mouse_pos(self, pos):
        pos = pos[0]-self.x, pos[1]-self.y
        return pos[1]//self.cell_size, pos[0]//self.cell_size

    def flip_cell(self, row, col):
        self.grid[row][col] = not self.grid[row][col]
    
    def set_cell(self, row, col, living):
        self.grid[row][col] = living

    def get_cell(self, row, col):
        return self.grid[row][col]
    
    def generate_empty_grid(self):
        self.grid = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                new_row.append(False)
            self.grid.append(new_row)

    
    def copy(self):
        grid = Grid(self.x, self.y, self.width, self.height, self.cell_size)
        return grid
    
    def num_live_cells(self):
        living = 0
        for row in self.grid:
            for cell in row:
                if cell:
                    living += 1
        return living
