import inspect
import os
from timeit import default_timer as timer

from termcolor import colored

MIN_A = 2
MAX_A = 100

MIN_B = 2
MAX_B = 100


def calculate():
    """
    Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

        2^2=4, 2^3=8, 2^4=16, 2^5=32
        3^2=9, 3^3=27, 3^4=81, 3^5=243
        4^2=16, 4^3=64, 4^4=256, 4^5=1024
        5^2=25, 5^3=125, 5^4=625, 5^5=3125

    If they are then placed in numerical order, with any repeats
    removed, we get the following sequence of 15 distinct terms:

        4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

    How many distinct terms are in the sequence generated by

        a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
    """

    distinct_terms = set()
    for a in range(MIN_A, MAX_A + 1):
        for b in range(MIN_B, MAX_B + 1):
            x = a ** b
            distinct_terms.add(str(x))
    return len(distinct_terms), distinct_terms


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
