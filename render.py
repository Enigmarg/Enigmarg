import pygame
from util import *


class Engine():
    def __init__(self):
        # Initializes pygame modules
        pygame.init()

        # Creates the display, the clock and sets a boolean to terminate the game
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # Instantiate the scene manager
        self.sceneManager = SceneManager(self.screen)
        self.sceneManager.changeScene("level0")

    def run(self):
        font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

        while self.running:
            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_e]:
                self.sceneManager.changeScene("level1")
            if keys[pygame.K_d]:
                self.sceneManager.changeScene("level0")

            self.sceneManager.getScene().run()

            pygame.display.flip()

            # Limita o framerate para 60FPS
            self.clock.tick(60)

        pygame.quit()


# The scene manager class
class SceneManager:
    def __init__(self, screen):
        self.currentScene = None
        self.screen = screen
        # Fetch scenelist from util file
        self.sceneList = SCENES
        print(SCENES["level1"])
        pass

    def changeScene(self, nextScene):
        self.currentScene = nextScene

    def getScene(self):
        nextLevel = self.sceneList[self.currentScene]
        return nextLevel(self.screen)

    def getAvailableScenes(self):
        return self.sceneList
