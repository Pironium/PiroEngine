class EnhancedPhysicsFunctions:
    def __init__(self, physics_config):
        self.config = physics_config

    def apply_gravity(self, object, time_step):
        # Calculate gravitational force and apply it to the object
        gravitational_force = self.config.gravity * object.mass
        object.velocity.y -= gravitational_force * time_step

    def simulate_friction(self, object, time_step):
        # Simulate friction based on the object's material
        friction_coefficient = object.material.friction_coefficient
        object.velocity.x *= 1 - friction_coefficient * time_step
        object.velocity.z *= 1 - friction_coefficient * time_step

    def apply_air_resistance(self, object, time_step):
        # Apply air resistance based on object's shape and speed
        drag_coefficient = object.shape.drag_coefficient
        velocity_magnitude = object.velocity.magnitude()
        resistance_force = 0.5 * self.config.air_density * velocity_magnitude ** 2 * drag_coefficient
        resistance_direction = object.velocity.normalized()
        resistance_force_vector = resistance_direction * resistance_force
        object.apply_force(resistance_force_vector)
