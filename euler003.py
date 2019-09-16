import os
from termcolor import colored

TARGET = 600851475143
PRIME_COUNT = 1000


def is_prime(test, prime_list):
    return not any(test % x == 0 for x in prime_list)


def get_prime_numbers(count):
    prime_list = [2]
    while len(prime_list) < count:
        current = prime_list[-1] + 1
        while True:
            if is_prime(current, prime_list):
                prime_list.append(current)
                break
            else:
                current += 1
    return prime_list


def find_next_prime_factor(accumulator, prime_list):
    for prime in prime_list:
        if accumulator % prime == 0:
            return prime
    print(accumulator)
    return -1


def calculate():
    prime_list = get_prime_numbers(PRIME_COUNT)
    factor_list = []
    accumulator = TARGET
    while accumulator > 1:
        first_prime = find_next_prime_factor(accumulator, prime_list)
        factor_list.append(first_prime)
        accumulator = accumulator / first_prime
    return max(factor_list)


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
