class DynamicLight:
    def __init__(self, position, color, intensity):
        self.position = position  # 3D координаты светового источника
        self.color = color  # Цвет света (RGB)
        self.intensity = intensity  # Интенсивность света

    def set_position(self, new_position):
        self.position = new_position

    def set_color(self, new_color):
        self.color = new_color

    def set_intensity(self, new_intensity):
        self.intensity = new_intensity


class DynamicLightManager:
    def __init__(self):
        self.lights = []

    def add_light(self, light):
        self.lights.append(light)

    def remove_light(self, light):
        if light in self.lights:
            self.lights.remove(light)

    def update_lights(self):
        # Логика обновления световых источников в каждом кадре
        pass

# Пример использования:

# Создаем менеджер световых источников
light_manager = DynamicLightManager()

# Создаем и добавляем световой источник
light1 = DynamicLight((1.0, 2.0, 3.0), (1.0, 1.0, 1.0), 10.0)
light_manager.add_light(light1)

# Обновляем световые источники в каждом кадре
light_manager.update_lights()
