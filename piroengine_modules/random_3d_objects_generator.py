import random

class Random3DObjectsGenerator:
    def __init__(self):
        self.objects = []

    def generate_random_cube(self, size):
        cube = {
            'type': 'cube',
            'size': size,
            'position': (random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)),
            'rotation': (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360)),
            'color': (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
        }
        self.objects.append(cube)

    def generate_random_sphere(self, radius):
        sphere = {
            'type': 'sphere',
            'radius': radius,
            'position': (random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)),
            'color': (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
        }
        self.objects.append(sphere)

    def generate_random_cylinder(self, radius, height):
        cylinder = {
            'type': 'cylinder',
            'radius': radius,
            'height': height,
            'position': (random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)),
            'rotation': (random.uniform(0, 360), random.uniform(0, 360), random.uniform(0, 360)),
            'color': (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
        }
        self.objects.append(cylinder)

    def get_generated_objects(self):
        return self.objects
