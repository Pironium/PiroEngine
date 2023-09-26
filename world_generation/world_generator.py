import random

class WorldGenerator:
    def __init__(self, seed=None):
        self.seed = seed if seed is not None else random.randint(0, 999999)
        self.randomizer = random.Random(self.seed)

    def generate_world(self, size, complexity):
        world = [[0 for _ in range(size)] for _ in range(size)]

        for _ in range(complexity):
            x, y = self.randomizer.randint(0, size - 1), self.randomizer.randint(0, size - 1)
            world[x][y] = self.randomizer.randint(1, 5)

        return world

if __name__ == "__main__":
    generator = WorldGenerator()
    world_size = 10
    complexity_level = 20
    generated_world = generator.generate_world(world_size, complexity_level)
    print(generated_world)
