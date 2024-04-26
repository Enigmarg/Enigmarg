import pygame
from Levels.level import Level


class Level0(Level):
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
        self.pos += 1

        if self.pos >= self.screen.get_width():
            self.pos = 0

    def get_status(self):
        return self.is_active