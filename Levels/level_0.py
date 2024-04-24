from Levels.level import Level


class Level0(Level):
    def __init__(self, screen):
        super().__init__(screen)

    def run(self):
        self.screen.fill("red")

    def get_status(self):
        return self.isActive
