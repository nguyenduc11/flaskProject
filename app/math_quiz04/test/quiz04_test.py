import random


def generate_random_pairs():
    while True:
        x = random.randint(1, 10)
        y = random.randint(1, 10)


        if x + y < 101 and x%10 + y%10 > 10:
            return x, y


x, y = generate_random_pairs()
print(f"x: {x}, y: {y}")