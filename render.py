import pygame
from util import WINDOW_SIZE
from Classes.scene_manager import SceneManager


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        # Instantiate the scene manager
        self.scene_manager = SceneManager(self.screen)
        self.scene_manager.transition(None, "level0", "out")

    def run(self):
        while self.running:
            active_scene = self.scene_manager.get_active_scene()

            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            self.scene_manager.transition(
                                active_scene, "level0")
                        if event.key == pygame.K_e:
                            self.scene_manager.transition(
                                active_scene, "level1")
                        if event.key == pygame.K_q:
                            self.running = False

            # Execute scene "run" function
            active_scene.run()

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()
