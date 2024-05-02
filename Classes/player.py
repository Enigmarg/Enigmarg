import pygame

class Player:
    def __init__(self) -> None:
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.size = 50
        self.color = pygame.Color("red")

    def move(self, dt) -> None:
        self.acceleration += self.velocity
        self.position += self.velocity * dt + self.acceleration * .5

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color,
                          (self.position.x, self.position.y, self.size, self.size))
