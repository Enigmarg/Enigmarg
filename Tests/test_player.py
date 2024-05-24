import unittest
import pygame
from unittest.mock import Mock, patch
from Classes import player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.display = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
        self.position = pygame.Vector2(0, 0)
        self.player = player.Player(self.position)

    def test_init(self):
        self.assertEqual(self.player.position, self.position)
        self.assertEqual(self.player.velocity, pygame.Vector2(0, 0))
        self.assertEqual(self.player.acceleration, pygame.Vector2(0, 0))
        self.assertEqual(self.player.can_collide, True)
        self.assertEqual(self.player.facing, "down")
        self.assertEqual(self.player.is_colliding, False)

    def test_walk(self):
        self.player.walk("up")
        self.assertEqual(self.player.acceleration.y, -self.player.speed)
        self.player.walk("down")
        self.assertEqual(self.player.acceleration.y, self.player.speed)
        self.player.walk("left")
        self.assertEqual(self.player.acceleration.x, -self.player.speed)
        self.player.walk("right")
        self.assertEqual(self.player.acceleration.x, self.player.speed)

    @patch('pygame.time.get_ticks', return_value=1000)
    def test_change_sprite(self, mock_get_ticks):
        self.player.acceleration = pygame.Vector2(1, 0)
        self.player.change_sprite()
        self.assertEqual(self.player.facing, "right")
        self.assertEqual(self.player.sprite, self.player.animations["right"][1])

    def test_change_movement(self):
        self.player.change_movement(True)
        self.assertEqual(self.player.is_colliding, True)
        self.player.change_movement(False)
        self.assertEqual(self.player.is_colliding, False)

if __name__ == '__main__':
    unittest.main()
