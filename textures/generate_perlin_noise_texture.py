import numpy as np
import noise
from PIL import Image

def generate_perlin_noise_texture(width, height, scale, octaves, persistence, lacunarity, seed):
    # Создаем пустой массив для текстуры
    texture = np.zeros((width, height, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            # Генерируем шум Перлина для каждого пикселя
            value = noise.pnoise2(x / scale,
                                  y / scale,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity,
                                  repeatx=1024,
                                  repeaty=1024,
                                  base=seed)
            # Масштабируем значение шума в диапазон от 0 до 255
            color = int((value + 1) * 127.5)
            # Задаем цвет пикселя
            texture[x, y, 0] = color
            texture[x, y, 1] = color
            texture[x, y, 2] = color

    # Создаем изображение из массива текстуры
    img = Image.fromarray(texture)
    img.save('perlin_noise_texture.png')

# Пример использования функции
generate_perlin_noise_texture(512, 512, 25, 6, 0.5, 2.0, 42)
