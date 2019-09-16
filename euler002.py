import os
from termcolor import colored


def calculate():
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


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
