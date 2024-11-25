def scalar_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    return sum(x * y for x, y in zip(vector1, vector2))