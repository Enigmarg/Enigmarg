import pygame
from util import WINDOW_SIZE
from Levels.level import Level
from UI.score import Score

# TELA DE RANKING

class Level4(Level):
    def __init__(self, screen, transition_call, score):
        super().__init__(screen, transition_call)
        self.screen = screen
        self.images = {}
        self.pos = 0
        self.font1 = pygame.font.Font("./resources/fonts/monogram.ttf", 40)
        self.font2 = pygame.font.Font("./resources/fonts/monogram.ttf", 30)
        self.font3 = pygame.font.Font("./resources/fonts/monogram.ttf", 20)
        self.texto1: pygame.Surface #Texto 1 = "Parabéns! Você concluiu todas as questões."
        self.texto2: pygame.Surface #Texto 2 = "Essa foi sua pontuação."
        self.texto3: pygame.Surface #Texto 3 = "Pressione esc para sair do jogo."

        self.logo: pygame.Surface
        self.pontuacao = Score((345, 400), (100, 50), pygame.Color("gray"))
        self.score = score


    def load(self):
        self.is_loaded = True
        self.images = {
            "background": pygame.image.load("./resources/background.png").convert(),
            "logo": pygame.image.load("./resources/logo.png").convert_alpha()
        }

        self.logo = pygame.transform.scale_by(self.images["logo"], 0.6)

        self.pontuacao.score = self.score #Pega a pontuação do jogador
        self.is_loaded = all(image is not None for image in self.images.values())
        self.texto1 = self.font1.render("Parabéns! Você concluiu todas as questões.", True, "white")
        self.texto2 = self.font2.render("Essa foi sua pontuação.", True, "white")
        self.texto3 = self.font3.render("Pressione esc para sair do jogo.", True, "PeachPuff4")

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos - WINDOW_SIZE[0], 0))
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.logo, ((self.screen.get_width() / 2 - self.logo.get_width()
                                        // 2), 70))

        self.screen.blit(self.texto1, (WINDOW_SIZE[0] / 2 - self.texto1.get_width() / 2, 300))
        self.screen.blit(self.texto2, (WINDOW_SIZE[0] / 2 - self.texto2.get_width() / 2, 350))
        self.screen.blit(self.texto3, (WINDOW_SIZE[0] / 2 - self.texto3.get_width() / 2, 500))

        self.pontuacao.draw(self.screen)

        self.pos += 1

        if self.pos >= WINDOW_SIZE[0]:
            self.pos = 0
