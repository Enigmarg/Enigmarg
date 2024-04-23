import pygame
from util import *

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False

            # Get a pool of all the pressed keys
            keys = pygame.key.get_pressed()
            
            self.screen.fill("purple")

            fps = font.render(f"FpS: %.0f" % (self.clock.get_fps()), 1, "white", "gray")

            self.screen.blit(fps, (20, 20))

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()
