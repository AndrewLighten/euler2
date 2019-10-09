import inspect
import os
from datetime import datetime
from timeit import default_timer as timer
from termcolor import colored

SUNDAY = 6
LAST_YEAR = 2000
MONTHS_IN_YEAR = 12


def calculate():
    """
    You are given the following information, but you may prefer to do
    some research for yourself.

        1 Jan 1900 was a Monday.
        Thirty days has September,
            April, June and November.
            All the rest have thirty-one,
            Saving February alone,
            Which has twenty-eight, rain or shine.
            And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4, but not
        on a century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the
    twentieth century (1 Jan 1901 to 31 Dec 2000)?
    """
    total = 0
    for year in range(1901, LAST_YEAR + 1):
        for month in range(1, MONTHS_IN_YEAR + 1):
            if datetime(year=year, month=month, day=1).weekday() == 6:
                total += 1
    return total


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
