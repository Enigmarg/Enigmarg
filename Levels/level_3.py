import pygame
from Levels.level import Level
from UI.button import Button
from UI.typography import Typography

# TELA DE RANKING

class Level3(Level):
    def __init__(self, screen, transition_call):
        super().__init__(screen, transition_call)
        self.screen = screen
        self.voltar = Button((225, 450), (150, 50), pygame.Color("gray"), "Voltar")
        self.images = {}
        self.texts = []
        self.pos = 0
        self.text = "Quais são os principais tópicos que devem ser abordados no parágrafo introdutório de uma redação modelo ENEM?"

    def load(self):
        self.is_loaded = True
        self.images = {
            "background": pygame.image.load("./resources/background.png").convert()
        }

        self.texts = []
        chars = []
        total_w = 0
        indice = 0
        h = 0
        chars = self.text.split(" ")
        for i in chars:
            t = pygame.font.Font("./resources/fonts/monogram.ttf", 32).render(i, True, "black")
            indice = chars.index(i)
            if total_w + t.get_width() > 365:
                h += 20
                total_w = 0
                self.texts.append(Typography((10, h), ' '.join(chars[:indice]), "black"))
                chars = chars[indice:]

            total_w += t.get_width()

        print(total_w)


        self.is_loaded = all(image is not None for image in self.images.values())

    def run(self):
        self.screen.fill("black")
        self.screen.blit(self.images["background"], (self.pos, 0))
        self.screen.blit(self.images["background"], (self.pos - self.screen.get_width(), 0))

        self.pos += 1

        if self.pos >= self.screen.get_width():
            self.pos = 0

        rect = pygame.Rect(0, 0, 500, 500)
        pygame.draw.rect(self.screen, "green", rect)
        for i in self.texts:
            i.draw(self.screen)
