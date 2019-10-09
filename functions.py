import doctest
import math
from typing import List


def sum_digits(n: int) -> int:
    """
    Sum the digits in a value.

    >>> sum_digits(123)
    6
    >>> sum_digits(159)
    15

    :param n: The number whose digits we need to sum.

    :return: The sum of the digits.
    """
    return sum(int(x) for x in str(n))


def factorise(n: int) -> List[int]:
    """
    Determine the factors of a number.

    >>> factorise(16)
    [1, 2, 8, 16]
    >>> factorise(127)
    [1, 127]
    >>> factorise(128)
    [1, 2, 4, 8, 16, 32, 64, 128]

    :param n: The number whose factors we want.

    :return: The list of factors.
    """
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    return sorted(factors)


def proper_divisors(n: int) -> List[int]:
    """
    Determine the proper divisors of a number (numbers less than n
    which divide evenly into n).

    >>> proper_divisors(16)
    [1, 2, 4, 8]
    >>> proper_divisors(25)
    [1, 5]
    >>> proper_divisors(127)
    [1]
    >>> proper_divisors(128)
    [1, 2, 4, 8, 16, 32, 64]

    :param n: The number whose proper divisors we want.

    :return: The list of proper divisors.
    """
    factors = []
    x = math.ceil(math.sqrt(n))
    for i in range(1, x):
        if n % i == 0:
            factors.append(i)
            if i > 1:
                factors.append(int(n / i))
    if x ** 2 == n:
        factors.append(x)
    return sorted(factors)


def prime_factorise(n: int) -> List[int]:
    """
    Determine the prime factors of a number.

    >>> prime_factorise(14)
    [2, 7]
    >>> prime_factorise(644)
    [2, 2, 7, 23]
    >>> prime_factorise(646)
    [2, 17, 19]

    :param n: The number whose prime factors we want.

    :return: The list of prime factors.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def get_prime_numbers_up_to(limit: int) -> List[int]:
    """
    Get a collection of prime numbers up to a particular number. This
    is implemented using the Sieve of Eratosthenes. See

        https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    for an explanation.

    >>> get_prime_numbers_up_to(10)
    [2, 3, 5, 7]
    >>> get_prime_numbers_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]

    :param limit: The highest value we want the prime number for.

    :return: The list of prime numbers not exceeding the limit.
    """
    number_list = list(range(2, limit))
    for i in range(0, len(number_list)):
        if number_list[i] == 0:
            continue
        for j in range(number_list[i] * 2, limit, number_list[i]):
            number_list[j - 2] = 0
    prime_list = [x for x in number_list if x != 0]
    return prime_list


def get_n_prime_numbers(count: int) -> List[int]:
    """
    Get a collection of prime numbers.

    >>> get_n_prime_numbers(4)
    [2, 3, 5, 7]
    >>> get_n_prime_numbers(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    :param count: The number of prime numbers wanted.

    :return: A list of 'count' prime numbers.
    """
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


def is_divisible_by_all(n: int, divisor_list: List[int]) -> bool:
    """
    Check whether a value is divisible by all numbers in a list.

    :param n: The value to test.
    :param divisor_list: The list of divisors.

    :return: True if the number is evenly divisible by all numbers in the list.
    """
    for x in divisor_list:
        if n % x != 0:
            return False
    return True


def is_prime(n: int, prime_list: List[int]) -> bool:
    """
    Check whether a particular number is a prime number.

    :param n: The number to test.
    :param prime_list: The list of prime numbers we're checking in.

    :return: True if the number is in the list of primes.
    """
    return not any(n % x == 0 for x in prime_list)


def is_palindrome(x: any) -> bool:
    """
    Check whether a particular value is palindromic.

    >>> is_palindrome('x')
    True
    >>> is_palindrome('12321')
    True
    >>> is_palindrome('123')
    False
    >>> is_palindrome('')
    True

    :param x: The value to check.

    :return: True if the value is a palindrome.
    """
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    doctest.testmod()
