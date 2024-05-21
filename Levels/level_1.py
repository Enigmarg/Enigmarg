import pygame
from Levels.level import Level
from Classes.player import Player
from Levels.level_3 import Level3
from UI.score import Score
from pytmx.util_pygame import load_pygame
from pytmx import pytmx

class Level1(Level):
    def __init__(self, screen, transition_caller):
        super().__init__(screen, transition_caller)
        self.player = Player(pygame.Vector2(300, 400))
        self.x = 0
        self.cloudx = 0
        self.images = {}
        self.score = None

    def load(self):
        self.layers = {}

        tmx_data = load_pygame("./resources/level0.tmx")
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    self.layers[layer.name] = self.layers.get(layer.name, [])
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        self.layers[layer.name].append((x, y, tile))

        self.images = {
            "background": pygame.image.load("./resources/teste.png"),
            "clouds": pygame.image.load("./resources/clouds.png")
        }
    
        print(self.layers)

        self.screen.fill("black")

        self.screen.blit(self.images["clouds"], (0 + self.cloudx,0))
        self.screen.blit(self.images["clouds"], (self.cloudx + 800,0))
        self.screen.blit(self.images["clouds"], (self.cloudx - 800,0))
        self.screen.blit(self.images["background"], (0 + self.x, 100))
        self.screen.blit(self.images["background"], (self.x + 800, 100))
        self.screen.blit(self.images["background"], (self.x - 800, 100))

        for layer in self.layers:
            for tile in self.layers[layer]:
                self.screen.blit(tile[2], (tile[0] * 30 + self.x, tile[1] * 30))
        self.is_loaded = True

    def run(self):
        dt = pygame.time.get_ticks() / 1000

        keys = pygame.key.get_pressed()
        self.player.acceleration = pygame.Vector2(0, 0)

        if keys[pygame.K_UP]:
            self.player.walk("up")
        if keys[pygame.K_DOWN]:
            self.player.walk("down")
        if keys[pygame.K_LEFT]:
            self.player.walk("left")
        if keys[pygame.K_RIGHT]:
            self.player.walk("right")

        if self.player.acceleration.x > 0 or self.player.acceleration.x < 0:
            self.x -= self.player.acceleration.x / 5
            self.cloudx -= self.player.acceleration.x / 3

        if abs(self.x) > 800:
            self.transition_call(Level3(self.screen, self.transition_call))
            self.x = 0
        if abs(self.cloudx) > 800:
            self.cloudx = 0

        self.player.move(dt)
        self.player.draw(self.screen)

    def get_status(self):
        return self.is_active
