from tile import Tile

class Plant(Tile):
    def __init__(self, position, sprite):
        super().__init__(position, 0, 0, sprite)