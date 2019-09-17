import inspect
import os
from termcolor import colored
from functions import get_prime_numbers_up_to
from timeit import default_timer as timer

PRIME_LIMIT = 2000000


def calculate():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum
    of all the primes below two million.
    """
    return sum(get_prime_numbers_up_to(PRIME_LIMIT))


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
