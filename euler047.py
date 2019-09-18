import inspect
import os
from timeit import default_timer as timer

from termcolor import colored

from functions import prime_factorise, get_prime_numbers_up_to

MAX_COUNT = 500000


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
    prime_list = get_prime_numbers_up_to(MAX_COUNT)
    prime_set = set(prime_list)
    consecutive_list = []

    while i < MAX_COUNT:
        prime_factors = prime_factorise(i, prime_list, prime_set)
        distinct_prime_factors = sorted(list(set(prime_factors)))
        if len(distinct_prime_factors) == 4:
            consecutive_list.append((i, distinct_prime_factors))
            if len(consecutive_list) == 4:
                print(consecutive_list)
                return i - 4
        else:
            consecutive_list = []
        i += 1

    return 0


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
