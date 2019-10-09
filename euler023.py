import inspect
import os
from typing import List

from termcolor import colored
from timeit import default_timer as timer

from functions import proper_divisors

LIMIT = 28123


def get_abundant_numbers(limit: int) -> List[int]:
    """
    Determine the list of abundant numbers up to the nominated limit.

    An abundant number is one whose proper divisors sum to a value
    greater than the number itself. For example, 12 has the perfect
    divisors 1, 2, 3, 4 and 6 — which sum to 16. Because 16 > 12, this
    makes 12 an abundant number.

    :param limit: The highest abundant number we're interested in.

    :return: The list of abundant numbers.
    """
    abundant_numbers = []
    for n in range(2, limit):
        divisor_sum = sum(proper_divisors(n))
        if divisor_sum > n:
            abundant_numbers.append(n)
    return abundant_numbers


def calculate():
    """
    A perfect number is a number for which the sum of its proper
    divisors is exactly equal to the number.

    For example, the sum of the proper divisors of 28 would be

        1 + 2 + 4 + 7 + 14 = 28

    which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is
    less than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number,

        1 + 2 + 3 + 4 + 6 = 16,

    the smallest number that can be written as the sum of two abundant
    numbers is 24. By mathematical analysis, it can be shown that all
    integers greater than 28123 can be written as the sum of two
    abundant numbers.

    However, this upper limit cannot be reduced any further by analysis
    even though it is known that the greatest number that cannot be
    expressed as the sum of two abundant numbers is less than this
    limit.

    Find the sum of all the positive integers which cannot be written
    as the sum of two abundant numbers.
    """

    # First find the list of all abundant numbers up to the limit
    # of our search
    abundant_numbers = get_abundant_numbers(LIMIT)

    # Next, calculate the sum of all abundant numbers and knock them
    # out of the list
    sums = [x for x in range(0, LIMIT)]
    for i in range(0, len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_number_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_number_sum < LIMIT:
                sums[abundant_number_sum] = 0
    return sum(sums)


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
