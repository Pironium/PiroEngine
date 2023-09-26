# world_generation.py

import random

class WorldGenerator:
    def __init__(self, seed):
        self.seed = seed
        self.random = random.Random(seed)
    
    def generate_world(self, size):
        world = [[0 for _ in range(size)] for _ in range(size)]
        
        # Генерируем случайные элементы в мире
        for i in range(size):
            for j in range(size):
                world[i][j] = self.random.randint(0, 1)
        
        return world

# Пример использования
if __name__ == "__main__":
    seed = 42
    generator = WorldGenerator(seed)
    world_size = 10
    generated_world = generator.generate_world(world_size)
    print(generated_world)
