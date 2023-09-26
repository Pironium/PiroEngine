import random

class PiroEngine:
    def generate_random_3d_model(self, complexity):
        """
        Генерирует случайную 3D модель с заданной сложностью.

        :param complexity: Сложность модели (целое число)
        :return: 3D модель в виде списка вершин и граней
        """
        if complexity < 1:
            raise ValueError("Сложность должна быть больше или равна 1")

        vertices = []
        edges = []

        # Генерация вершин
        for _ in range(complexity * 10):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            z = random.uniform(-1, 1)
            vertices.append((x, y, z))

        # Генерация граней
        for i in range(complexity * 5):
            vertex_indices = random.sample(range(len(vertices)), 3)
            edge = (vertex_indices[0], vertex_indices[1], vertex_indices[2])
            edges.append(edge)

        return vertices, edges

engine = PiroEngine()
model_complexity = 10
random_model = engine.generate_random_3d_model(model_complexity)
print("Сгенерирована случайная 3D модель:")
print("Вершины:", random_model[0])
print("Грани:", random_model[1])
