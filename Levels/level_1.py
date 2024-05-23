import pygame
from pytmx import pytmx
from pytmx.util_pygame import load_pygame
from Levels.level import Level
from Levels.level_3 import Level3
from Classes.player import Player

class Level1(Level):
    def __init__(self, screen, transition_call):
        super().__init__(screen, transition_call)
        self.player = Player(pygame.Vector2(300, 550))
        self.x = 0
        self.cloudx = 0
        self.images = {}
        self.score = None
        self.obstacles: pygame.sprite.Group
        self.layers = {}
        self.door: pygame.sprite.Sprite

    def load(self):
        tmx_data = load_pygame("./resources/level0.tmx")
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer: # type: ignore
                    self.layers[layer.name] = self.layers.get(layer.name, [])
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        self.layers[layer.name].append((x, y, tile))

        self.obstacles = pygame.sprite.Group()

        for obj in tmx_data.objects:
            if obj.type == "door":
                self.door = pygame.sprite.Sprite()
                self.door.rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
            else:
                obstacle = pygame.sprite.Sprite()
                obstacle.rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
                self.obstacles.add(obstacle)

        self.images = {
            "background": pygame.image.load("./resources/teste.png"),
            "clouds": pygame.image.load("./resources/clouds.png")
        }

        self.is_loaded = True

    def run(self):
        self.screen.fill("black")
        dt = pygame.time.get_ticks() / 1000

        self.screen.blit(self.images["clouds"], (self.cloudx, 0))
        self.screen.blit(self.images["background"], (self.x, 100))

        for _, tiles in self.layers.items():
            for tile in tiles:
                self.screen.blit(tile[2], (tile[0] * 30 + self.x * 2.5, tile[1] * 30))

        pygame.draw.rect(self.screen, "blue", self.door.rect)

        keys = pygame.key.get_pressed()
        self.player.acceleration = pygame.Vector2(0, 0)

        self.check_collision()

        if keys[pygame.K_UP]:
            self.player.walk("up")
        if keys[pygame.K_DOWN]:
            self.player.walk("down")
        if keys[pygame.K_LEFT]:
            self.player.walk("left")
        if keys[pygame.K_RIGHT]:
            self.player.walk("right")

        if self.player.acceleration.x != 0:
            if self.player.position.x > self.screen.get_width() / 2:
                self.x -= self.player.acceleration.x / 5
                self.cloudx -= self.player.acceleration.x / 3
                self.door.rect.x -= self.player.acceleration.x / 5 * 2.5


            if abs(self.x) > 2400:
                self.x = 0
            if abs(self.cloudx) > 2400:
                self.cloudx = 0

        self.player.move(dt)
        self.player.draw(self.screen)

    def check_collision(self):
        if self.check_door():
            self.is_active = False
            self.transition_call(Level3(self.screen, self.transition_call))
            return

        if not self.check_obstacles():
            self.player.change_movement(True)
        else:
            self.player.change_movement(False)

    def check_obstacles(self):
        return self.player.get_rect().collidelist([obstacle.rect for obstacle in self.obstacles])

    def check_door(self):
        return self.player.get_rect().colliderect(self.door.rect)

    def get_status(self):
        return self.is_active
