import pygame

from UI.typography import Typography
from interfaces.database import Database

WINDOW_SIZE = (800, 600)
TILE_SIZE = 30
PLAYER_VELOCITY = 200
DATABASE = Database()

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
            print(f"Unable to load spritesheet image: {imagepath}")
            raise e
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

def break_line(text:str, start_pos: pygame.Vector2, max_size=300) -> list[Typography]:
    texts = []
    chars = []
    total_w = 0
    indice = 0
    chars = text.split(" ")
    for i in chars:
        t = pygame.font.Font("./resources/fonts/monogram.ttf", 32).render(i, True, "black")
        indice = chars.index(i)
        if total_w + t.get_width() > max_size:
            start_pos.y += 20
            total_w = 0
            texts.append(Typography(((start_pos.x, start_pos.y)),
                                     ' '.join(chars[:indice + 1]), "white"))
            chars = chars[indice + 1:]
        elif total_w < max_size and indice == len(chars) - 1:
            start_pos.y += 20
            texts.append(Typography(((start_pos.x, start_pos.y)),
                                     ' '.join(chars[:indice + 1]), "white"))

        total_w += t.get_width()

    return texts

class User:
    def __init__(self, id):
        self.player_id = id

    def get_id(self) -> int:
        return self.player_id

    def set_id(self, id):
        self.player_id = id

USER = User(None)
