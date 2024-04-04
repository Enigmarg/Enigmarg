import pygame

class Engine():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.debug = False
        
    def run(self):
        font = pygame.font.Font("./resources/fonts/monogram.ttf", 32)

        while self.running:

            self.screen.fill(pygame.Color(255, 185, 87))

            self.screen.blit(font.render(f"FPS: %.0f" % (self.clock.get_fps()), 1, "black", "gray"), (10, 10))
            
            logo = font.render("ENIGMARG", 1, "WHITE", "BLACK")
            self.screen.blit(logo, (400 - logo.get_width() / 2, 200 - logo.get_height() / 2))
            
            btn = font.render("Jogar", 1, "white", "black")
            self.screen.blit(btn, (400 - btn.get_width() / 2, 300 - btn.get_height() / 2))

            btn2 = font.render("Ranking", 1, "white", "black")
            self.screen.blit(btn2, (400 - btn2.get_width() / 2, 350 - btn2.get_height() / 2))

            btn3 = font.render("Sair", 1, "white", "black")
            self.screen.blit(btn3, (400 - btn3.get_width() / 2, 400 - btn3.get_height() / 2))

            # Cria uma pool para todos os eventos do jogo
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        self.running = False
            
            dt = self.clock.tick(60)
            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    Engine().run()