'''
    Returns a sliced spritesheet that you can access each individual sprite by providing it's x and y coordinates.
'''

import pygame

class Spritesheet(object):
    def __init__(self, imagepath, sizeX, sizeY):
        # Sets the size of each individual sprite in the sheet
        self.sizeX = sizeX
        self.sizeY = sizeY
        # Tries to load the spritesheet image and convert it to have alpha channels
        try:
            self.sheet = pygame.image.load(imagepath).convert_alpha()
        except:
            print("Unable to load image from specified path")

    # Access each individual sprite via it's position in the sheet
    def image_at(self, x, y, color_key = None):
        self.rect = pygame.Rect(x * self.sizeX, y * self.sizeY, self.sizeX, self.sizeY)
        self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA).convert_alpha()
        self.image.blit(self.sheet, (0, 0), self.rect)

        if color_key != None:
            if color_key == -1:
                color_key = self.image.get_at(0, 0)
            self.image.set_colorkey(color_key, pygame.RLEACCEL)
        
        return self.image
