import pygame
from Levels.level import Level
from Levels.level_1 import Level1
from UI.button import Button


class Level0(Level):
    def __init__(self, screen, transition_caller):
        super().__init__(screen, transition_caller)
        self.screen = screen
        self.pos = 0
        self.images = {}
        self.button = Button((400, 300), (200, 100), pygame.Color("red"), "Level 1")

    def load(self):
        self.pos = 0

        self.images = {
            "background": pygame.image.load("./resources/background.png").convert(),
        }

        # Check if all images have been loaded successfully
        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos,0))
        self.screen.blit(self.images["background"], (self.pos - self.screen.get_width(),0))

        self.button.draw(self.screen)
        if self.button.check_button():
            self.transition_call(Level1(self.screen, self.transition_call))

        self.pos += 1

        if self.pos >= self.screen.get_width():
            self.pos = 0
