# PiroEngine Anti-Piracy Module

import hashlib
import random
import string

class AntiPiracy:
    def __init__(self):
        self.activation_key = self.generate_activation_key()
        self.piracy_attempts = 0

    def generate_activation_key(self):
        salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        activation_key = hashlib.sha256(salt.encode()).hexdigest()
        return activation_key

    def verify_activation_key(self, user_key):
        if self.activation_key == user_key:
            return True
        else:
            self.piracy_attempts += 1
            return False

    def is_piracy_attempt_limit_exceeded(self):
        return self.piracy_attempts >= 3

class PiroEngine:
    def __init__(self):
        self.anti_piracy_module = AntiPiracy()

    def load_game(self, activation_key):
        if self.anti_piracy_module.verify_activation_key(activation_key):
            print("Game loaded successfully!")
        else:
            if self.anti_piracy_module.is_piracy_attempt_limit_exceeded():
                print("Piracy attempt limit exceeded. Please contact support.")
            else:
                print("Invalid activation key. Please try again.")

if __name__ == "__main__":
    engine = PiroEngine()
    activation_key = input("Enter your activation key: ")
    engine.load_game(activation_key)
