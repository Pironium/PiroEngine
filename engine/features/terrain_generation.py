# Python code for terrain generation in PiroEngine

import numpy as np

class TerrainGenerator:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        self.seed = seed
        if seed is not None:
            np.random.seed(seed)

    def generateTerrain(self):
        # Initialize an empty terrain map
        terrain = np.zeros((self.width, self.height))

        # Apply Perlin noise to create a realistic terrain
        scale = 10.0  # Adjust the scale for different terrains
        octaves = 6   # Adjust the number of octaves for complexity
        persistence = 0.5
        lacunarity = 2.0

        for x in range(self.width):
            for y in range(self.height):
                amplitude = 1.0
                frequency = 1.0
                noise_height = 0.0

                for _ in range(octaves):
                    sample_x = x / scale * frequency
                    sample_y = y / scale * frequency

                    noise_height += (np.interp(sample_x, [0, 1], [-1, 1]) *
                                     np.interp(sample_y, [0, 1], [-1, 1]) * amplitude)

                    amplitude *= persistence
                    frequency *= lacunarity

                terrain[x][y] = noise_height

        return terrain

# Example usage:
if __name__ == "__main__":
    width = 256
    height = 256
    seed = 42  # You can change the seed for different terrains

    terrain_generator = TerrainGenerator(width, height, seed)
    terrain = terrain_generator.generateTerrain()
    # Use the generated terrain for your game
