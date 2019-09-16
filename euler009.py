import os
from termcolor import colored
from euler003 import get_prime_numbers

TARGET = 1000


def is_pythagorean_triplet(a, b, c):
    return (a * a) + (b * b) == (c * c)


def calculate():
    for a in range(1, int(TARGET / 2)):
        for b in range(a, TARGET):
            c = TARGET - (a + b)
            if is_pythagorean_triplet(a, b, c):
                return a * b * c


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
