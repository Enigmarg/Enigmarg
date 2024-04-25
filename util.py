from Levels.level_0 import Level0
from Levels.level_1 import Level1

WINDOW_SIZE = (800, 600)
TILE_SIZE = 30
PLAYER_VELOCITY = 200
SCENES = {"level0": Level0, "level1": Level1}


def ease_in_out_cubic(t: float):
    t *= 2
    if t < 1:
        return t * t * t / 2
    else:
        t -= 2
        return (t * t * t + 2) / 2
