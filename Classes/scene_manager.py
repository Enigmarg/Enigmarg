import pygame
from Levels.level import Level
from Levels.level_0 import Level0
from Levels.level_1 import Level1
from util import WINDOW_SIZE


SCENES = {"level0": Level0, "level1": Level1}


def ease_in_out_cubic(t: float):
    t *= 2
    if t < 1:
        return t * t * t / 2
    else:
        t -= 2
        return (t * t * t + 2) / 2

# The scene manager class
class SceneManager:
    def __init__(self, screen):
        self.previous_scene: str | None = None
        self.current_scene: str = 'level0'
        self.screen: pygame.Surface = screen
        self.scene_list: dict = SCENES
        self.active_scene: Level = self.initialize_scene()

    # Loads the next scene and returns it
    def initialize_scene(self):
        scene: Level = self.scene_list[self.current_scene](
            self)
        scene.is_active = True
        scene.load()
        return scene

    # Getter for all the lists
    def get_available_scenes(self):
        return self.scene_list

    # Getter for active scene
    def get_active_scene(self):
        return self.active_scene

    # Transition animation for scene
    def transition(self, current_scene, next_scene, mode="both"):
        # Initialize variables for transition
        # Creates overlay surface with colorkey
        radius = WINDOW_SIZE[1]
        on_transition = True
        transition_delay = 150
        growing = False
        overlay = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
        overlay.set_colorkey(pygame.Color("green"))

        while on_transition:
            for i in range(1, transition_delay):
                # Return value from formula
                r = ease_in_out_cubic(i/transition_delay) * radius

                if mode == "in":
                    r = (-1 * r) + 600
                elif mode == "out":
                    r = r
                elif mode == "both":
                    if not growing:
                        r = (-1 * r) + 600

                overlay.fill("black")
                self.active_scene.run()

                pygame.draw.circle(overlay, pygame.Color("green"), (WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2), r)
                self.screen.blit(overlay, (0, 0))

                pygame.display.flip()

                if i == transition_delay - 1:
                    if mode is not "both":
                        on_transition = False
                        break
                    if not growing:
                        self.previous_scene = current_scene

                        if current_scene is not None:
                            self.previous_scene.is_active = False

                        self.current_scene = next_scene

                        active = self.initialize_scene() 

                        self.active_scene = active
                        if self.active_scene.is_loaded:
                            growing = True
                        break
                    elif growing:
                        on_transition = False