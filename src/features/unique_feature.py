# src/features/unique_feature.py

class SuperPhysics:
    def __init__(self, game_object):
        self.game_object = game_object
        self.gravity = 9.81
        self.velocity = [0, 0, 0]

    def apply_gravity(self):
        # Рассчитываем воздействие гравитации на объект
        self.velocity[1] -= self.gravity * self.game_object.mass

    def apply_force(self, force):
        # Применяем силу к объекту
        for i in range(3):
            self.velocity[i] += force[i] / self.game_object.mass

    def update_position(self):
        # Обновляем позицию объекта на основе скорости
        for i in range(3):
            self.game_object.position[i] += self.velocity[i]
