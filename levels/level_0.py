import pygame
from interfaces.ranking import Ranking
from levels.level import Level
from levels.level_1 import Level1
from levels.level_2 import Level2
from UI.button import Button
from UI.image_button import ImageButton
from util import DATABASE, WINDOW_SIZE

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
        self.speaker: ImageButton

    def load(self):
        self.pos = 0

        self.images = {
            "background": pygame.image.load("./resources/background.png").convert(),
            "logo": pygame.image.load("./resources/logo.png").convert_alpha(),
            "speaker": pygame.transform.scale_by(pygame.image.load("./resources/speaker.png")
                                                 .convert_alpha(), 1.5),
            "speaker_d": pygame.transform.scale_by(pygame.image.load("./resources/speaker_d.png") #Imagem do botão de som desativado
                                                   .convert_alpha(), 1.5)
        }

        self.logo = pygame.transform.scale_by(self.images["logo"], 0.6)
        self.speaker = ImageButton((700, 500), self.images["speaker"], self.images["speaker_d"])

        # Verifica se todas as imagens foram carregadas
        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        if self.is_loaded:
            self.screen.fill("black")
            self.screen.blit(self.images["background"], (self.pos, 0))
            self.screen.blit(self.logo, ((WINDOW_SIZE[0] / 2 - self.logo.get_width()
                                        // 2), 70)) #Posiciona o logo no centro da tela
            self.pos -= 1

            self.jogar.draw(self.screen)
            if self.jogar.check_button():
                self.transition_call(Level1(self.screen, self.transition_call)) #Se o botão jogar for pressionado, muda para a tela de jogo

            self.ranking.draw(self.screen)
            if self.ranking.check_button():
                Ranking(DATABASE).create_ranking_screen()
                # self.transition_call(Level2(self.screen, self.transition_call, self.quit, Level0)) #Se o botão ranking for pressionado, muda para a tela de ranking

            self.sair.draw(self.screen)
            if self.sair.check_button():
                self.quit() #Se o botão sair for pressionado, fecha o jogo


            self.speaker.draw(self.screen)
            self.speaker.check_click()
            if self.speaker.state:
                pygame.mixer.pause() #Se o botão de som for pressionado, silencia o jogo
            else:
                pygame.mixer.unpause()

            if abs(self.pos) > WINDOW_SIZE[0]:
                self.pos = 0
