import inspect
import os
from timeit import default_timer as timer

from termcolor import colored

# The highest candidate number we can look for.
# If the highest value is a six digit number, the maximum possible
# would be 6*9^5, which is 354294.
# If it was a seven digit number, the maximum would be 7*9^5 = 413343,
# so it can't be a seven digit number (because it produces a six digit
# result).
#
# We'll search up to 6*9^5.
MAX_TEST = 6 * pow(9, 5)


def calculate():
    """
    Surprisingly there are only three numbers that can be written as
    the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

    As 1 = 1^4 is not a sum it is not included. The sum of these
    numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of
    fifth powers of their digits.
    """

    total = 0
    for i in range(2, MAX_TEST):
        if i == fifth_digit_sum(i):
            total += i
    return total


def fifth_digit_sum(i: int) -> int:
    return sum(int(x) ** 5 for x in str(i))


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
