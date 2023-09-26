import numpy as np
from noise import snoise3
import matplotlib.pyplot as plt

def generate_perlin_texture(width, height, depth, scale, octaves, persistence, lacunarity):
    texture = np.zeros((width, height, depth))

    for x in range(width):
        for y in range(height):
            for z in range(depth):
                texture[x, y, z] = snoise3(
                    x / scale,
                    y / scale,
                    z / scale,
                    octaves=octaves,
                    persistence=persistence,
                    lacunarity=lacunarity,
                    base=0,
                )

    return texture

if __name__ == "__main__":
    width, height, depth = 256, 256, 256
    scale = 20.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    generated_texture = generate_perlin_texture(
        width, height, depth, scale, octaves, persistence, lacunarity
    )

    plt.imshow(generated_texture[:, :, 128], cmap='terrain')
    plt.colorbar()
    plt.show()
