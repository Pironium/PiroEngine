# PiroProtection.py - PiroEngine Security Module

import hashlib
import random
import string

class PiroProtection:
    def __init__(self):
        self.pirate_blacklist = set()
        self.game_keys = {}
        self.key_expiration = {}

    def generate_game_key(self, game_id, validity_days=30):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        self.game_keys[game_id] = key
        expiration_time = self.calculate_expiration(validity_days)
        self.key_expiration[game_id] = expiration_time
        return key, expiration_time

    def calculate_expiration(self, validity_days):
        # Calculate expiration timestamp in seconds since epoch
        return int(time.time()) + (validity_days * 24 * 60 * 60)

    def validate_game_key(self, game_id, key):
        if game_id in self.game_keys and game_id in self.key_expiration:
            if key == self.game_keys[game_id] and time.time() < self.key_expiration[game_id]:
                return True
        return False

    def add_to_pirate_blacklist(self, pirate_ip):
        self.pirate_blacklist.add(pirate_ip)

    def check_pirate_blacklist(self, ip):
        return ip in self.pirate_blacklist

    def hash_file(self, file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536)  # Read in 64KB chunks
                if not data:
                    break
                sha256_hash.update(data)
        return sha256_hash.hexdigest()

    def verify_file_integrity(self, file_path, expected_hash):
        file_hash = self.hash_file(file_path)
        return file_hash == expected_hash
