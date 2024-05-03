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
        border_color = pygame.Color("black") 
        border_width = 4  
        pygame.draw.rect(surface, self.color, self.rect, border_radius=10)
        pygame.draw.rect(surface, border_color, self.rect, border_width, border_radius=10)
        text_surface = self.font.render(self.text, True, pygame.Color("white"))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

#Pegando a posição do mouse para ativar a funcionalidade dos funções.
    def mouse_pos(self) -> tuple[int,int]:
        pos = pygame.mouse.get_pos()
        return pos

    def check_button(self) -> bool:
        if self.rect.collidepoint(self.mouse_pos()):
            self.color = pygame.Color("black")
            self.border_color = pygame.Color("white")
        
            if pygame.mouse.get_pressed()[0]:
                return True
        else:
            self.color = pygame.Color("gray")
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        return False
