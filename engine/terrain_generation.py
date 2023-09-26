# engine/terrain_generation.py

import random

class AdvancedTerrainGeneration:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain_map = [[0 for _ in range(width)] for _ in range(height)]

    def generate_terrain(self):
        # Здесь будем генерировать сложный ландшафт
        for x in range(self.width):
            for y in range(self.height):
                # Пример случайной генерации высоты ландшафта
                self.terrain_map[y][x] = random.randint(0, 100)

    def smooth_terrain(self, iterations=1):
        # Здесь будем сглаживать ландшафт для более натурального вида
        for _ in range(iterations):
            for x in range(1, self.width - 1):
                for y in range(1, self.height - 1):
                    # Сглаживаем высоту на основе соседних точек
                    avg_height = (self.terrain_map[y - 1][x - 1] + self.terrain_map[y - 1][x] +
                                  self.terrain_map[y - 1][x + 1] + self.terrain_map[y][x - 1] +
                                  self.terrain_map[y][x] + self.terrain_map[y][x + 1] +
                                  self.terrain_map[y + 1][x - 1] + self.terrain_map[y + 1][x] +
                                  self.terrain_map[y + 1][x + 1]) // 9
                    self.terrain_map[y][x] = avg_height

    def export_terrain_map(self, filename):
        # Записываем карту ландшафта в файл для дальнейшего использования
        with open(filename, 'w') as file:
            for row in self.terrain_map:
                file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    terrain_generator = AdvancedTerrainGeneration(100, 100)
    terrain_generator.generate_terrain()
    terrain_generator.smooth_terrain(5)
    terrain_generator.export_terrain_map("terrain_map.txt")
