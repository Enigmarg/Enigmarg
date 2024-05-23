import pygame
from Levels.level import Level
from UI.button import Button
from util import WINDOW_SIZE

# TELA DE RANKING

class Level4(Level):
    def __init__(self, screen, transition_call):
        super().__init__(screen, transition_call)
        self.screen = screen
        self.images = {}
        self.pos = 0

    def load(self):
        self.is_loaded = True
        self.images = {
            "background": pygame.image.load("./resources/background.png").convert()
        }

        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.images["background"], (self.pos - WINDOW_SIZE[0], 0))

        self.pos += 1

        if self.pos >= WINDOW_SIZE[0]:
            self.pos = 0
