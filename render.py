import pygame
from util import SCENES, WINDOW_SIZE, ease_in_out_cubic


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
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
        self.scene_list = SCENES
        self.active_scene = self.initialize_scene()

    # Changes the scene and unloads the previous
    def change_scene(self, current_scene, next_scene):
        self.transition(current_scene, next_scene)

    # Loads the next scene and returns it
    def initialize_scene(self):
        scene = self.scene_list[self.current_scene](
            self.screen)
        scene.is_active = True
        return scene

    # Getter for all the lists
    def get_available_scenes(self):
        return self.scene_list

    # Getter for active scene
    def get_active_scene(self):
        return self.active_scene

    # Transition animation for scene
    def transition(self, current_scene, next_scene):
        # Initialize variables for transition
        # Creates overlay surface with colorkey
        radius = 600
        on_transition = True
        transition_delay = 150
        growing = False
        overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
        overlay.set_colorkey(pygame.Color("green"))

        while on_transition:
            for i in range(1, transition_delay):
                # Return value from formula
                r = ease_in_out_cubic(i/transition_delay) * radius
                if not growing:
                    # Invert formula
                    r = (-1 * r) + 600
                overlay.fill("black")
                self.active_scene.run()
                pygame.draw.circle(overlay, pygame.Color(
                    0, 255, 0), (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2), r)
                self.screen.blit(overlay, (0, 0))

                pygame.display.flip()

                if i == transition_delay - 1 and not growing:
                    self.previous_scene = current_scene

                    if current_scene is not None:
                        self.previous_scene.is_active = False

                    self.current_scene = next_scene

                    active = self.initialize_scene()

                    self.active_scene = active
                    growing = True
                elif i == transition_delay - 1 and growing:
                    on_transition = False
