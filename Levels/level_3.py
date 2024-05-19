import pygame
from Levels.level import Level
from UI.button import Button
from UI.typography import Typography
from UI.score import Score

# TELA DE JOGO

class Level3(Level):
    def __init__(self, screen, transition_call, previous_level, quit_game):
        super().__init__(screen, transition_call)
        self.screen = screen
        self.voltar = Button((225, 450), (150, 50), pygame.Color("gray"), "Voltar")
        self.images = {}
        self.texts = []
        self.pos = 0
        self.text = "Quais são os principais tópicos que devem ser abordados no parágrafo introdutório de uma redação modelo ENEM?"
        self.a = Button((183, 465), (205, 90), pygame.Color("red"), "Frase temática")
        self.b = Button((413, 325), (205, 90), pygame.Color("green"), "Conclusão do texto")
        self.c = Button((183, 325), (205, 90), pygame.Color("blue"), "Tese")
        self.d = Button((413, 465), (205, 90), pygame.Color("yellow"), "Apresentação do parágrafo D2")
        self.voltar = Button((10, 465), (150, 50), pygame.Color("gray"), "Voltar")
        self.score = None

    def load(self):
        self.is_loaded = True
        self.images = {
            "background": pygame.image.load("./resources/background.png").convert(),
            "chalkboard": pygame.transform.scale_by(pygame.image.load("./resources/chalkboard.png").convert_alpha(), 1.5)
        }

        self.texts = []
        chars = []
        total_w = 0
        indice = 0
        h = 20
        chars = self.text.split(" ")
        for i in chars:
            t = pygame.font.Font("./resources/fonts/monogram.ttf", 32).render(i, True, "black")
            indice = chars.index(i)
            if total_w + t.get_width() > 330:
                h += 20
                total_w = 0
                self.texts.append(Typography((self.screen.get_width() / 2 - 150 * 1.5 + 30, h), ' '.join(chars[:indice]), "white"))
                chars = chars[indice:]

            total_w += t.get_width()

        for i in self.texts:
            print(i.text)

        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.images["background"], (self.pos - self.screen.get_width(), 0))

        self.pos += 1

        if self.pos >= self.screen.get_width():
            self.pos = 0

        self.screen.blit(self.images["chalkboard"], (self.screen.get_width() / 2 - 150 * 1.5, 20))
        for i in self.texts:
            i.draw(self.screen)

        self.a.draw(self.screen)
        self.a.check_button()

        self.b.draw(self.screen)
        self.b.check_button()

        self.c.draw(self.screen)
        self.c.check_button()

        self.d.draw(self.screen)
        self.d.check_button()

        self.score = Score((10, 10), (100, 50), pygame.Color("gray"))
        self.score.draw(self.screen)

        self.voltar.draw(self.screen)
        self.voltar.check_button()