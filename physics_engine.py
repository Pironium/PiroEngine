# physics_engine.py

class PhysicsEngine:
    def __init__(self):
        self.gravity = 9.81
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def apply_gravity(self):
        for obj in self.objects:
            if obj.mass:
                obj.apply_force((0, obj.mass * self.gravity))

class GameObject:
    def __init__(self, mass=0, position=(0, 0)):
        self.mass = mass
        self.position = position
        self.velocity = (0, 0)

    def apply_force(self, force):
        acceleration = (force[0] / self.mass, force[1] / self.mass)
        self.velocity = (self.velocity[0] + acceleration[0], self.velocity[1] + acceleration[1])

    def update(self, time_step):
        new_x = self.position[0] + self.velocity[0] * time_step
        new_y = self.position[1] + self.velocity[1] * time_step
        self.position = (new_x, new_y)

    def __str__(self):
        return f"Object with mass {self.mass} at position {self.position}"

if __name__ == "__main__":
    engine = PhysicsEngine()
    obj1 = GameObject(mass=5, position=(0, 0))
    obj2 = GameObject(mass=10, position=(3, 0))

    engine.add_object(obj1)
    engine.add_object(obj2)

    for _ in range(10):
        engine.apply_gravity()
        obj1.update(0.1)
        obj2.update(0.1)
        print(obj1)
        print(obj2)
