from Levels.level import Level


class Level0(Level):
    def run(self):
        self.screen.fill("red")
        print("blip")

    def get_status(self):
        return self.is_active
