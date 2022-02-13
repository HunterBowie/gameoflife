import pygame

class Text:
    def __init__(self, x, y, string, font_file=pygame.font.get_default_font(),
    size=30, color=(0, 0, 0), alpha=0, antialias=True, positioner=None):
        self.x = x
        self.y = y
        self.string = string
        self.font_file = font_file
        self.size = size
        self.color = color
        self.alpha = alpha
        self.antialias = antialias
        self.font = pygame.font.Font(self.font_file, self.size)

        if positioner:
            positioner.position(self)


    
    def add(self, string):
        self.string = self.string + string
    
    def pop(self):
        char = self.string[len(self.string)-1]
        self.string = self.string[:len(self.string)-1]
        return char

    
    def get_width(self):
        return self.get_surf().get_width()
    
    def get_height(self):
        return self.get_surf().get_height()
    
    def get_surf(self):
        self.font = pygame.font.Font(self.font_file, self.size)
        return self.font.render(self.string, self.antialias, self.color)
    
    def render(self, screen):
        screen.blit(self.get_surf(), (self.x, self.y))
    
    def center_y(self, rect):
        self.y = rect.center[1]-self.get_height()/2

    def center_x(self, rect):
        self.x = rect.center[0]-self.get_width()/2
    
    def center(self, rect):
        self.center_x(rect)
        self.center_y(rect)
    
    def get(self):
        return self.string
    
    def set(self, string):
        self.string = string
    
    def get_positioning_data(self):
        return self.x, self.y, self.get_width(), self.get_height()
    
    def set_positioning_data(self, x, y):
        self.x = x
        self.y = y

    
    @staticmethod
    def create_with_bg(bg_size, bg_color, text):
        surf = pygame.Surface(bg_size)
        surf.fill(bg_color)
        text.center(surf.get_rect())
        text.render(surf)
        return surf
    
    @staticmethod
    def get_text_size(string, size=30, font_file=pygame.font.get_default_font()):
        t = Text(0, 0, string, font_file, size)
        return t.get_width(), t.get_height()
