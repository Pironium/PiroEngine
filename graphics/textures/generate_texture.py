import numpy as np
from noise import snoise3
import matplotlib.pyplot as plt

def generate_perlin_texture(width, height, depth, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0, seed=0):
    """
    Generates a 3D Perlin noise texture.

    :param width: Width of the texture.
    :param height: Height of the texture.
    :param depth: Depth of the texture.
    :param scale: Scaling factor for the noise.
    :param octaves: Number of octaves in the noise.
    :param persistence: Persistence of the noise.
    :param lacunarity: Lacunarity of the noise.
    :param seed: Seed for the random generation.
    :return: 3D numpy array representing the generated texture.
    """
    np.random.seed(seed)
    texture = np.zeros((width, height, depth))
    
    for x in range(width):
        for y in range(height):
            for z in range(depth):
                sample_x = x / scale
                sample_y = y / scale
                sample_z = z / scale
                noise_value = snoise3(sample_x, sample_y, sample_z, octaves=octaves, persistence=persistence, lacunarity=lacunarity, base=seed)
                texture[x][y][z] = noise_value

    texture = (texture - np.min(texture)) / (np.max(texture) - np.min(texture))  # Normalize to [0, 1]
    return texture

if __name__ == "__main__":
    width, height, depth = 128, 128, 128
    scale = 10.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    seed = 42

    generated_texture = generate_perlin_texture(width, height, depth, scale, octaves, persistence, lacunarity, seed)
    
    # Visualize the generated texture (optional)
    plt.imshow(generated_texture[:, :, 64], cmap='viridis', origin='lower')
    plt.colorbar()
    plt.show()
