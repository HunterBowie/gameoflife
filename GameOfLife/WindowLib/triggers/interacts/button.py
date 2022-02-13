from turtle import pos, position
import pygame
from .interact import Interact
from ...entity import Entity
from ...private.loader import Loader



class Button(Interact):
    RELEASE_DELAY = 50
    def __init__(self, x, y, type, color, window, text=None, icon=None, positioner=None):
        super().__init__(window, positioner)
        self.image = Loader.get_button(type, color, False)
        self.clicked_image = Loader.get_button(type, color, True)
        self.current_image = self.image
        self.entity = Entity(x, y, self.image.get_width(), self.image.get_height())
        self.position()

        self.text = text
        if self.text:
            self.text.center(self.image.get_rect())
        self.icon = icon 
        if self.icon:
            self.icon.center(self.image.get_rect())

        self.clicked_timer = pygame.time.get_ticks()-Button.RELEASE_DELAY


    def update(self):
        pos = pygame.mouse.get_pos()
        if self.entity.rect.collidepoint(pos):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.clicked_timer = pygame.time.get_ticks()

        now = pygame.time.get_ticks()
        if now - self.clicked_timer < Button.RELEASE_DELAY:
            self.current_image = self.clicked_image
        else:
            self.current_image = self.image

    def eventloop(self, event):
        pos = pygame.mouse.get_pos()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.entity.rect.collidepoint(pos):
                self.trigger()
                self.clicked_timer = pygame.time.get_ticks()
            
    
    def render(self, screen):
        image = self.current_image.copy()
        if self.text:
            self.text.render(image)
        if self.icon:
            self.icon.render(image)
        pos = self.entity.get_pos()
        if self.current_image == self.clicked_image:
            screen.blit(image, (pos[0], pos[1]+4))
        else:
            screen.blit(image, self.entity.get_pos())
