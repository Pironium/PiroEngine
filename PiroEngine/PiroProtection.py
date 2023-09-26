# PiroProtection.py - PiroEngine Anti-Piracy and Anti-Hacking Module

import hashlib
import os
import random

class PiroProtection:
    def __init__(self, game_name):
        self.game_name = game_name
        self.encryption_key = self.generate_encryption_key()
        self.activation_code = self.generate_activation_code()

    def generate_encryption_key(self):
        # Generate a random encryption key for data protection
        key = ""
        for _ in range(32):
            key += chr(random.randint(32, 126))  # Generate printable ASCII characters
        return key

    def generate_activation_code(self):
        # Generate a unique activation code based on game name and encryption key
        activation_data = self.game_name + self.encryption_key
        activation_code = hashlib.sha256(activation_data.encode()).hexdigest()
        return activation_code

    def activate_game(self, user_activation_code):
        if user_activation_code == self.activation_code:
            print(f"Activation successful. Welcome to {self.game_name}!")
        else:
            print("Invalid activation code. Access denied.")

    def protect_game_data(self, data):
        # Encrypt game data using the encryption key
        encrypted_data = ""
        for char in data:
            encrypted_char = chr(ord(char) + ord(self.encryption_key) % 256)
            encrypted_data += encrypted_char
        return encrypted_data

    def decrypt_game_data(self, encrypted_data):
        # Decrypt game data using the encryption key
        decrypted_data = ""
        for char in encrypted_data:
            decrypted_char = chr(ord(char) - ord(self.encryption_key) % 256)
            decrypted_data += decrypted_char
        return decrypted_data

if __name__ == "__main__":
    game_name = "PiroGame"
    piro_protection = PiroProtection(game_name)
    user_input = input("Enter your activation code: ")
    piro_protection.activate_game(user_input)
