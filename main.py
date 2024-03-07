import pygame
from spritesheet import Spritesheet
from tilemap import Tilemap

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Tilemap((int(800 / 50), int(600 / 50)), 50, self.screen)
        self.map.render_map()

    def run(self):
        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            self.map.create_plant()

            # self.map.render()
            font = pygame.font.Font(pygame.font.get_default_font(), 32)

            # text = font.render(str("FPS: %.2f" % (self.clock.get_fps())), True, "black")
            # self.screen.blit(text, (0, 0))

            print(str("FPS: %.1f" % (self.clock.get_fps())))

            self.clock.tick(60)
            # self.map.update()
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    Engine().run()