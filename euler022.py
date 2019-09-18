import inspect
import os
from typing import List

from termcolor import colored
from timeit import default_timer as timer


def load_name_list() -> List[str]:
    name_list = []
    with open("p022_names.txt") as f:
        lines = f.readlines()
        for line in lines:
            separated = line.replace('"', "").split(",")
            name_list.extend(separated)
    return sorted(name_list)


def score(name: str) -> int:
    return sum(ord(x) - ord("@") for x in name.upper())


def calculate():
    """
    Using p022_names.txt, a 46K text file containing over five-thousand
    first names, begin by sorting it into alphabetical order. Then
    working out the alphabetical value for each name, multiply this
    value by its alphabetical position in the list to obtain a name
    score.

    For example, when the list is sorted into alphabetical order, COLIN,
    which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
    list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """

    # Note sort order is zero-based, so have to add one when calculating
    # sort-order multiplier
    name_list = load_name_list()
    accumulator = 0
    for sort_order, name in enumerate(name_list):
        accumulator += (sort_order + 1) * score(name)
    return accumulator


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
