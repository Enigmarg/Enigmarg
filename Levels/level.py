class Level:
    def __init__(self, screen):
        self.screen = screen
        self.is_active = False

    def run(self):
        pass

    def get_status(self):
        return self.is_active
