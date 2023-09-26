def calculate_vector_magnitude(vector):
    """Calculate the magnitude of a vector."""
    magnitude = 0
    for component in vector:
        magnitude += component**2
    return magnitude**0.5

def normalize_vector(vector):
    """Normalize a vector to have a magnitude of 1."""
    magnitude = calculate_vector_magnitude(vector)
    return [component / magnitude for component in vector]

def dot_product(vector1, vector2):
    """Calculate the dot product of two vectors."""
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

def cross_product(vector1, vector2):
    """Calculate the cross product of two vectors."""
    x = vector1[1]*vector2[2] - vector1[2]*vector2[1]
    y = vector1[2]*vector2[0] - vector1[0]*vector2[2]
    z = vector1[0]*vector2[1] - vector1[1]*vector2[0]
    return [x, y, z]
