import random

class LandscapeGenerator:
    def __init__(self, width, height, complexity, roughness):
        self.width = width
        self.height = height
        self.complexity = complexity
        self.roughness = roughness
        self.map = [[0.0] * width for _ in range(height)]

    def generate(self):
        self._divide(0, 0, self.width - 1, self.height - 1, self.complexity)
        return self.map

    def _divide(self, x1, y1, x2, y2, depth):
        if depth <= 0:
            return

        mid_x = (x1 + x2) // 2
        mid_y = (y1 + y2) // 2

        displacement = random.uniform(-self.roughness, self.roughness)

        self.map[mid_y][mid_x] = (
            (self.map[y1][x1] + self.map[y1][x2] + self.map[y2][x1] + self.map[y2][x2]) / 4.0 + displacement
        )

        self.map[y1][mid_x] = ((self.map[y1][x1] + self.map[y1][x2]) / 2.0)
        self.map[y2][mid_x] = ((self.map[y2][x1] + self.map[y2][x2]) / 2.0)
        self.map[mid_y][x1] = ((self.map[y1][x1] + self.map[y2][x1]) / 2.0)
        self.map[mid_y][x2] = ((self.map[y1][x2] + self.map[y2][x2]) / 2.0)

        self._divide(x1, y1, mid_x, mid_y, depth - 1)
        self._divide(mid_x, y1, x2, mid_y, depth - 1)
        self._divide(x1, mid_y, mid_x, y2, depth - 1)
        self._divide(mid_x, mid_y, x2, y2, depth - 1)

if __name__ == "__main__":
    width = 128
    height = 128
    complexity = 8
    roughness = 1.0

    generator = LandscapeGenerator(width, height, complexity, roughness)
    landscape = generator.generate()
    print(landscape)
