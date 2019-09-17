import inspect
import os

from termcolor import colored
from timeit import default_timer as timer

MAX_RANGE = 10 ** 6
values = dict()


def collatz_len(n) -> int:
    if values.get(n):
        return values[n]
    if n % 2 == 0:
        values[n] = 1 + collatz_len(int(n / 2))
    else:
        values[n] = 2 + collatz_len(int((3 * n + 1) / 2))
    return values[n]


def calculate():
    """
    The following iterative sequence is defined for the set of positive
    integers:

        n → n/2 (n is even)
        n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the
    following sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at
    1) contains 10 terms. Although it has not been proved yet (Collatz
    Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest
    chain?

    NOTE: Once the chain starts the terms are allowed to go above one
    million.
    """
    max_len = 0
    max_i = 0
    values[1] = 1
    for i in range(int(MAX_RANGE / 2), MAX_RANGE):
        seq_len = collatz_len(i)
        if seq_len > max_len:
            max_len = seq_len
            max_i = i
    return max_i


if __name__ == '__main__':
    program = os.path.splitext(os.path.basename(__file__))[0]
    start = timer()
    print(colored('-' * 70, 'red'))
    print(colored(program, "red"))
    print(colored(inspect.getdoc(calculate), 'yellow'))
    print(f'> {colored(calculate(), "green", attrs=["dark"])}')
    delta = round(timer() - start, 4)
    print(f'(Finished in {colored(delta, "magenta")} seconds)')
    print(colored('-' * 70, 'red'))
