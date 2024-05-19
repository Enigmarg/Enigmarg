import pygame

WINDOW_SIZE = (800, 600)
TILE_SIZE = 30
PLAYER_VELOCITY = 200

class Spritesheet:
    def __init__(self, imagepath, size_x, size_y):
        # Sets the size of each individual sprite in the sheet
        self.size_x = size_x
        self.size_y = size_y
        self.rect = None
        self.image = None
        # Tries to load the spritesheet image and convert it to have alpha channels
        try:
            self.sheet = pygame.image.load(imagepath).convert_alpha()
        except Exception as e:
            print("Unable to load image from specified path:", str(e))

    # Access each individual sprite via its position in the sheet
    def image_at(self, x, y, color_key=None):
        self.rect = pygame.Rect(x * self.size_x, y * self.size_y, self.size_x, self.size_y)
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA).convert_alpha()
        self.image.blit(self.sheet, (0, 0), self.rect)

        if color_key is not None:
            if color_key == -1:
                color_key = self.image.get_at((0, 0))
            self.image.set_colorkey(color_key, pygame.RLEACCEL)

        return self.image