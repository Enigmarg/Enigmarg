import pygame
from UI.button import Button

class Level0():
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        self.screen.fill("red")
        jogar = Button(300, 200, 200, 100, pygame.Color("gray"), "Jogar")
        jogar.draw(self.screen)
        jogar.check_button()

        fechar = Button(400, 400, 100, 50, pygame.Color("gray"), "Fechar")
        fechar.draw(self.screen)
        fechar.check_button()
        
