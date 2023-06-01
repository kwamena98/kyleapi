import random

def generate_random_string(length):
    """Generate a random string of given length."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

# Generate 10 random strings of length 10
random_strings = generate_random_string(10)

print(random_strings)