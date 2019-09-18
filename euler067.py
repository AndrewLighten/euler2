import inspect
import os

from termcolor import colored
from timeit import default_timer as timer


def collapse(rows, n):
    for i in range(len(rows[n])):
        rows[n][i] += max(rows[n + 1][i], rows[n + 1][i + 1])
    if len(rows[n]) == 1:
        return rows[n][0]
    else:
        return collapse(rows, n - 1)


def calculate():
    """
    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

    That is, 3 + 7 + 4 + 9 = 23. Find the maximum total from top to
    bottom in 'p067_triangle.txt', a 15K text file containing a triangle
    with one-hundred rows.

    NOTE: This is a much more difficult version of Problem 18. It is
    not possible to try every route to solve this problem, as there are
    2^99 altogether! If you could check one trillion (10^12) routes
    every second it would take over twenty billion years to check them
    all. There is an efficient algorithm to solve it. ;o)
    """
    rows = []
    with open("p067_triangle.txt") as fd:
        for line in fd:
            rows.append([int(i) for i in line.rstrip("\n").split(" ")])
    return collapse(rows, len(rows) - 2)


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
