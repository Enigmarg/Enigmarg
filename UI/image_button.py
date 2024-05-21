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

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def check_click(self) -> bool:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                if not self.clicked:
                    self.image = self.hover_image
                    self.clicked = True
                    return self.clicked
                else:
                    self.image = self.default_image
                    self.clicked = False
                    return self.clicked

        return self.clicked
