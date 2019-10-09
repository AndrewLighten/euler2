import inspect
import os

from termcolor import colored
from timeit import default_timer as timer
from functions import proper_divisors

MAX_CANDIDATE = 10000


def calculate():
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers
    less than n which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
    amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are

        1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110;
        ∴ d(220) = 284

    The proper divisors of 284 are

        1, 2, 4, 71, 142;
        ∴ d(284) = 220

    This means that 220 and 284 are amicable numbers.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    total = 0
    for n in range(1, MAX_CANDIDATE):
        b = sum(proper_divisors(n))
        a = sum(proper_divisors(b))
        if a != b and a == n:
            total += b
    return total


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
