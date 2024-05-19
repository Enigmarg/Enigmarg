import pygame
from Levels.level import Level
from Levels.level_1 import Level1
from Levels.level_2 import Level2
from UI.button import Button

# TELA DE MENU
class Level0(Level):
    def __init__(self, screen, transition_call, quit_game):
        super().__init__(screen, transition_call)
        self.quit = quit_game
        self.screen = screen
        self.pos = 0
        self.images = {}
        self.sair = Button((325, 480), (150, 50), pygame.Color("gray"), "Sair")
        self.ranking = Button((325, 420), (150, 50), pygame.Color("gray"), "Ranking")
        self.jogar = Button((300, 300), (200, 100), pygame.Color("gray"), "Jogar")
        self.logo: pygame.Surface

    def load(self):
        self.pos = 0

        self.images = {
            "background": pygame.image.load("./resources/background.png").convert(),
            "logo": pygame.image.load("./resources/logo.png").convert_alpha()
        }

        self.logo = pygame.transform.scale_by(self.images["logo"], 0.6)

        # Check if all images have been loaded successfully
        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.images["background"], (self.pos - self.screen.get_width(), 0))
        self.screen.blit(self.logo, ((self.screen.get_width() / 2 - self.logo.get_width()
                                    // 2), 70))

        self.pos += 1

        self.jogar.draw(self.screen)
        if self.jogar.check_button():
            self.transition_call(Level1(self.screen, self.transition_call))

        self.ranking.draw(self.screen)
        if self.ranking.check_button():
            self.transition_call(Level2(self.screen, self.transition_call, self.quit, Level0))

        self.sair.draw(self.screen)
        if self.sair.check_button():
            self.quit()

        if self.pos >= self.screen.get_width():
            self.pos = 0
