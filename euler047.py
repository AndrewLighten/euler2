import inspect
import os

from timeit import default_timer as timer
from termcolor import colored
from functions import prime_factorise

MAX_COUNT = 500000
FACTOR_COUNT = 4
SEQUENCE_COUNT = 4


def calculate():
    """
    The first two consecutive numbers to have two distinct prime
    factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime
    factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct
    prime factors each. What is the first of these numbers?
    """
    i = 2
    consecutive_list = []
    while i < MAX_COUNT:
        prime_factors = prime_factorise(i)
        distinct_prime_factors = sorted(list(set(prime_factors)))
        if len(distinct_prime_factors) == FACTOR_COUNT:
            consecutive_list.append((i, distinct_prime_factors))
            if len(consecutive_list) == SEQUENCE_COUNT:
                return i - (SEQUENCE_COUNT - 1)
        else:
            consecutive_list = []
        i += 1


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
