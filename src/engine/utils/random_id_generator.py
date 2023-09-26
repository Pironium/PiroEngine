import random
import string

def generate_random_id(length=10):
    """
    Generate a random alphanumeric ID of the specified length.
    
    Args:
        length (int): Length of the generated ID (default is 10).
        
    Returns:
        str: A random alphanumeric ID.
    """
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return random_id

if __name__ == "__main__":
    # Example usage:
    random_id = generate_random_id()
    print("Generated Random ID:", random_id)
