import pygame

#Classe contendo características gerais de todos os botões de dentro do jogo.
class Button:
    def __init__(self, pos:tuple[float, float], size:tuple[float, float], color, text):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.text = text
        self.font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

#Definindo a interface dos botões.
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, pygame.Color("white"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

#Pegando a posição do mouse para ativar a funcionalidade dos funções.
    def mouse_pos(self) -> tuple[int,int]:
        pos = pygame.mouse.get_pos()
        return pos

    def check_button(self):
        if self.rect.collidepoint(self.mouse_pos()):
            self.color = pygame.Color("black")
            if pygame.mouse.get_pressed()[0]:
                return True

        return False
