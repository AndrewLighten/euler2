import inspect
import os
from termcolor import colored
from timeit import default_timer as timer

NATURAL_NUMBER_COUNT = 100


def square_of_sum():
    s = NATURAL_NUMBER_COUNT * (NATURAL_NUMBER_COUNT + 1) / 2
    return int(s * s)


def sum_of_squares():
    return sum([x * x for x in range(1, NATURAL_NUMBER_COUNT + 1)])


def calculate():
    """
    The sum of the squares of the first ten natural numbers is,

        1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,

        (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first
    ten natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    return square_of_sum() - sum_of_squares()


if __name__ == '__main__':
    program = os.path.splitext(os.path.basename(__file__))[0]
    start = timer()
    print(colored('-' * 70, 'red'))
    print(colored(program, "red"))
    print(colored(inspect.getdoc(calculate), 'yellow'))
    print(f'> {colored(calculate(), "green", attrs=["dark"])}')
    delta = round(timer() - start, 4)
    print(f'(Finished in {colored(delta, "magenta")} seconds)')
    print(colored('-' * 70, 'red'))
