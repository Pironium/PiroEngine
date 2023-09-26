import numpy as np
import noise

class PerlinNoiseGenerator:
    def __init__(self, width, height, scale, octaves, persistence, lacunarity, seed):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed

    def generate_map(self):
        # Initialize an empty map
        world_map = np.zeros((self.height, self.width))

        # Generate random noise using Perlin noise
        for y in range(self.height):
            for x in range(self.width):
                sample_x = x / self.scale
                sample_y = y / self.scale
                noise_value = noise.pnoise2(sample_x,
                                            sample_y,
                                            octaves=self.octaves,
                                            persistence=self.persistence,
                                            lacunarity=self.lacunarity,
                                            repeatx=1024,
                                            repeaty=1024,
                                            base=self.seed)
                world_map[y][x] = noise_value

        # Normalize the noise values to the range [0, 1]
        world_map = (world_map - np.min(world_map)) / (np.max(world_map) - np.min(world_map))

        return world_map
