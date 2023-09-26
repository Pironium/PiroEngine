# PiroEngine Texture Mapping Module

import random

class TextureMapper:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_texture_coords(self, vertices):
        texture_coords = []
        for vertex in vertices:
            x = random.uniform(0, self.width)
            y = random.uniform(0, self.height)
            texture_coords.append((x, y))
        return texture_coords

# Usage example:
if __name__ == "__main__":
    engine = TextureMapper(1024, 1024)
    polygon_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    texture_coords = engine.generate_texture_coords(polygon_vertices)
    print("Generated Texture Coordinates:")
    for i, coord in enumerate(texture_coords):
        print(f"Vertex {i + 1}: ({coord[0]}, {coord[1]})")
