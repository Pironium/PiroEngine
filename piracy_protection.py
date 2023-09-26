# piracy_protection.py - PiroEngine Anti-Piracy and Security Features

import random
import hashlib

class PiracyProtection:
    def __init__(self):
        self.pirate_database = {}  # Database to store information about known pirates
        self.activation_key_generator = ActivationKeyGenerator()
    
    def register_pirate(self, username, hardware_id):
        """
        Register a pirate user by username and hardware ID.
        """
        if username not in self.pirate_database:
            self.pirate_database[username] = hardware_id
    
    def generate_activation_key(self, username, game_title):
        """
        Generate a unique activation key for a user to access a specific game.
        """
        if username not in self.pirate_database:
            raise Exception("User is not registered as a pirate.")
        
        # Combine username, game title, and a random salt to create a unique activation key
        salt = str(random.randint(1, 1000000))
        key = hashlib.sha256(f"{username}-{game_title}-{salt}".encode()).hexdigest()
        return key
    
    def verify_activation_key(self, activation_key, game_title):
        """
        Verify if an activation key is valid for a specific game.
        """
        for username, hardware_id in self.pirate_database.items():
            salt = str(random.randint(1, 1000000))
            expected_key = hashlib.sha256(f"{username}-{game_title}-{salt}".encode()).hexdigest()
            if activation_key == expected_key:
                return True
        return False

class ActivationKeyGenerator:
    def __init__(self):
        self.key_length = 32  # Length of the activation key
    
    def generate_key(self):
        """
        Generate a random activation key.
        """
        return ''.join(random.choice('0123456789ABCDEF') for _ in range(self.key_length))

# Usage example:
if __name__ == "__main__":
    piracy_protection = PiracyProtection()
    piracy_protection.register_pirate("pirate123", "HWID-12345")
    activation_key = piracy_protection.generate_activation_key("pirate123", "AwesomeGame")
    
    # Verify the activation key
    if piracy_protection.verify_activation_key(activation_key, "AwesomeGame"):
        print("Activation key is valid.")
    else:
        print("Invalid activation key.")
