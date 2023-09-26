import random

class TerrainGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain = [[0 for _ in range(width)] for _ in range(height)]

    def generate_terrain(self):
        # Генерация случайного ландшафта
        for y in range(self.height):
            for x in range(self.width):
                self.terrain[y][x] = random.randint(0, 100)

    def smooth_terrain(self):
        # Сглаживание ландшафта
        for _ in range(5):
            for y in range(1, self.height - 1):
                for x in range(1, self.width - 1):
                    avg = (
                        self.terrain[y - 1][x - 1] + self.terrain[y - 1][x] +
                        self.terrain[y - 1][x + 1] + self.terrain[y][x - 1] +
                        self.terrain[y][x + 1] + self.terrain[y + 1][x - 1] +
                        self.terrain[y + 1][x] + self.terrain[y + 1][x + 1]
                    ) // 8
                    self.terrain[y][x] = avg

    def export_terrain(self, filename):
        # Экспорт ландшафта в файл
        with open(filename, 'w') as file:
            for y in range(self.height):
                for x in range(self.width):
                    file.write(str(self.terrain[y][x]) + ' ')
                file.write('\n')

if __name__ == '__main__':
    terrain_gen = TerrainGenerator(100, 100)
    terrain_gen.generate_terrain()
    terrain_gen.smooth_terrain()
    terrain_gen.export_terrain('terrain_map.txt')
