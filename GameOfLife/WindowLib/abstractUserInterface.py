import pygame
from .triggers.interacts import Interact

class AbstractUserInterface:
    def __init__(self, window):
        self.window = window
        self.screen = window.screen
        
        self.run_eventloop = True
        self.sub_interfaces = []

        self.triggers = {
            "events": [],
            "interacts": []
        }
        
        self.config()
        
    def set_sub_interfaces(self, sub_interfaces):
        self.sub_interfaces = [sub_interface(self) for sub_interface in self.sub_interfaces]

    def config(self):
        pass


    def new_interact(self, interact, positioner):
        if positioner:
            positioner.position_interact(interact)

        self.triggers["interacts"].append(interact)
        return interact
    
    def new_event(self, event):
        self.triggers["events"].append(event)
        return event
    


    
    def eventloop(self, event):
        for interact_trigger in self.triggers["interacts"]:
            interact_trigger.eventloop(event)
        
        for event_trigger in self.triggers["events"]:
            event_trigger.eventloop(event)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.eventloop(event)

        if event.type == pygame.QUIT:
            self.window.stop()
    
    def update(self):
        if self.run_eventloop:
            for event in pygame.event.get():
                self.eventloop(event)

        for interact_trigger in self.triggers["interacts"]:
            interact_trigger.update()
        
        for event_trigger in self.triggers["events"]:
            event_trigger.update()
    

        for interact_trigger in self.triggers["interacts"]:
            interact_trigger.render(self.screen)
        
        for sub_interface in self.sub_interfaces:
            sub_interface.update()
    
        
            