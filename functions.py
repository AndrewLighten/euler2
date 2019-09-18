import math
import doctest

from typing import List, Set


def sum_digits(n: int) -> int:
    """
    Sum the digits in a value.

    :param n: The number whose digits we need to sum.

    :return: The sum of the digits.
    """
    return sum(int(x) for x in str(n))


def factorise(n: int) -> List[int]:
    """
    Determine the factors of a number.

    :param n: The number whose factors we want.

    :return: The list of factors.
    """
    factors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
    return sorted(factors)


def prime_factorise(n: int, prime_list: List[int] = None, prime_set: Set[int] = None) -> List[int]:
    """
    Determine the prime factors of a number.

    :param n: The number whose prime factors we want.
    :param prime_list: The prime number list.
    :param prime_set: The prime number list as a set (for fast find).

    :return: The list of prime factors.
    """
    if prime_set is None or prime_list is None:
        prime_list = get_prime_numbers_up_to(n + 1)
        prime_set = set(prime_list)
    prime_factors = []
    while n not in prime_set:
        for i in prime_list:
            if i > n:
                break
            if n % i == 0:
                prime_factors.append(i)
                n = int(n / i)
                break
    prime_factors.append(n)
    return prime_factors


def get_prime_numbers_up_to(limit: int) -> List[int]:
    """
    Get a collection of prime numbers up to a particular number.

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

    :param x: The value to check.

    :return: True if the value is a palindrome.
    """
    return str(x) == str(x)[::-1]


if __name__ == "__main__":
    doctest.testmod()
