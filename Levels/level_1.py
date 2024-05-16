import pygame
from Levels.level import Level
from Classes.player import Player
from UI.score import Score

class Level1(Level):
    def __init__(self, screen, transition_caller):
        super().__init__(screen, transition_caller)
        self.player = Player()
        self.x = 0
        self.cloudx = 0

    def load(self):
        self.images = {
            "background": pygame.image.load("./resources/teste.png").convert_alpha(),
            "cloud": pygame.image.load("./resources/clouds.png").convert_alpha()
        }
        self.is_loaded = True

    def run(self):
        dt = pygame.time.get_ticks() / 1000
        self.screen.fill("black")
        self.screen.blit(self.images["cloud"], (0 + self.cloudx,0))
        self.screen.blit(self.images["cloud"], (self.cloudx + 800,0))
        self.screen.blit(self.images["background"], (0 + self.x, 100))
        self.screen.blit(self.images["background"], (self.x + 800, 100))

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

        if self.player.acceleration.x > 0 or self.player.acceleration.x < 0:
            self.x -= self.player.acceleration.x / 5
            self.cloudx -= self.player.acceleration.x / 3

        if abs(self.x) > 800:
            self.x = 0
        if abs(self.cloudx) > 800:
            self.cloudx = 0
            
        self.player.move(dt)
        self.player.draw(self.screen)

        self.score = Score((10, 10), (100, 50), pygame.Color("gray"))
        self.score.draw(self.screen)

    def get_status(self):
        return self.is_active