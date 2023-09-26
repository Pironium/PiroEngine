# water_effects.py - Модуль для создания водных эффектов в играх

class WaterEffect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.water_surface = [[0.0] * width for _ in range(height)]
        self.current_time = 0

    def create_water_surface(self):
        # Создаем водную поверхность, используя уравнение волн
        for y in range(self.height):
            for x in range(self.width):
                self.water_surface[y][x] = (
                    math.sin(x / 10.0 + self.current_time) +
                    math.cos(y / 5.0 + self.current_time)
                )
        
        self.current_time += 0.1

    def apply_water_effect(self, image):
        # Применяем водный эффект к изображению
        for y in range(self.height):
            for x in range(self.width):
                image[y][x] += self.water_surface[y][x] * 10
                
        # Нормализуем значения пикселей
        for y in range(self.height):
            for x in range(self.width):
                image[y][x] = min(max(image[y][x], 0), 255)

# Пример использования:
if __name__ == "__main__":
    import math
    width, height = 800, 600
    game_image = [[0] * width for _ in range(height)]
    
    water_effect = WaterEffect(width, height)
    
    for frame in range(100):
        water_effect.create_water_surface()
        water_effect.apply_water_effect(game_image)
        # Здесь вы можете отобразить game_image на экране игры
