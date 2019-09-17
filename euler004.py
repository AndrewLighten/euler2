import inspect
import os
from termcolor import colored
from timeit import default_timer as timer
from functions import is_palindrome

START = 100
END = 999


def generate_palindrome_list():
    palindrome_list = list()
    for i in range(START, END):
        for j in range(i, END):
            multiple = i * j
            if is_palindrome(multiple):
                palindrome_list.append(multiple)
    return palindrome_list


def calculate():
    """
    A palindromic number reads the same both ways. The largest
    palindrome made from the product of two 2-digit numbers is

        9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit
    numbers.
    """
    return max(generate_palindrome_list())


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
