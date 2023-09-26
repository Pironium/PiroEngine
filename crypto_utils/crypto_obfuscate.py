import hashlib
import random
import string

def generate_obfuscated_code(code):
    # Шифруем исходный код с использованием хэш-функции
    hashed_code = hashlib.sha256(code.encode()).hexdigest()

    # Генерируем случайное имя переменной
    variable_name = ''.join(random.choice(string.ascii_letters) for _ in range(10))

    # Создаем функцию для расшифровки кода
    def decrypt_code():
        nonlocal hashed_code
        hashed_code = hashlib.sha256(hashed_code.encode()).hexdigest()
        return hashed_code

    # Генерируем обфусцированный код
    obfuscated_code = f"{variable_name} = '{decrypt_code()}'\nexec({variable_name})"

    return obfuscated_code

if __name__ == "__main__":
    # Пример использования
    original_code = """
    def hello_world():
        print('Hello, world!')
    hello_world()
    """

    obfuscated_code = generate_obfuscated_code(original_code)
    print(obfuscated_code)
