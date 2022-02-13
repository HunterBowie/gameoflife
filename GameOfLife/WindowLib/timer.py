import pygame, time

class Timer:
    def __init__(self):
        self.ticks = 0
        self.stopped = False
        self.stop_time = 0
        self.passed_timer = pygame.time.get_ticks()
    
    def start(self):
        self.stopped = False
        self.stop_time = 0
        self.ticks = pygame.time.get_ticks()
    
    def stop(self):
        self.stopped = True
        self.stop_time = pygame.time.get_ticks()
    
    def time_passed_reset(self):
        self.passed_timer = pygame.time.get_ticks()
    
    def ticks_passed(self, ticks):
        now = pygame.time.get_ticks()
        if now - self.passed_timer >= ticks:
            return True
        return False
    
    def milliseconds_passed(milliseconds):
        pass


            
    
    def get(self):
        if self.stopped:
            return self.stop_time-self.ticks
        return pygame.time.get_ticks()-self.ticks
