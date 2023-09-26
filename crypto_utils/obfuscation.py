# Pironium Cryptographic Obfuscation Module
# Copyright (c) 2023 Pironium Inc. All rights reserved.

import hashlib
import base64

class Obfuscator:
    def __init__(self, key):
        self.key = key

    def _hash(self, data):
        # Perform a SHA-256 hash with our secret key
        key_bytes = self.key.encode('utf-8')
        data_bytes = data.encode('utf-8')
        hashed = hashlib.sha256(data_bytes + key_bytes).hexdigest()
        return hashed

    def obfuscate(self, data):
        # Obfuscate the data using a custom algorithm
        hashed_data = self._hash(data)
        reversed_data = hashed_data[::-1]
        encoded_data = base64.b64encode(reversed_data.encode('utf-8')).decode('utf-8')
        return encoded_data

    def deobfuscate(self, encoded_data):
        # Deobfuscate the encoded data
        reversed_data = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
        original_data = reversed_data[::-1]
        return original_data
