import inspect
import os

from timeit import default_timer as timer
from termcolor import colored

from functions import get_n_prime_numbers

PRIME_COUNT = 10001


def calculate():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
    can see that the 6th prime is 13. What is the 10,001st prime number?
    """
    return get_n_prime_numbers(PRIME_COUNT)[-1]


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
