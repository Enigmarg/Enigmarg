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
        self.next_scene: Level  = Level0(self.screen, self.call_transition)
        self.loaded = False

    def run(self):
        # font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

        while self.running:
            if not self.loaded:
                self.transition += 1
                if self.transition > 60:
                    self.load_scene(self.next_scene)
                    self.loaded = True
                    self.transition = -60
            if self.transition < 0:
                self.transition += 1

            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
                    case pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            self.call_transition(Level1(self.screen, self.call_transition))
                        if event.key == pygame.K_e:
                            self.call_transition(Level0(self.screen, self.call_transition))
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

            pygame.display.update()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()

    def load_scene(self, scene: Level):
        scene.load()

        if scene.is_loaded:
            self.active_scene = scene

    def call_transition(self, scene: Level):
        self.next_scene = scene
        self.loaded = False
