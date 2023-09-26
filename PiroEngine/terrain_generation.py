import random

class TerrainGenerator:
    def __init__(self, seed):
        self.seed = seed

    def generateTerrain(self, width, height):
        terrain = [[0 for _ in range(width)] for _ in range(height)]

        # Complex terrain generation algorithm here
        for x in range(width):
            for y in range(height):
                terrain[y][x] = random.randint(0, 1)

        return terrain
