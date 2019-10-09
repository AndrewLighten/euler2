import inspect
import os
from timeit import default_timer as timer

from termcolor import colored

FACTOR_LIST = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def calculate():
    """
    2520 is the smallest number that can be divided by each of the
    numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by
    all of the numbers from 1 to 20?
    """
    i = 20
    while (
        i % 2
        or i % 3
        or i % 4
        or i % 5
        or i % 6
        or i % 7
        or i % 8
        or i % 9
        or i % 10
        or i % 11
        or i % 12
        or i % 13
        or i % 14
        or i % 15
        or i % 16
        or i % 17
        or i % 18
        or i % 19
        or i % 20
    ):
        i += 20
    return i


if __name__ == "__main__":
    program = os.path.splitext(os.path.basename(__file__))[0]
    start = timer()
    print(colored("-" * 70, "red"))
    print(colored(program, "red"))
    print(colored(inspect.getdoc(calculate), "yellow"))
    print(f'> {colored(calculate(), "green", attrs=["dark"])}')
    delta = round(timer() - start, 4)
    print(f'(Finished in {colored(delta, "magenta")} seconds)')
    print(colored("-" * 70, "red"))
