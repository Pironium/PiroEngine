import numpy as np
import noise

def generate_3d_terrain(width, height, depth, scale=100.0, octaves=6, persistence=0.5, lacunarity=2.0, seed=None):
    if seed is not None:
        np.random.seed(seed)

    terrain = np.zeros((depth, height, width), dtype=np.float32)

    for d in range(depth):
        for y in range(height):
            for x in range(width):
                nx = x / width - 0.5
                ny = y / height - 0.5
                nz = d / depth - 0.5

                value = noise.snoise3(nx * scale,
                                      ny * scale,
                                      nz * scale,
                                      octaves=octaves,
                                      persistence=persistence,
                                      lacunarity=lacunarity,
                                      repeatx=1024,
                                      repeaty=1024,
                                      repeatz=1024,
                                      base=seed)

                terrain[d][y][x] = value

    return terrain
