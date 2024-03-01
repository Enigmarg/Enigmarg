import pygame
from spritesheet import Spritesheet
from entity import Entity
from util import *

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        # Creates spritesheet and player object
        player_sheet = Spritesheet("./resources/player.png", tile_size, tile_size)
        player = Entity("Jogador", pygame.Vector2(0, 0), pygame.transform.scale(player_sheet.image_at(0, 0), (tile_size * 3, tile_size * 3)))
        
        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False

            # Get a pool of all the pressed keys
            keys = pygame.key.get_pressed()
            
            # Handle the specified keys
            if keys[pygame.K_UP]:
                player.pos.y -= player_velocity * delta_time
            if keys[pygame.K_DOWN]:
                player.pos.y += player_velocity * delta_time
            if keys[pygame.K_LEFT]:
                player.pos.x -= player_velocity * delta_time
            if keys[pygame.K_RIGHT]:
                player.pos.x += player_velocity * delta_time

            self.screen.fill("purple")

            # Renderiza o jogo            
            self.screen.blit(player.sprite, (player.pos.x, player.pos.y))
            pygame.display.flip()

            # Limita o framerate para 60FPS
            delta_time = self.clock.tick(60) / 1000

        pygame.quit()
