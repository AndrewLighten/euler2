import inspect
import math
import os

from termcolor import colored
from timeit import default_timer as timer

import functions

LIMIT = 1000000


def calculate():
    """
    Euler's Totient function, φ(n) [sometimes called the phi function],
    is used to determine the number of numbers less than n which are
    relatively prime to n.

    For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and
    relatively prime to nine, so φ(9)=6.

        n   Relatively Prime    φ(n)    n/φ(n)
        2   1                   1       2
        3   1,2                 2       1.5
        4   1,3                 2       2
        5   1,2,3,4             4       1.25
        6   1,5                 2       3
        7   1,2,3,4,5,6         6       1.1666...
        8   1,3,5,7             4       2
        9   1,2,4,5,7,8         6       1.5
        10  1,3,7,9             4       2.5

    It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10. Find
    the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

    First tried to brute-force this, but that results in having to do
    basically 500,000,500,000 (500 billion) operations...

    Solution found at:

        https://www.mathblog.dk/project-euler-69-find-the-value-of-n-%E2%89%A4-1000000-for-which-n%CF%86n-is-a-maximum/
    """
    prime_list = functions.get_prime_numbers_up_to(math.ceil(math.sqrt(LIMIT)))
    result = 1
    i = 0
    while result * prime_list[i] < LIMIT:
        result *= prime_list[i]
        i += 1
    return result


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
