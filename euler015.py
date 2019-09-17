import os

from termcolor import colored
from timeit import default_timer as timer


def calculate():
    max_len = 0
    return max_len


if __name__ == '__main__':
    start = timer()
    print(f'- Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
    delta = round(timer() - start, 4)
    print(f'- Took {colored(delta, "magenta")} sec')
