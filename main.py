import pygame
from spritesheet import Spritesheet
from tilemap import Tilemap

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        # Creates the tile map that fits the screen size and render it only once
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
                        # When the user presses the left mouse button it creates a plant
                        if pygame.mouse.get_pressed()[0]:
                            self.map.create_plant()

            # Prints the game FPS on the terminal
            print(str("FPS: %.1f" % (self.clock.get_fps())))

            # Limits the game fps to 60
            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()


if __name__ == "__main__":
    Engine().run()