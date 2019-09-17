import inspect
import os

from termcolor import colored
from timeit import default_timer as timer

WORD_LIST = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
             'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

TENS_LIST = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def words(n):
    thousands = int(n / 1000)
    n -= thousands * 1000
    hundreds = int(n / 100)
    n -= hundreds * 100
    tens = int(n / 10)
    n -= tens * 10
    units = n

    msg = ''
    if thousands:
        msg += WORD_LIST[thousands - 1] + ' thousand'
    if hundreds:
        msg += WORD_LIST[hundreds - 1] + ' hundred'
    if tens == 1:
        if msg:
            msg += ' and '
        msg += WORD_LIST[(tens * 10 + units) - 1]
    elif tens:
        if msg:
            msg += ' and '
        msg += TENS_LIST[tens - 1]
        if units:
            if msg:
                msg += '-'
            msg += WORD_LIST[units - 1]
    elif units:
        if msg:
            msg += ' and '
        msg += WORD_LIST[units - 1]
    return msg


def strip(s) -> str:
    return s.replace(' ', '').replace('-', '')


def calculate():
    """
    If the numbers 1 to 5 are written out in words: one, two, three,
    four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in
    total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were
    written out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three
    hundred and forty-two) contains 23 letters and 115 (one hundred and
    fifteen) contains 20 letters. The use of "and" when writing out
    numbers is in compliance with British usage.
    """
    accumulator = 0
    for i in range(1, 1001):
        accumulator += len(strip(words(i)))
    return accumulator


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
