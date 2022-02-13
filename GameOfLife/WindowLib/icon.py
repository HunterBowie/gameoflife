import pygame
from .private.loader import Loader
from .entity import Entity

class Icon:
    def __init__(self, x, y, type, scale=(50, 50)):
        self.type = type
        self.image = Loader.load_img(type)
        # implement full lib scaling 
        if scale != None:
            self.image = pygame.transform.scale(self.image, scale)
        self.entity = Entity(x, y, self.image.get_width(), self.image.get_height())
    
    def get_positioning_data(self):
        return self.entity.unpack()
    
    def set_positioning_data(self, x, y):
        self.entity.set_pos(x, y)


    def center_y(self, rect):
        self.entity.y = rect.center[1]-self.entity.width/2

    def center_x(self, rect):
        self.entity.x = rect.center[0]-self.entity.height/2

    def center(self, rect):
        self.center_x(rect)
        self.center_y(rect)

    def render(self, screen):
        screen.blit(self.image, self.entity.get_pos())