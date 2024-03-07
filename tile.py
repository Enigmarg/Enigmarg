import pygame

class Tile():
    def __init__(self, position: tuple[int, int], type: int, state: int, sprite:object):
        self.position = position
        self.type = type
        self.state = state
        self.object = pygame.Rect(position[0], position[1], 50, 50) 
        self.sprite = sprite