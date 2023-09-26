import hashlib
import os

class IntegrityChecker:
    def __init__(self):
        self.engine_directory = os.path.dirname(os.path.realpath(__file__))
        self.file_integrity_data = {}

    def calculate_file_hash(self, file_path):
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(65536)  # Read in 64KB chunks
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()

    def check_integrity(self):
        for root, _, files in os.walk(self.engine_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if file_path == os.path.realpath(__file__):  # Skip this file
                    continue
                if file_path in self.file_integrity_data:
                    current_hash = self.calculate_file_hash(file_path)
                    if current_hash != self.file_integrity_data[file_path]:
                        print(f"File {file_path} has been modified! Alert!")
                else:
                    self.file_integrity_data[file_path] = self.calculate_file_hash(file_path)

if __name__ == "__main__":
    integrity_checker = IntegrityChecker()
    integrity_checker.check_integrity()
