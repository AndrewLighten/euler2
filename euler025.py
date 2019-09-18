import inspect
import os
from timeit import default_timer as timer

from termcolor import colored


def calculate():
    """
    The Fibonacci sequence is defined by the recurrence relation:

        Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

    Hence the first 12 terms will be:

        F1 = 1
        F2 = 1
        F3 = 2
        F4 = 3
        F5 = 5
        F6 = 8
        F7 = 13
        F8 = 21
        F9 = 34
        F10 = 55
        F11 = 89
        F12 = 144

    The 12th term, F12, is the first term to contain three digits. What
    is the index of the first term in the Fibonacci sequence to contain
    1000 digits?
    """

    prev = 0
    curr = 0
    index = 0
    while True:
        index = index + 1
        fib = prev + curr
        if fib == 0:
            fib = 1
        if len(str(fib)) >= 1000:
            break
        prev, curr = curr, fib
    return index


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
