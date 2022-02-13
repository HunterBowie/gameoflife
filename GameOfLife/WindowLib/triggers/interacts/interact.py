import pygame
from ..triggerable import Triggerable

class Interact(Triggerable):
    def __init__(self, interface, positioner=None):
      super().__init__(interface)
      self.entity = None
      self.positioner = positioner

    def position(self):
      self.positioner.position(self)
    
    def set_pos(self, x, y):
      self.entity.set_pos(x, y)
    
    def get_positioning_data(self):
      return self.entity.unpack()
    
    def set_positioning_data(self, x,y):
      self.entity.set_pos(x, y)
    
