import pygame
from pytmx import pytmx
from pytmx.util_pygame import load_pygame
from levels.level import Level
from levels.level_3 import Level3
from classes.player import Player

class Level1(Level):
    def __init__(self, screen, transition_call):
        super().__init__(screen, transition_call)
        self.player = Player(pygame.Vector2(300, 550))
        self.x = 0 #Posição do background
        self.cloudx = 0
        self.images = {}
        self.score = None
        self.obstacles: pygame.sprite.Group
        self.layers = {}
        self.door: pygame.sprite.Sprite

    def load(self):
        tmx_data = load_pygame("./resources/level0.tmx") #Carrega o arquivo tmx
        for layer in tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    self.layers[layer.name] = self.layers.get(layer.name, []) #Cria um dicionário com as camadas do mapa
                    tile = tmx_data.get_tile_image_by_gid(gid)
                    if tile:
                        self.layers[layer.name].append((x, y, tile))

        self.obstacles = pygame.sprite.Group() #Cria um grupo de sprites para os obstáculos

        for obj in tmx_data.objects:
            if obj.type == "door":
                self.door = pygame.sprite.Sprite() #Cria um sprite para a porta
                self.door.rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height) #Define a posição e o tamanho da porta
            else:
                obstacle = pygame.sprite.Sprite() #Cria um sprite para a colisão
                obstacle.rect = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height) #Define a posição e o tamanho da colisão
                self.obstacles.add(obstacle) #Adiciona a colisão ao grupo de sprites

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
                self.screen.blit(tile[2], (tile[0] * 30 + self.x * 2.5, tile[1] * 30)) #Desenha o mapa

        keys = pygame.key.get_pressed()
        self.player.acceleration = pygame.Vector2(0, 0)

        self.check_collision()

        if keys[pygame.K_UP]: #Define a direção do movimento
            self.player.walk("up")
        if keys[pygame.K_DOWN]:
            self.player.walk("down")
        if keys[pygame.K_LEFT]:
            self.player.walk("left")
        if keys[pygame.K_RIGHT]:
            self.player.walk("right")

        if self.player.acceleration.x != 0: #Move o background (parallax)
            if self.player.position.x > self.screen.get_width() / 2 and abs(self.x * 2.5) < 2300:
                self.x -= self.player.acceleration.x / 5
                self.cloudx -= self.player.acceleration.x / 3
                self.door.rect.x -= self.player.acceleration.x / 5 * 2.5

            if abs(self.x) > 2400: #Se o background sair da tela, volta para a posição inicial
                self.x = 0
            if abs(self.cloudx) > 2400:
                self.cloudx = 0

        self.player.move(dt)
        self.player.draw(self.screen)

    def check_collision(self):
        if self.check_door():
            self.is_active = False
            self.transition_call(Level3(self.screen, self.transition_call)) #Se o jogador colidir com a porta, muda para a próxima fase

        if not self.check_obstacles():
            self.player.change_movement(True) #Se o jogador não colidir com os obstáculos, ele pode se mover
        else:
            self.player.change_movement(False)

    def check_obstacles(self):
        return self.player.get_rect().collidelist([obstacle.rect for obstacle in self.obstacles]) #Verifica se o jogador colide com os obstáculos

    def check_door(self):
        return self.player.get_rect().colliderect(self.door.rect) #Verifica se o jogador colide com a porta

    def get_status(self):
        return self.is_active
