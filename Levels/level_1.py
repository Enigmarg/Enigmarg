import pygame
from Levels.level import Level
from Classes.player import Player

class Level1(Level):
    def __init__(self, screen, transition_caller):
        super().__init__(screen, transition_caller)
        self.player = Player()

    def load(self):
        self.is_loaded = True

    def run(self):
        dt = pygame.time.get_ticks() / 1000
        self.screen.fill("blue")

        keys = pygame.key.get_pressed()
        self.player.acceleration = pygame.Vector2(0, 0)

        if keys[pygame.K_UP]:
            self.player.acceleration.y = -6
        if keys[pygame.K_DOWN]:
            self.player.acceleration.y = 6
        if keys[pygame.K_LEFT]:
            self.player.acceleration.x = -6
        if keys[pygame.K_RIGHT]:
            self.player.acceleration.x = 6

        self.player.move(dt)
        self.player.draw(self.screen)

    def get_status(self):
        return self.is_active
