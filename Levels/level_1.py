from Levels.level import Level


class Level1(Level):
    def load(self):
        pass

    def run(self):
        self.screen.fill("red")

    def get_status(self):
        return self.is_active
