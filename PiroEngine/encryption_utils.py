# PiroEngine Encryption Utilities
# This module provides functions for encryption and decryption of game data.

import hashlib
import base64
import cryptography
from cryptography.fernet import Fernet

def generate_encryption_key():
    """
    Generate a secure encryption key for data protection.
    Returns:
        bytes: A randomly generated encryption key.
    """
    return Fernet.generate_key()

def encrypt_data(data, encryption_key):
    """
    Encrypt the game data using Fernet symmetric encryption.
    Args:
        data (bytes): The data to be encrypted.
        encryption_key (bytes): The encryption key.
    Returns:
        bytes: Encrypted data.
    """
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data

def decrypt_data(encrypted_data, encryption_key):
    """
    Decrypt the encrypted game data.
    Args:
        encrypted_data (bytes): The encrypted data to be decrypted.
        encryption_key (bytes): The encryption key.
    Returns:
        bytes: Decrypted data.
    """
    cipher_suite = Fernet(encryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

def hash_data(data):
    """
    Generate a cryptographic hash of the game data.
    Args:
        data (bytes): The data to be hashed.
    Returns:
        str: The hexadecimal representation of the hash.
    """
    sha256_hash = hashlib.sha256(data)
    return sha256_hash.hexdigest()
