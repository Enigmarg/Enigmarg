import pygame
from spritesheet import Spritesheet

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False

            # Renderiza o jogo
            player = pygame.Rect(0, 0, 50, 50)
            pygame.draw.rect(self.screen, "white", player)

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    Engine().run()