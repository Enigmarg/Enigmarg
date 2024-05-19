import pygame

class ImageButton:
    def __init__(self, position:tuple[int,int], default_image:pygame.Surface, hover_image:pygame.Surface):
        self.position = position
        self.default_image = default_image
        self.hover_image = hover_image
        self.image = self.default_image
        self.rect = self.image.get_rect(topleft=self.position)
        self.state = 0

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def check_hover(self) -> bool:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.hover_image
            if pygame.mouse.get_pressed()[0]:
                self.image = self.hover_image
                return True
        self.image = self.default_image
        return False