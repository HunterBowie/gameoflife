import pygame

class Clock:
    def __init__(self, window, fps=60):
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.window = window
    
    def update(self):
        self.clock.tick(self.fps)

    def wait(self, duration):
        self.clock.wait(duration)
