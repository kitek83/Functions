#random_seed.py
"""Testiing usage of seed function."""
import random

random.seed(5332)

for num in range(30):
    print(random.randrange(1,7), end=' ')

