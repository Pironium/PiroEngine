import random

class TerrainGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.terrain_map = self.generate_terrain()

    def generate_terrain(self):
        terrain_map = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Генерируем случайный ландшафт
        for y in range(self.height):
            for x in range(self.width):
                terrain_map[y][x] = random.randint(0, 1)

        return terrain_map

    def get_terrain_map(self):
        return self.terrain_map

    def set_terrain(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.terrain_map[y][x] = value

    def get_terrain_at(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.terrain_map[y][x]
        else:
            return None

    def smooth_terrain(self, iterations):
        for _ in range(iterations):
            new_terrain = [[0 for _ in range(self.width)] for _ in range(self.height)]
            for y in range(self.height):
                for x in range(self.width):
                    neighbors = self.count_neighbors(x, y)
                    if neighbors >= 5:
                        new_terrain[y][x] = 1
                    else:
                        new_terrain[y][x] = 0
            self.terrain_map = new_terrain

    def count_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.width and 0 <= y + j < self.height:
                    count += self.terrain_map[y + j][x + i]
        return count
