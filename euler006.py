import os
from termcolor import colored

NATURAL_NUMBER_COUNT = 100


def square_of_sum():
    s = NATURAL_NUMBER_COUNT * (NATURAL_NUMBER_COUNT + 1) / 2
    return int(s * s)


def sum_of_squares():
    return sum([x * x for x in range(1, NATURAL_NUMBER_COUNT + 1)])


def calculate():
    return square_of_sum() - sum_of_squares()


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
