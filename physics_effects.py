# Директория: engine/modules/
# Название файла: physics_effects.py

import math

class PhysicsEffects:
    def __init__(self):
        self.gravity = 9.81  # Ускорение свободного падения (м/с^2)
        self.air_density = 1.225  # Плотность воздуха (кг/м^3)

    def apply_gravity(self, object, time_step):
        """Применить гравитацию к объекту."""
        if object.mass > 0:
            force = object.mass * self.gravity
            object.apply_force((0, -force, 0))

    def apply_drag(self, object, velocity):
        """Применить сопротивление воздуха к объекту."""
        if object.cross_sectional_area > 0:
            drag_coefficient = 0.47  # Коэффициент сопротивления для сферы
            drag_force = 0.5 * self.air_density * velocity**2 * drag_coefficient * object.cross_sectional_area
            object.apply_force((-drag_force, 0, 0))

    def apply_rotation(self, object, angular_velocity):
        """Применить вращение к объекту."""
        if object.moment_of_inertia > 0:
            torque = object.moment_of_inertia * angular_velocity
            object.apply_torque((0, 0, torque))

    def simulate_physics(self, objects, time_step):
        """Симулировать физические эффекты на объектах."""
        for obj in objects:
            self.apply_gravity(obj, time_step)
            velocity = math.sqrt(obj.velocity[0]**2 + obj.velocity[1]**2 + obj.velocity[2]**2)
            self.apply_drag(obj, velocity)
            angular_velocity = math.sqrt(obj.angular_velocity[0]**2 + obj.angular_velocity[1]**2 + obj.angular_velocity[2]**2)
            self.apply_rotation(obj, angular_velocity)
