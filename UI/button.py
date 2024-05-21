import pygame

#Classe contendo características gerais de todos os botões de dentro do jogo.
class Button:
    def __init__(self, pos:tuple[float, float], size:tuple[float, float], color, text):
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.color = color
        self.text = text
        self.border_color = pygame.Color("white")
        self.clicked = False
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

    def check_button(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.color = pygame.Color("black")

            if pygame.mouse.get_pressed()[0] and not self.clicked:
                # Set the flag to True when the button is clicked
                self.clicked = True
        else:
            self.color = pygame.Color("gray")
            # Reset the flag when the button is not clicked
            self.clicked = False

        if not pygame.mouse.get_pressed()[0] and self.clicked:
            # Return True only when the button is clicked and the mouse button is released
            return True

        return False
