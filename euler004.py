import os
from termcolor import colored

START = 100
END = 999


def is_palindrome(x):
    return str(x) == str(x)[::-1]


def generate_palindrome_list():
    palindrome_list = list()
    calc_count = 0
    for i in range(START, END):
        for j in range(i, END):
            calc_count += 1
            multiple = i * j
            if is_palindrome(multiple):
                palindrome_list.append(multiple)
    print(calc_count)
    return palindrome_list


def calculate():
    return max(generate_palindrome_list())


if __name__ == '__main__':
    print(f'Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
