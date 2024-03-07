import pygame
import random
from plant import Plant
from tile import Tile
from spritesheet import Spritesheet

class Tilemap():
    def __init__(self, dimension:tuple[int, int], tile_size:int, display):
        self.dimension = dimension
        self.tilesheet = Spritesheet("./resources/grass.png", 16, 16)
        self.tile_size = tile_size
        self.display = display
        self.tiles = {}
        self.plants = []

        for x in range(dimension[0]):
            for y in range(dimension[1]):
                self.tiles[x,y] = Tile((x * 50, y * 50), 1, 0, self.tilesheet.image_at(1, 1) if random.randrange(0, 100) <= 75 else self.tilesheet.image_at(random.randrange(0, 6), random.randrange(5, 6)))

    def render_map(self):
        tile_list = list(self.tiles.values())
        for tile in range(len(tile_list)):
            self.display.blit(pygame.transform.scale(tile_list[tile].sprite, (50, 50)), tile_list[tile].position)
    
    def render(self):
        pass

    def update_tile(self, tile):
        self.display.blit(pygame.transform.scale(tile.sprite, (50, 50)), tile.position)
        if tile.state == 1:
            pygame.draw.rect(self.display, "white", pygame.Rect(tile.position[0], tile.position[1], 50, 50), 5, 10)

    def render_plants(self, plant):
        self.display.blit(pygame.transform.scale(plant.sprite, (50, 50)), plant.position)
            
    def create_plant(self): 
        pos = pygame.mouse.get_pos()
        new_plant = Plant(self.get_tile(pos).position, Spritesheet("./resources/plants.png", 16, 16).image_at(random.randrange(1, 5), random.randrange(0, 2)))
        self.plants.append(new_plant)
        self.render_plants(new_plant)

    def get_tile(self, position):
        tile_list = list(self.tiles.values())

        for tile in range(len(tile_list)):
            if((tile_list[tile].position[0] / 50, tile_list[tile].position[1]/50) == (int(position[0]/50), int(position[1]/50))):
                return tile_list[tile]