import numpy as np
import noise

class ProceduralTextureGenerator:
    def __init__(self, width, height, depth, scale, octaves, persistence, lacunarity, seed):
        self.width = width
        self.height = height
        self.depth = depth
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed

    def generate_texture(self):
        texture = np.zeros((self.height, self.width, self.depth), dtype=np.float32)
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    nx = x / self.width - 0.5
                    ny = y / self.height - 0.5
                    nz = z / self.depth - 0.5

                    noise_value = self._generate_noise(nx, ny, nz)
                    texture[y][x][z] = noise_value

        return texture

    def _generate_noise(self, x, y, z):
        return noise.snoise3(
            x=self.scale * x,
            y=self.scale * y,
            z=self.scale * z,
            octaves=self.octaves,
            persistence=self.persistence,
            lacunarity=self.lacunarity,
            repeatx=self.width,
            repeaty=self.height,
            repeatz=self.depth,
            base=self.seed
        )

if __name__ == "__main__":
    width = 512
    height = 512
    depth = 64
    scale = 0.1
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    seed = 42

    texture_generator = ProceduralTextureGenerator(width, height, depth, scale, octaves, persistence, lacunarity, seed)
    texture = texture_generator.generate_texture()
    print("Generated 3D Procedural Texture:")
    print(texture)
