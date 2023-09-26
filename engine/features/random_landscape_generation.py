import random

class RandomLandscapeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.landscape = [[0 for _ in range(width)] for _ in range(height)]

    def generate_landscape(self):
        for x in range(self.width):
            for y in range(self.height):
                self.landscape[y][x] = random.randint(0, 1)  # 0 for land, 1 for water

    def export_landscape(self, filename):
        with open(filename, 'w') as file:
            for row in self.landscape:
                file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    landscape_generator = RandomLandscapeGenerator(100, 100)
    landscape_generator.generate_landscape()
    landscape_generator.export_landscape('random_landscape.txt')
