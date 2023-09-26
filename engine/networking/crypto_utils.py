import hashlib
import random
import string

def generate_salt(length=16):
    """
    Generate a random salt for cryptographic purposes.

    Args:
        length (int): Length of the salt.

    Returns:
        str: A random salt.
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def hash_password(password, salt=None):
    """
    Hash a password using a salt.

    Args:
        password (str): The password to hash.
        salt (str, optional): Salt for hashing. If not provided, a random salt will be generated.

    Returns:
        str: The hashed password.
    """
    if not salt:
        salt = generate_salt()
    password_salt = password + salt
    hashed_password = hashlib.sha256(password_salt.encode()).hexdigest()
    return hashed_password

def verify_password(hashed_password, password, salt):
    """
    Verify a password against its hashed version and salt.

    Args:
        hashed_password (str): The hashed password to compare.
        password (str): The password to verify.
        salt (str): Salt used for hashing.

    Returns:
        bool: True if the password matches the hashed version, False otherwise.
    """
    return hashed_password == hash_password(password, salt)
