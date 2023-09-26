import noise
import numpy as np

def generate_terrain(width, height, scale, octaves, persistence, lacunarity, seed):
    terrain = np.zeros((width, height))

    for i in range(width):
        for j in range(height):
            x = i / scale
            y = j / scale
            value = noise.pnoise2(x,
                                  y,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity,
                                  repeatx=1024,
                                  repeaty=1024,
                                  base=seed)
            terrain[i][j] = value

    return terrain
