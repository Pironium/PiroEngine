class AdvancedPhysicsEngine:
    def __init__(self):
        self.gravity = 9.81  # Standard gravity constant
        self.objects = []    # List of physical objects in the scene

    def add_object(self, obj):
        """Add a physical object to the simulation."""
        self.objects.append(obj)

    def apply_gravity(self):
        """Apply gravitational force to all objects."""
        for obj in self.objects:
            obj.apply_force([0, -self.gravity * obj.mass])

    def update(self, delta_time):
        """Update the physics simulation for a given time step."""
        for obj in self.objects:
            obj.update(delta_time)

class PhysicalObject:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.forces = [0, 0]  # List of forces acting on the object

    def apply_force(self, force):
        """Apply an external force to the object."""
        self.forces[0] += force[0]
        self.forces[1] += force[1]

    def update(self, delta_time):
        """Update the object's position and velocity based on applied forces."""
        acceleration = [self.forces[0] / self.mass, self.forces[1] / self.mass]
        self.velocity[0] += acceleration[0] * delta_time
        self.velocity[1] += acceleration[1] * delta_time
        self.position[0] += self.velocity[0] * delta_time
        self.position[1] += self.velocity[1] * delta_time
        self.forces = [0, 0]  # Reset forces for the next update
