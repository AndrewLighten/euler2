import os

from termcolor import colored
from timeit import default_timer as timer


def calculate():
    result = str(2 ** 1000)
    return sum(int(x) for x in result)


if __name__ == '__main__':
    start = timer()
    print(f'- Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
    delta = round(timer() - start, 4)
    print(f'- Took {colored(delta, "magenta")} sec')
