import random

class WorldGenerator:
    def __init__(self):
        self.seed = random.randint(0, 10000)

    def generate_world(self, width, height):
        random.seed(self.seed)
        world = [[random.choice(['grass', 'water', 'mountain']) for _ in range(width)] for _ in range(height)]
        return world

if __name__ == "__main__":
    generator = WorldGenerator()
    world = generator.generate_world(10, 10)
    for row in world:
        print(" ".join(row))
