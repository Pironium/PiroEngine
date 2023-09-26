# crypto_utils.py - Утилиты для криптографии в мультиплеере

import hashlib
import random

# Генерация случайного ключа для шифрования
def generate_encryption_key():
    key = ''.join(random.choice('0123456789abcdef') for _ in range(32))
    return key

# Шифрование данных с использованием ключа
def encrypt_data(data, encryption_key):
    encrypted_data = []
    for char in data:
        encrypted_char = ord(char) ^ ord(encryption_key)
        encrypted_data.append(encrypted_char)
    return encrypted_data

# Дешифрование данных с использованием ключа
def decrypt_data(encrypted_data, encryption_key):
    decrypted_data = []
    for encrypted_char in encrypted_data:
        decrypted_char = chr(encrypted_char ^ ord(encryption_key))
        decrypted_data.append(decrypted_char)
    return ''.join(decrypted_data)

# Хеширование данных для проверки целостности
def hash_data(data):
    hasher = hashlib.sha256()
    hasher.update(data.encode('utf-8'))
    return hasher.hexdigest()

# Проверка целостности данных
def verify_data_integrity(data, hash):
    return hash == hash_data(data)
