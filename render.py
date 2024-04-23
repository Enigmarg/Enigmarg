import pygame
from util import SCENES


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        # Creates the display, the clock and sets a boolean to terminate the game
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # Instantiate the scene manager
        self.scene_manager = SceneManager(self.screen)
        self.scene_manager.change_scene("level0")

    def run(self):
        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False

            keys = pygame.key.get_pressed()

            # Change scene on key press
            if keys[pygame.K_e]:
                self.scene_manager.change_scene("level1")
            if keys[pygame.K_d]:
                self.scene_manager.change_scene("level0")

            # Execute scene "run" function
            self.scene_manager.get_scene().run()

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()


# The scene manager class
class SceneManager:
    def __init__(self, screen):
        self.current_scene = None
        self.screen = screen
        # Fetch scenelist from util file
        self.scene_list = SCENES
        print(SCENES["level1"])

    def change_scene(self, next_scene):
        self.current_scene = next_scene

    def get_scene(self):
        next_level = self.scene_list[self.current_scene]
        return next_level(self.screen)

    def get_available_scenes(self):
        return self.scene_list
