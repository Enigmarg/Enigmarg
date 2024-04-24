import pygame
from util import SCENES


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # Instantiate the scene manager
        self.scene_manager = SceneManager(self.screen)

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
                            self.scene_manager.change_scene(
                                active_scene, "level0")
                        if event.key == pygame.K_e:
                            self.scene_manager.change_scene(
                                active_scene, "level1")

            # Execute scene "run" function
            active_scene.run()

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()


# The scene manager class
class SceneManager:
    def __init__(self, screen):
        self.previous_scene = None
        self.current_scene = 'level0'
        self.screen = screen
        # Fetch scenelist from util file
        self.scene_list = SCENES
        self.active_scene = self.initialize_scene()

    def change_scene(self, current_scene, next_scene):
        self.transition(current_scene, next_scene)

    def initialize_scene(self):
        scene = self.scene_list[self.current_scene](
            self.screen)
        scene.is_active = True
        return scene

    def get_available_scenes(self):
        return self.scene_list

    def get_active_scene(self):
        return self.active_scene

    def transition(self, current_scene, next_scene):
        r = 600
        on_transition = True
        growing = False
        s = pygame.Surface((800, 600), pygame.SRCALPHA)
        rect = pygame.Rect(0, 0, 800, 600)
        s.set_colorkey(pygame.Color("green"))

        while on_transition:
            self.active_scene.run()
            s.fill("black")
            pygame.draw.circle(s, pygame.Color(0, 255, 0), rect.center, r)
            self.screen.blit(s, (0, 0))

            if not growing:
                r -= 1
                if r == -10:
                    self.previous_scene = current_scene

                    if current_scene is not None:
                        self.previous_scene.is_active = False

                    self.current_scene = next_scene

                    active = self.initialize_scene()

                    self.active_scene = active
                    growing = True
            else:
                r += 1
                if r >= 600:
                    on_transition = False
                    break

            pygame.display.flip()
