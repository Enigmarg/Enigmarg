import pygame

class ImageButton:
    def __init__(self, position:tuple[int,int],
                  default_image:pygame.Surface, hover_image:pygame.Surface):
        self.position = position
        self.default_image = default_image
        self.hover_image = hover_image
        self.image = self.default_image
        self.rect = self.image.get_rect(topleft=self.position)
        self.clicked = False
        self.state = False

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.state:
            self.image = self.hover_image
        else:
            self.image = self.default_image

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                # Set the flag to True when the button is clicked
                if self.state == False:
                    self.state = True
                else:
                    self.state = False
                self.clicked = True
        else:
            # Reset the flag when the button is not clicked
            self.clicked = False
