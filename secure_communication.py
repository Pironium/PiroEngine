import hashlib
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hmac
from cryptography.hazmat.primitives import constant_time
from cryptography.hazmat.primitives import serialization

# Функция для генерации пары ключей (публичный и приватный) для клиента
def generate_client_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Функция для генерации пары ключей (публичный и приватный) для сервера
def generate_server_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

# Функция для генерации случайной соли
def generate_salt():
    return os.urandom(16)

# Функция для вычисления хеша пароля с использованием соли
def hash_password(password, salt):
    password = password.encode('utf-8')
    salted_password = password + salt
    hasher = hashlib.pbkdf2_hmac('sha256', salted_password, salt, 100000)
    return hasher

# Функция для инициализации ключевого производства на стороне клиента
def initialize_kdf_client(password, salt):
    password = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)
    return key

# Функция для инициализации ключевого производства на стороне сервера
def initialize_kdf_server(password, salt):
    password = password.encode('utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password)
    return key

# Функция для шифрования сообщения с использованием публичного ключа сервера
def encrypt_message(message, server_public_key):
    ciphertext = server_public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# Функция для расшифровки сообщения с использованием приватного ключа сервера
def decrypt_message(ciphertext, server_private_key):
    plaintext = server_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# Функция для создания HMAC (код аутентификации сообщения)
def create_hmac(key, message):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message.encode('utf-8'))
    return h.finalize()

# Функция для проверки HMAC (код аутентификации сообщения)
def verify_hmac(key, message, received_hmac):
    h = hmac.HMAC(key, hashes.SHA256())
    h.update(message.encode('utf-8'))
    try:
        h.verify(received_hmac)
        return True
    except InvalidSignature:
        return False

# Функция для сериализации ключа
def serialize_key(key):
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

# Функция для десериализации ключа
def deserialize_key(key_bytes):
    return serialization.load_pem_private_key(key_bytes, password=None)
