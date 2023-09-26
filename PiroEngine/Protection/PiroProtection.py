# PiroProtection - Advanced Anti-Piracy and Anti-Hacking Module for PiroEngine
# Copyright (c) 2023 Pironium Inc. All rights reserved.

import hashlib
import random
import os

class PiroProtection:
    def __init__(self):
        self.activation_key = self.generate_activation_key()
        self.hardcoded_salt = self.generate_hardcoded_salt()

    def generate_activation_key(self):
        # Generate a unique activation key for each installation
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()

    def generate_hardcoded_salt(self):
        # Generate a random salt for hardcoding security measures
        return os.urandom(16)

    def encrypt_data(self, data):
        # Implement a custom encryption algorithm for sensitive data
        encrypted_data = ""
        for char in data:
            encrypted_char = chr(ord(char) + 5)  # Shift each character by 5 positions
            encrypted_data += encrypted_char
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Implement decryption using the reverse process
        decrypted_data = ""
        for char in encrypted_data:
            decrypted_char = chr(ord(char) - 5)  # Reverse the shift
            decrypted_data += decrypted_char
        return decrypted_data

    def validate_activation_key(self, user_key):
        # Validate user's activation key against the generated one
        return user_key == self.activation_key

    def hardcode_security(self):
        # Hardcode security measures using the generated salt
        hardcoded_security = self.hardcoded_salt + b"custom_security_string"
        return hashlib.sha256(hardcoded_security).hexdigest()

if __name__ == "__main__":
    protection_module = PiroProtection()
    print(f"Activation Key: {protection_module.activation_key}")
    print(f"Hardcoded Salt: {protection_module.hardcoded_salt}")
    user_key = input("Enter activation key for validation: ")
    if protection_module.validate_activation_key(user_key):
        print("Activation key is valid.")
        print(f"Hardcoded Security Hash: {protection_module.hardcode_security()}")
    else:
        print("Invalid activation key. Access denied.")
