import random

class WeatherGenerator:
    def __init__(self):
        self.weather_types = ["clear", "cloudy", "rainy", "snowy", "foggy"]
    
    def generate_weather(self):
        # Генерируем случайный тип погоды
        weather_type = random.choice(self.weather_types)
        
        if weather_type == "clear":
            print("The weather is clear and sunny.")
            # Дополнительные настройки для ясной погоды
        elif weather_type == "cloudy":
            print("The sky is cloudy.")
            # Дополнительные настройки для облачной погоды
        elif weather_type == "rainy":
            print("It's raining.")
            # Дополнительные настройки для дождливой погоды
        elif weather_type == "snowy":
            print("Snow is falling.")
            # Дополнительные настройки для снежной погоды
        elif weather_type == "foggy":
            print("The area is covered in thick fog.")
            # Дополнительные настройки для туманной погоды

# Пример использования
if __name__ == "__main__":
    weather_generator = WeatherGenerator()
    weather_generator.generate_weather()
