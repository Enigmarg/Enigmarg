import pygame
from util import Spritesheet

class Player:
    def __init__(self, position:pygame.Vector2) -> None:
        self.size = 30
        self.scale = 3
        self.speed = 6
        self.sprite_list = Spritesheet("./resources/player.png", self.size, self.size)
        self.position = position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.can_collide = True
        self.animations = { #Define os sprites de cada direção
            "down": [(0,0), (1,0), (2,0)],
            "up": [(0,1), (1,1), (2,1)],
            "left": [(0,2), (1,2), (2,2)],
            "right": [(0,3), (1,3), (2,3)]
        }
        self.mask = pygame.mask.from_surface(pygame.transform.scale_by( #Cria a máscara de colisão
            self.sprite_list.image_at(0, 0),
            self.scale))
        self.sprite = (0,0)
        self.facing = "down"
        self.is_colliding = False

    def walk(self, direction) -> None: #Define a direção do movimento
        match direction:
            case "up":
                if not self.is_colliding:
                    self.acceleration.y = -self.speed
            case "down":
                self.acceleration.y = self.speed
            case "left":
                self.acceleration.x = -self.speed
            case "right":
                self.acceleration.x = self.speed

    def move(self, dt) -> None: #Move o jogador
        self.acceleration += self.velocity
        self.position += self.velocity * dt + self.acceleration * .5
        self.change_sprite()

    def draw(self, screen) -> None: #Desenha o jogador
        if self.can_collide:
            self.collide_check(screen)
        screen.blit(pygame.transform.scale_by(self.sprite_list.image_at(
            self.sprite[0], self.sprite[1]), self.scale),
            (self.position.x, self.position.y))

    def collide_check(self, screen) -> None: #Verifica se o jogador colide com as bordas da tela
        self.position.x = max(self.position.x, 0)
        self.position.y = max(self.position.y, 0)
        if self.position.x + self.mask.get_size()[0] > screen.get_width():
            self.position.x = screen.get_width() - self.mask.get_size()[0]
        if self.position.y + self.mask.get_size()[1] > screen.get_height():
            self.position.y = screen.get_height() - self.mask.get_size()[1]

    def change_sprite(self): #Muda o sprite do jogador
        if self.acceleration.x > 0:
            self.facing = "right"
        elif self.acceleration.x < 0:
            self.facing = "left"
        elif self.acceleration.y > 0:
            self.facing = "down"
        elif self.acceleration.y < 0:
            self.facing = "up"

        if self.acceleration.length() > 0: #Animação de andar
            self.sprite = self.animations[self.facing][int(pygame.time.get_ticks() / 400) % 2 + 1]
        else:
            self.sprite = self.animations[self.facing][0]

    def get_rect(self): #Retorna o retângulo da máscara de colisão
        return pygame.rect.Rect(self.position.x + 15, self.position.y + 50,
                                 self.mask.get_size()[0] - 30, self.mask.get_size()[1] - 50)

    def change_movement(self, collided): #Muda o movimento do jogador
        self.position.y = self.position.y
        self.is_colliding = collided
