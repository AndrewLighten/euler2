import os
from termcolor import colored

FACTOR_LIST = [9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# FACTOR_LIST = [9, 15]


def is_divisible_by_all(accumulator, factor_list):
    for x in factor_list:
        if accumulator % x != 0:
            return False
    return True


def calculate():
    accumulator = 1
    while True:
        if is_divisible_by_all(accumulator, FACTOR_LIST):
            return accumulator
        accumulator = accumulator + 1


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
