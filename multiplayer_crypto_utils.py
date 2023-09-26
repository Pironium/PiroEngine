# multiplayer_crypto_utils.py

import hashlib
import random
import string

def generate_session_key():
    """
    Генерирует уникальный ключ сессии для мультиплеера.
    """
    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return session_key

def hash_password(password):
    """
    Хеширует пароль для безопасного хранения.
    """
    salt = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    password_with_salt = password + salt
    hashed_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    return hashed_password

def verify_password(password, hashed_password, salt):
    """
    Проверяет, соответствует ли введенный пароль хешу и соли.
    """
    password_with_salt = password + salt
    hashed_input_password = hashlib.sha256(password_with_salt.encode()).hexdigest()
    return hashed_password == hashed_input_password
