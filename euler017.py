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
    accumulator = 0
    for i in range(1, 1001):
        accumulator += len(strip(words(i)))
    return accumulator


if __name__ == '__main__':
    start = timer()
    print(f'- Result for {colored(os.path.splitext(os.path.basename(__file__))[0], "red")} = {colored(calculate(), "blue")}')
    delta = round(timer() - start, 4)
    print(f'- Took {colored(delta, "magenta")} sec')
