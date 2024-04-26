import pygame

class Level:
    def __init__(self, screen):
        """
        Initializes a Level object.

        Args:
            screen (pygame.Surface): The surface to render the level on.

        Attributes:
            screen (pygame.Surface): The surface to render the level on.
            is_active (bool): Indicates whether the level is currently active.
            is_loaded (bool): Indicates whether the level has been loaded.
        """
        self.screen: pygame.Surface = screen
        self.is_active: bool = False
        self.is_loaded: bool = False

    def load(self):
        """
        Loads the level data from a file.
        """
        pass

    def run(self):
        """
        This method is responsible for executing the logic of the level.
        """
        pass

    def get_status(self):
        """
        Returns the status of the object.

        Returns:
            bool: The status of the object.
        """
        return self.is_active
