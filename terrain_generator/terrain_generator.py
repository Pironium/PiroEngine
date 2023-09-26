# terrain_generator.py

import random

class TerrainGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain_map = [[0] * width for _ in range(height)]

    def generate_terrain(self, mountain_density=0.2, hill_density=0.3, river_density=0.1):
        self.generate_mountains(mountain_density)
        self.generate_hills(hill_density)
        self.generate_rivers(river_density)

    def generate_mountains(self, density):
        for _ in range(int(self.width * self.height * density)):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.terrain_map[y][x] = 1

    def generate_hills(self, density):
        for _ in range(int(self.width * self.height * density)):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.terrain_map[y][x] = 2

    def generate_rivers(self, density):
        for _ in range(int(self.width * self.height * density)):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.terrain_map[y][x] = 3

    def get_terrain_map(self):
        return self.terrain_map

# Пример использования
if __name__ == "__main__":
    map_width = 100
    map_height = 100
    generator = TerrainGenerator(map_width, map_height)
    generator.generate_terrain()
    terrain_map = generator.get_terrain_map()
    # Далее можно использовать полученную карту для создания игрового мира.
