import pygame
from .clock import Clock
from .scheduler import Scheduler
from .colors import Colors


class Window:
    def __init__(self, screen_size):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = Clock(self)
        self.scheduler = Scheduler(self)
        self.interface = None

        self.running = False
        
        self.bg_color = Colors.RED
    
    def set_display_color(self, color):
        self.bg_color = color
        
    def set_interface(self, interface):
        self.interface = interface(self)
    
    def set_caption(self, caption):
        self.caption = caption
        pygame.display.set_caption(self.caption)
    
    def set_icon(self, icon):
        self.icon = icon
        pygame.display.set_icon(self.icon)
    
    def start(self):
        self.running = True
        while self.running:
            self.update()
        pygame.quit()
    
    def stop(self):
        self.running = False
    
    def update(self):
        self.scheduler.run()
        
        if self.interface:
            self.interface.update()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()

        pygame.display.update()
        self.screen.fill(self.bg_color)
        self.clock.update()

