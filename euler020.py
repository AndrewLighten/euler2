import inspect
import os

from termcolor import colored
from timeit import default_timer as timer
from functions import factorial, sum_digits


def calculate():
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1

    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum
    of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!
    """
    return sum_digits(factorial(100))


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
