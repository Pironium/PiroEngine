class Piro3DPhysicsEngine:
    def __init__(self):
        self.objects = []  # Список объектов, участвующих в физическом моделировании
        self.gravity = (0, -9.81, 0)  # Земное ускорение

    def add_object(self, obj):
        # Добавляет объект в список участвующих в физическом моделировании
        self.objects.append(obj)

    def remove_object(self, obj):
        # Удаляет объект из списка участвующих в физическом моделировании
        if obj in self.objects:
            self.objects.remove(obj)

    def apply_gravity(self):
        # Применяет гравитацию ко всем объектам
        for obj in self.objects:
            obj.apply_force(self.gravity * obj.mass)

    def simulate(self, delta_time):
        # Выполняет симуляцию физики на протяжении заданного времени
        self.apply_gravity()
        for obj in self.objects:
            obj.update_position(delta_time)

class Piro3DPhysicsObject:
    def __init__(self, mass):
        self.mass = mass  # Масса объекта
        self.position = (0, 0, 0)  # Текущая позиция объекта
        self.velocity = (0, 0, 0)  # Текущая скорость объекта

    def apply_force(self, force):
        # Применяет силу к объекту
        # F = m * a, где F - сила, m - масса, a - ускорение
        acceleration = force / self.mass
        self.velocity += acceleration

    def update_position(self, delta_time):
        # Обновляет позицию объекта на основе его скорости
        self.position += self.velocity * delta_time
