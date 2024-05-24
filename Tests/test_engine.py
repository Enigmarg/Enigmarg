import unittest
from unittest.mock import Mock, patch
import pygame
from Levels.level import Level
from Levels.level_0 import Level0
from engine import Engine

class TestEngine(unittest.TestCase):
    def setUp(self):
        self.engine = Engine()

    def test_init(self):
        self.assertIsInstance(self.engine, Engine)
        self.assertTrue(self.engine.running)
        self.assertEqual(self.engine.transition, 0)
        self.assertIsNone(self.engine.active_scene)
        self.assertIsNone(self.engine.previous_scene)
        self.assertIsInstance(self.engine.next_scene, Level0)
        self.assertFalse(self.engine.loaded)

    @patch('pygame.event.get')
    def test_run(self, mock_get):
        mock_get.return_value = [Mock(type=pygame.QUIT)]
        self.engine.run()
        self.assertFalse(self.engine.running)

    @patch('pygame.event.get')
    def test_keydown_escape(self, mock_get):
        mock_get.return_value = [Mock(type=pygame.KEYDOWN, key=pygame.K_ESCAPE)]
        self.engine.run()
        self.assertFalse(self.engine.running)

    def test_load_scene(self):
        scene = Mock(spec=Level)
        scene.is_loaded = True
        self.engine.load_scene(scene)
        self.assertEqual(self.engine.active_scene, scene)

    def test_call_transition(self):
        scene = Mock(spec=Level)
        self.engine.call_transition(scene)
        self.assertEqual(self.engine.next_scene, scene)
        self.assertFalse(self.engine.loaded)

    def test_go_back(self):
        self.engine.previous_scene = Mock(spec=Level)
        self.engine.go_back()
        self.assertEqual(self.engine.next_scene, self.engine.previous_scene)
        self.assertFalse(self.engine.loaded)

    def test_quit(self):
        self.engine.quit()
        self.assertFalse(self.engine.running)

if __name__ == '__main__':
    unittest.main()
