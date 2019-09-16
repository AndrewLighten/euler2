import os
from termcolor import colored
from euler003 import get_prime_numbers

PRIME_COUNT = 10001


def calculate():
    x = get_prime_numbers(PRIME_COUNT)
    return x[-1]


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
