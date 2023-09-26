# PiroEngine Encryption Utilities
# Provides functions for secure data encryption in multiplayer communication

import cryptography
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key):
        self.key = key

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_message(self, message):
        f = Fernet(self.key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        f = Fernet(self.key)
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message

# Example Usage:
# key = EncryptionManager.generate_key()
# encryption_manager = EncryptionManager(key)
# encrypted_msg = encryption_manager.encrypt_message("Hello, World!")
# decrypted_msg = encryption_manager.decrypt_message(encrypted_msg)
# print(decrypted_msg)  # Output should be "Hello, World!"
