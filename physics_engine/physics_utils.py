class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

class PhysicsObject:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def apply_force(self, force):
        # Формула второго закона Ньютона: F = ma
        acceleration = Vector3D(force.x / self.mass, force.y / self.mass, force.z / self.mass)
        self.velocity.add(acceleration)

    def move(self, time_step):
        # Обновляем позицию на основе скорости и времени
        displacement = Vector3D(self.velocity.x * time_step, self.velocity.y * time_step, self.velocity.z * time_step)
        self.position.add(displacement)
