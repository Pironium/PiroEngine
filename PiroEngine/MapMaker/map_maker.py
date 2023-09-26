import random
import math

class MapMaker:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_data = [[0 for _ in range(width)] for _ in range(height)]

    def generate_random_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self.map_data[y][x] = random.randint(0, 1)

    def add_perlin_noise(self, scale, persistence, octaves):
        for y in range(self.height):
            for x in range(self.width):
                noise_value = self.perlin_noise(x * scale, y * scale, persistence, octaves)
                self.map_data[y][x] = int(noise_value * 255)

    def perlin_noise(self, x, y, persistence, octaves):
        total = 0
        frequency = 1
        amplitude = 1
        max_value = 0

        for _ in range(octaves):
            total += self.smooth_noise(x * frequency, y * frequency) * amplitude
            max_value += amplitude
            amplitude *= persistence
            frequency *= 2

        return total / max_value

    def smooth_noise(self, x, y):
        corners = (self.noise(x - 1, y - 1) + self.noise(x + 1, y - 1) +
                   self.noise(x - 1, y + 1) + self.noise(x + 1, y + 1)) / 16
        sides = (self.noise(x - 1, y) + self.noise(x + 1, y) +
                 self.noise(x, y - 1) + self.noise(x, y + 1)) / 8
        center = self.noise(x, y) / 4
        return corners + sides + center

    def noise(self, x, y):
        seed = random.seed(x * 49632 + y * 325176 + 101101)
        return math.sin(seed)

    def save_map_to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.map_data:
                file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    map_maker = MapMaker(512, 512)
    map_maker.generate_random_map()
    map_maker.add_perlin_noise(0.1, 0.5, 5)
    map_maker.save_map_to_file('generated_map.txt')
