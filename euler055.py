import inspect
import os
from timeit import default_timer as timer

from termcolor import colored

from functions import is_palindrome

MAX_ROUNDS = 50
LIMIT = 10000


def is_lychrel(n: int) -> bool:
    rounds = 0
    while rounds < MAX_ROUNDS:
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
        rounds += 1
    return True


def calculate():
    """
    If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

    Not all numbers produce palindromes so quickly. For example,

        349 + 943 = 1292,
        1292 + 2921 = 4213
        4213 + 3124 = 7337

    That is, 349 took three iterations to arrive at a palindrome.
    Although no one has proved it yet, it is thought that some numbers,
    like 196, never produce a palindrome. A number that never forms a
    palindrome through the reverse and add process is called a Lychrel
    number. Due to the theoretical nature of these numbers, and for the
    purpose of this problem, we shall assume that a number is Lychrel
    until proven otherwise. In addition you are given that for every
    number below ten-thousand, it will either

         (i) become a palindrome in less than fifty iterations, or,
        (ii) no one, with all the computing power that exists, has
             managed so far to map it to a palindrome.

     In fact, 10677 is the first number to be shown to require over
     fifty iterations before producing a palindrome:

        4668731596684224866951378664 (53 iterations, 28-digits).

    Surprisingly, there are palindromic numbers that are themselves
    Lychrel numbers; the first example is 4994.

    How many Lychrel numbers are there below ten-thousand?
    """

    lychrel_count = 0
    for i in range(1, LIMIT + 1):
        if is_lychrel(i):
            lychrel_count += 1
    return lychrel_count


if __name__ == "__main__":
    program = os.path.splitext(os.path.basename(__file__))[0]
    start = timer()
    print(colored("-" * 70, "red"))
    print(colored(program, "red"))
    print(colored(inspect.getdoc(calculate), "yellow"))
    print(f'> {colored(calculate(), "green", attrs=["dark"])}')
    delta = round(timer() - start, 4)
    print(f'(Finished in {colored(delta, "magenta")} seconds)')
    print(colored("-" * 70, "red"))
