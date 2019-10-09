import inspect
import os
from timeit import default_timer as timer

from termcolor import colored


def multiple_digits_match(n: int) -> bool:
    digits = []
    for i in range(1, 7):
        digits.append(sorted(str(n * i)))
    for i in range(1, 6):
        if digits[0] != digits[i]:
            return False
    return True


def calculate():
    """
    It can be seen that the number, 125874, and its double, 251748,
    contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that

        2x, 3x, 4x, 5x, and 6x

    contain the same digits.
    """

    i = 1
    while True:
        if multiple_digits_match(i):
            return i
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
