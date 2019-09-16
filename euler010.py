import os
from termcolor import colored
from euler003 import is_prime

PRIME_LIMIT = 2000000


def get_prime_numbers(limit):
    number_list = list(range(2, PRIME_LIMIT))
    for i in range(0, len(number_list)):
        if number_list[i] == 0:
            continue
        for j in range(number_list[i] * 2, PRIME_LIMIT, number_list[i]):
            number_list[j - 2] = 0
    prime_list = [x for x in number_list if x != 0]
    return prime_list


def calculate():
    prime_list = get_prime_numbers(PRIME_LIMIT)
    return sum(prime_list)


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
