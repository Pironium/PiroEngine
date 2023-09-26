import numpy as np
import noise

class TerrainGenerator:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        self.seed = seed if seed is not None else np.random.randint(0, 1000)

    def generate_terrain(self, scale=50.0, octaves=6, persistence=0.5, lacunarity=2.0):
        terrain = np.zeros((self.width, self.height))
        for x in range(self.width):
            for y in range(self.height):
                nx = x / self.width - 0.5
                ny = y / self.height - 0.5
                value = noise.snoise2(
                    nx * scale,
                    ny * scale,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    repeatx=self.width,
                    repeaty=self.height,
                    base=self.seed,
                )
                terrain[x][y] = value
        return terrain
