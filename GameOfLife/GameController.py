import pygame
from .Constants import Constants
from .WindowLib.userInterface import UserInterface
from .WindowLib.triggers.interacts import Button
from .WindowLib.positioner import Positioner
from .WindowLib.text import Text
from .WindowLib.icon import Icon
from .WindowLib.colors import Colors
from .commands import RunGameCommand, ClearGameCommand, GenGameCommand, PauseGameCommand, SlowGameCommand, FastGameCommand, SetCellCommand
from .WindowLib.triggers.events import MouseClick
from .Grid import Grid
from .Game import Game

class GameController(UserInterface):
    def config(self):
        self.grid = Grid(Constants.GRID_RECT.x, Constants.GRID_RECT.y, Constants.GRID_RECT.width, Constants.GRID_RECT.height, 20)
        self.game = Game(self)
        self.speed_label = Text(40, -10, "Speed: ", positioner=Positioner(self, bottom_y=True))
        self.running_label = Text(10, -50, "Running: ", positioner=Positioner(self, bottom_y=True))
        self.speed_text = Text(40, -10, "", positioner=Positioner(self, bottom_y=True))
        self.running_text = Text(10, -50, "", positioner=Positioner(self, bottom_y=True))



        faster_button = self.new_interact(
            Button(-25, -55, "square", "green", self, icon=Icon(0, 0, "arrowUp"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        faster_button.set_commands([
            FastGameCommand(self)
        ])
        slower_button = self.new_interact(
            Button(-25, -5, "square", "green", self, icon=Icon(0, 0, "arrowDown"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        slower_button.set_commands([
            SlowGameCommand(self)
        ])
        run_button = self.new_interact(
            Button(-100, -55, "long", "blue", self, text=Text(0, 0, "Run"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        run_button.set_commands([
            RunGameCommand(self)
        ])
        pause_button = self.new_interact(
            Button(-100, -5, "long", "blue", self, text=Text(0, 0, "Pause"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        pause_button.set_commands([
            PauseGameCommand(self)
        ])
        clear_button = self.new_interact(
            Button(-300, -5, "long", "blue", self, text=Text(0, 0, "Clear"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        clear_button.set_commands([
            ClearGameCommand(self)
        ])
        generate_button = self.new_interact(
            Button(-300, -55, "long", "blue", self, text=Text(0, 0, "Generate"),
            positioner=Positioner(self, right_x=True, bottom_y=True))
        )
        generate_button.set_commands([
            GenGameCommand(self)
        ])


        left_mouse_click = self.new_event(
            MouseClick(self, Constants.GRID_RECT, mode="hold")
        )

        left_mouse_click.set_commands([
            SetCellCommand(self, True)
        ])

        right_mouse_click = self.new_event(
            MouseClick(self, Constants.GRID_RECT, mode="hold", hold_data=(0, 0, 1))
        )

        right_mouse_click.set_commands([
            SetCellCommand(self, False)
        ])


        
    def update(self):
        self.game.update()
        self.grid.render(self.window.screen)

        line_start, line_end = Constants.GRID_RECT.bottomleft, Constants.GRID_RECT.bottomright
        pygame.draw.line(self.screen, Colors.BLACK, line_start, line_end, 5)
        game_speed = Constants.GAME_DELAY_MAX - self.game.delay
        if self.game.running:
            self.running_text.color = Colors.GREEN
        else:
            self.running_text.color = Colors.RED
        self.speed_text.set(f"               {game_speed}")
        self.running_text.set(f"                   {self.game.running}")

        self.speed_text.render(self.window.screen)
        self.running_text.render(self.window.screen)
        self.speed_label.render(self.window.screen)
        self.running_label.render(self.window.screen)
        
        super().update()
