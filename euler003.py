import inspect
import os

from termcolor import colored
from timeit import default_timer as timer
from functions import get_n_prime_numbers

TARGET = 600851475143
PRIME_COUNT = 1000


def find_next_prime_factor(accumulator, prime_list):
    for prime in prime_list:
        if accumulator % prime == 0:
            return prime
    print(accumulator)
    return -1


def calculate():
    """
    The prime factors of 13195 are 5, 7, 13 and 29. What is the largest
    prime factor of the number 600851475143?
    """
    prime_list = get_n_prime_numbers(PRIME_COUNT)
    factor_list = []
    accumulator = TARGET
    while accumulator > 1:
        first_prime = find_next_prime_factor(accumulator, prime_list)
        factor_list.append(first_prime)
        accumulator = accumulator / first_prime
    return max(factor_list)


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
