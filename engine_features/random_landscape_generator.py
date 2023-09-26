import random

class RandomLandscapeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.landscape = [[0 for _ in range(width)] for _ in range(height)]

    def generate_landscape(self):
        for i in range(self.height):
            for j in range(self.width):
                self.landscape[i][j] = random.randint(0, 1)  # Randomly generate 0 or 1 for terrain type

    def get_landscape(self):
        return self.landscape

if __name__ == "__main__":
    width = 100
    height = 100
    landscape_generator = RandomLandscapeGenerator(width, height)
    landscape_generator.generate_landscape()
    landscape = landscape_generator.get_landscape()
    for row in landscape:
        print(" ".join(str(cell) for cell in row))
