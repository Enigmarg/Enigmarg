from Levels.level import Level


class Level1(Level):
    def load(self):
        self.is_loaded = True

    def run(self):
        self.screen.fill("blue")

    def get_status(self):
        return self.is_active
