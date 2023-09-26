import hashlib
import base64

def generate_license_key(user_id):
    """Generates a unique license key based on user's ID."""
    key_base = str(user_id) + "PiroEngineLicenseKeySalt"
    hashed_key = hashlib.sha256(key_base.encode()).digest()
    return base64.urlsafe_b64encode(hashed_key).decode()

def verify_license_key(license_key, user_id):
    """Verifies if the license key is valid for the given user ID."""
    expected_key = generate_license_key(user_id)
    return license_key == expected_key
