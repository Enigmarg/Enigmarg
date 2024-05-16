import pygame
from util import WINDOW_SIZE
from Levels.level_0 import Level0
from Levels.level_1 import Level1
from Levels.level import Level


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.transition = 0
        self.active_scene: Level | None = None
        self.previous_scene: Level | None = None
        self.next_scene: Level  = Level0(self.screen, self.call_transition, self.quit)
        self.loaded = False

    def run(self):
        # font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)
        mixer = pygame.mixer
        #! MUDAR !!!!
        menu = mixer.Sound("./resources/shh.wav")
        menu.set_volume(0.6)
        menu.play(-1)

        while self.running:
            if not self.loaded:
                self.transition += 1
                if self.transition > 60:
                    self.load_scene(self.next_scene)
                    self.loaded = True
                    self.transition = -60
            if self.transition < 0:
                self.transition += 1

            # Creates an event loop
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            self.call_transition(Level1(self.screen, self.call_transition))
                        if event.key == pygame.K_e:
                            self.call_transition(
                                Level0(self.screen, self.call_transition, self.quit))
                        if event.key == pygame.K_q:
                            self.running = False

            if self.active_scene:
                self.active_scene.run()

            if self.transition:
                transition_surf = pygame.Surface(WINDOW_SIZE)
                transition_surf.set_colorkey("green")
                pygame.draw.circle(transition_surf, "green",
                                   (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2),
                                    (60 - abs(self.transition)) * 10)
                self.screen.blit(transition_surf, (0, 0))

            pygame.display.update() # type: ignore

            # Limits the frame rate to 60 FPS
            self.clock.tick(60)

        pygame.quit()

    def load_scene(self, scene: Level):
        self.previous_scene = self.active_scene
        scene.load()

        if scene.is_loaded:
            self.active_scene = scene

    def call_transition(self, scene: Level):
        self.next_scene = scene
        self.loaded = False

    def go_back(self):
        if self.previous_scene:
            self.call_transition(self.previous_scene)

    def quit(self):
        self.running = False
