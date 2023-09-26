# PiroProtection - Anti-piracy and anti-hacking module for PiroEngine
import hashlib
import random
import string

class PiroProtection:
    def __init__(self):
        self.license_key = self.generate_license_key()
        self.activation_status = False

    def generate_license_key(self):
        # Generate a unique license key
        key_length = 32
        characters = string.ascii_letters + string.digits
        license_key = ''.join(random.choice(characters) for _ in range(key_length))
        return hashlib.sha256(license_key.encode()).hexdigest()

    def activate(self, input_key):
        # Activate PiroEngine with a valid license key
        if hashlib.sha256(input_key.encode()).hexdigest() == self.license_key:
            self.activation_status = True
            print("PiroEngine activated successfully.")
        else:
            print("Invalid license key. Activation failed.")

    def is_activated(self):
        # Check if PiroEngine is activated
        return self.activation_status

    def protect_game_code(self, game_code):
        # Implement advanced code obfuscation and encryption techniques here
        protected_code = game_code  # Placeholder for code protection logic
        return protected_code
