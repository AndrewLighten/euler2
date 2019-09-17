import inspect
import os
from termcolor import colored

from functions import is_divisible_by_all
from timeit import default_timer as timer

FACTOR_LIST = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def calculate():
    """
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20?
    """
    accumulator = 1
    while True:
        if is_divisible_by_all(accumulator, FACTOR_LIST):
            return accumulator
        accumulator = accumulator + 1


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
