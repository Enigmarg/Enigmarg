import pygame

#Classe contendo características gerais de todos os botões de dentro do jogo.
class Button:

    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

#Definindo a interface dos botões.
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, pygame.Color("white"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        print(self.color)

#Pegando a posição do mouse para ativar a funcionalidade dos funções.
    def mouse_pos(self) -> tuple[int,int]:
        pos = pygame.mouse.get_pos()
        return pos 
    
    def check_button(self):
        if self.rect.collidepoint(self.mouse_pos()):
            self.color = pygame.Color("black")
            print(self.color)
            print("collide")