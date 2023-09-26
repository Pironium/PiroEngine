class PiroEngine:
    def __init__(self):
        self.game_objects = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def remove_game_object(self, game_object):
        self.game_objects.remove(game_object)

class GameObject:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0, 0)
        self.scale = (1, 1, 1)
        self.rotation = (0, 0, 0)

    def translate(self, x, y, z):
        self.position = (self.position[0] + x, self.position[1] + y, self.position[2] + z)

    def scale_up(self, factor):
        self.scale = (self.scale[0] * factor, self.scale[1] * factor, self.scale[2] * factor)

    def rotate(self, x, y, z):
        self.rotation = (self.rotation[0] + x, self.rotation[1] + y, self.rotation[2] + z)

if __name__ == "__main__":
    engine = PiroEngine()
    obj1 = GameObject("Cube")
    obj2 = GameObject("Sphere")

    engine.add_game_object(obj1)
    engine.add_game_object(obj2)

    obj1.translate(1, 2, 0)
    obj2.scale_up(2)
    obj2.rotate(45, 30, 0)
