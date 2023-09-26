# PiroEngine Model Maker Module
# Allows developers to create 3D models easily

import math

class ModelMaker:
    def __init__(self):
        self.models = []

    def create_box(self, width, height, depth):
        """
        Creates a 3D box model with the specified dimensions.
        
        :param width: Width of the box.
        :param height: Height of the box.
        :param depth: Depth of the box.
        :return: A 3D model representing a box.
        """
        vertices = [
            (-width / 2, -height / 2, -depth / 2),
            (-width / 2, height / 2, -depth / 2),
            (width / 2, height / 2, -depth / 2),
            (width / 2, -height / 2, -depth / 2),
            (-width / 2, -height / 2, depth / 2),
            (-width / 2, height / 2, depth / 2),
            (width / 2, height / 2, depth / 2),
            (width / 2, -height / 2, depth / 2),
        ]

        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        return {"vertices": vertices, "edges": edges}

    def create_sphere(self, radius, segments):
        """
        Creates a 3D sphere model with the specified radius and number of segments.
        
        :param radius: Radius of the sphere.
        :param segments: Number of horizontal segments.
        :return: A 3D model representing a sphere.
        """
        vertices = []
        edges = []

        for i in range(segments):
            phi = i * math.pi / segments
            for j in range(segments):
                theta = j * 2 * math.pi / segments
                x = radius * math.sin(phi) * math.cos(theta)
                y = radius * math.sin(phi) * math.sin(theta)
                z = radius * math.cos(phi)
                vertices.append((x, y, z))

                if i < segments - 1:
                    if j < segments - 1:
                        edges.append((i * segments + j, i * segments + j + 1))
                        edges.append((i * segments + j, (i + 1) * segments + j))
                    else:
                        edges.append((i * segments + j, i * segments))
                        edges.append((i * segments + j, (i + 1) * segments))
                else:
                    edges.append((i * segments + j, j))

        return {"vertices": vertices, "edges": edges}
