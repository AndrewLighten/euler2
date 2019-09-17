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
    start = timer()
    print(f'- Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
    delta = round(timer() - start, 4)
    print(f'- Took {colored(delta, "magenta")} sec')
