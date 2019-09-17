import math
import os

from termcolor import colored


def factorise(n):
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    return sorted(factors)


def calculate():
    base = 1
    inc = 2
    while len(factorise(base)) < 500:
        base += inc
        inc += 1
    return base


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
