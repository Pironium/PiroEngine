# PiroEngine Piracy Protection Module

import hashlib
import random

class PiracyProtection:
    def __init__(self):
        self.activation_code = None

    def generate_activation_code(self, user_id):
        """
        Generates a unique activation code for a user based on their user ID.
        """
        salt = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))
        user_id_str = str(user_id)
        activation_code = hashlib.sha256((user_id_str + salt).encode()).hexdigest()
        self.activation_code = activation_code

    def verify_activation_code(self, user_id, provided_code):
        """
        Verifies if the provided activation code matches the expected code for the user.
        """
        salt = ''.join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))
        user_id_str = str(user_id)
        expected_code = hashlib.sha256((user_id_str + salt).encode()).hexdigest()
        
        return provided_code == expected_code

if __name__ == "__main__":
    piracy_protection = PiracyProtection()
    user_id = 12345
    piracy_protection.generate_activation_code(user_id)
    provided_code = input("Enter your activation code: ")
    
    if piracy_protection.verify_activation_code(user_id, provided_code):
        print("Activation successful. Enjoy your PiroEngine experience!")
    else:
        print("Invalid activation code. Please purchase a valid license.")
