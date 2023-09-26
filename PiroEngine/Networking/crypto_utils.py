# Crypto utilities for secure multiplayer communication

import hashlib
import hmac
import base64
import os

class CryptoUtils:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def generate_salt(self, size=16):
        return os.urandom(size)

    def hash_password(self, password, salt=None):
        if salt is None:
            salt = self.generate_salt()
        password_bytes = password.encode('utf-8')
        salted_password = salt + password_bytes
        hashed_password = hashlib.sha256(salted_password).digest()
        return salt, hashed_password

    def verify_password(self, password, salt, hashed_password):
        _, expected_password = self.hash_password(password, salt)
        return hmac.compare_digest(expected_password, hashed_password)

    def encrypt_data(self, data):
        cipher = AES.new(self.secret_key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext + tag).decode('utf-8')

    def decrypt_data(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data.encode('utf-8'))
        nonce = encrypted_data[:16]
        ciphertext_tag = encrypted_data[16:]
        cipher = AES.new(self.secret_key, AES.MODE_EAX, nonce=nonce)
        data = cipher.decrypt(ciphertext_tag[:-16])
        return data.decode('utf-8')
