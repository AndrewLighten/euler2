import inspect
import os
from termcolor import colored
from timeit import default_timer as timer

TARGET = 1000


def is_pythagorean_triplet(a, b, c):
    return (a * a) + (b * b) == (c * c)


def calculate():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which, a^2 + b^2 = c^2. For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c =
    1000. Find the product abc.
    """
    for a in range(1, int(TARGET / 2)):
        for b in range(a, TARGET):
            c = TARGET - (a + b)
            if is_pythagorean_triplet(a, b, c):
                return a * b * c


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
