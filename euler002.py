import inspect
import os
from termcolor import colored
from timeit import default_timer as timer


def calculate():
    """
    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms
    will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do
    not exceed four million, find the sum of the even-valued terms.
    """
    prev = 1
    curr = 1
    total = 0
    while True:
        fib = prev + curr
        if fib >= 4000000:
            break
        prev, curr = curr, fib
        if fib % 2 == 0:
            total += fib
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
