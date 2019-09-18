import inspect
import os
from timeit import default_timer as timer

from termcolor import colored


def calculate():
    """
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317. Find the
    last ten digits of the series:

        1^1 + 2^2 + 3^3 + ... + 1000^1000.
    """

    accumulator = 0
    for i in range(1, 1001):
        accumulator += i ** i
    return str(accumulator)[-10:]


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
