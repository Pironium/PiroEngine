import math
import random

class ThreeDEffects:
    def __init__(self):
        self.effects = []

    def create_explosion(self, x, y, z, size):
        # Генерируем случайное количество частиц
        num_particles = random.randint(100, 500)

        for _ in range(num_particles):
            # Генерируем случайные координаты внутри сферы
            phi = random.uniform(0, 2 * math.pi)
            theta = random.uniform(0, math.pi)
            r = random.uniform(0, size)

            # Преобразуем сферические координаты в декартовы
            x_particle = r * math.sin(theta) * math.cos(phi)
            y_particle = r * math.sin(theta) * math.sin(phi)
            z_particle = r * math.cos(theta)

            self.effects.append((x + x_particle, y + y_particle, z + z_particle))

    def render_effects(self):
        for effect in self.effects:
            # Отрисовываем каждую частицу в 3D пространстве
            x, y, z = effect
            print(f"Rendered particle at ({x}, {y}, {z})")

if __name__ == "__main__":
    engine = ThreeDEffects()
    engine.create_explosion(0, 0, 0, 10)
    engine.render_effects()
