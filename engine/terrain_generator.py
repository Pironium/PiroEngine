import random
import numpy as np

class TerrainGenerator:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        self.seed = seed if seed is not None else random.randint(0, 9999)

    def generate_terrain(self):
        # Инициализация случайного генератора с сидом
        random.seed(self.seed)

        # Создаем случайный ландшафт
        terrain = np.zeros((self.width, self.height), dtype=float)
        for x in range(self.width):
            for y in range(self.height):
                terrain[x][y] = random.uniform(0, 1)

        return terrain

# Пример использования
if __name__ == "__main__":
    terrain_generator = TerrainGenerator(256, 256)
    terrain = terrain_generator.generate_terrain()
