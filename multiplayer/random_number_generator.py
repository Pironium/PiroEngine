import random

def generate_unique_random_numbers(count):
    """
    Generates a list of unique random numbers.

    :param count: The number of unique random numbers to generate.
    :return: A list of unique random numbers.
    """
    if count <= 0:
        raise ValueError("Count must be a positive integer.")
    
    # Create a pool of possible random numbers.
    pool = list(range(1, 1000000))  # Assume a range of 1 to 1,000,000 for uniqueness.

    if count > len(pool):
        raise ValueError("Count exceeds the maximum possible unique numbers.")

    # Shuffle the pool and select the first 'count' numbers.
    random.shuffle(pool)
    unique_numbers = pool[:count]

    return unique_numbers
