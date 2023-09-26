import numpy as np

class WaterSurfaceGenerator:
    def __init__(self, width, height, wave_speed, wave_amplitude):
        self.width = width
        self.height = height
        self.wave_speed = wave_speed
        self.wave_amplitude = wave_amplitude
        self.time = 0
        self.surface = np.zeros((width, height))

    def update(self, delta_time):
        self.time += delta_time
        x = np.arange(0, self.width)
        y = np.arange(0, self.height)
        x, y = np.meshgrid(x, y)
        self.surface = np.sin(x * 0.1 + self.time * self.wave_speed) * \
                       np.sin(y * 0.1 + self.time * self.wave_speed) * self.wave_amplitude

    def get_surface(self):
        return self.surface

    def reset(self):
        self.time = 0
        self.surface = np.zeros((self.width, self.height))
