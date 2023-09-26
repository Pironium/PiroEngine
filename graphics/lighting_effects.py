# PiroEngine Lighting Effects Module

class LightingEffect:
    def __init__(self, name):
        self.name = name
        self.intensity = 1.0
        self.color = (1.0, 1.0, 1.0)  # Default to white light

    def set_intensity(self, intensity):
        self.intensity = intensity

    def set_color(self, color):
        self.color = color

    def apply(self, scene):
        # Apply the lighting effect to the scene
        for object in scene.objects:
            object.apply_lighting(self.intensity, self.color)

class DynamicLightingEffect(LightingEffect):
    def __init__(self, name):
        super().__init__(name)
        self.radius = 5.0

    def set_radius(self, radius):
        self.radius = radius

    def apply(self, scene):
        # Apply dynamic lighting effect to the scene
        for object in scene.objects:
            object.apply_dynamic_lighting(self.intensity, self.color, self.radius)

# More advanced lighting effects can be added here
