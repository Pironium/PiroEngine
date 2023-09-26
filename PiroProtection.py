# PiroProtection.py - Защита от пиратов и взломов для игр

import hashlib
import random

class PiroProtection:
    def __init__(self):
        self.activation_key = self.generate_activation_key()

    def generate_activation_key(self):
        # Генерируем случайный активационный ключ
        random.seed()
        key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=32))
        return key

    def check_activation_key(self, user_key):
        # Проверяем, является ли переданный ключ действительным
        return hashlib.sha256(user_key.encode()).hexdigest() == hashlib.sha256(self.activation_key.encode()).hexdigest()

    def encrypt_game_data(self, data):
        # Шифруем игровые данные перед сохранением
        encrypted_data = ""
        for char in data:
            encrypted_data += chr(ord(char) + 1)  # Простой шифр, сдвигаем каждый символ на 1
        return encrypted_data

    def decrypt_game_data(self, data):
        # Расшифровываем игровые данные при загрузке
        decrypted_data = ""
        for char in data:
            decrypted_data += chr(ord(char) - 1)  # Расшифровываем обратно
        return decrypted_data

# Пример использования:

if __name__ == "__main__":
    protection = PiroProtection()
    user_input = input("Введите активационный ключ: ")
    if protection.check_activation_key(user_input):
        print("Активация успешна!")
    else:
        print("Неверный активационный ключ!")

    game_data = "This is sensitive game data."
    encrypted_data = protection.encrypt_game_data(game_data)
    print("Зашифрованные игровые данные:", encrypted_data)

    decrypted_data = protection.decrypt_game_data(encrypted_data)
    print("Расшифрованные игровые данные:", decrypted_data)
