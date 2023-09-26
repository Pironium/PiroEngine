class PhysicsEngine:
    def __init__(self):
        self.gravity = Vector3(0, -9.81, 0)
        self.objects = []

    def apply_gravity(self):
        for obj in self.objects:
            if obj.has_gravity:
                obj.apply_force(self.gravity * obj.mass)
