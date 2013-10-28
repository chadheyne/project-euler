#!/usr/bin/env python
from itertools import product


def find_factors(number):
    for i in range(1, number//2 + 1):
        if not number % i:
            yield i


def is_abundant(number1):
    if sum(find_factors(number1)) > number1:
        return True
    return False


def find_abundant(limit=28123):
    abundant = (number for number in range(1, limit) if is_abundant(number))
    two_abundants = set(map(lambda i: sum(i), product(abundant, repeat=2)))
    numbers = set(range(1, limit))
    return numbers.difference(two_abundants)


def main():
    total_sum = sum(find_abundant())
    print(total_sum)


if __name__ == "__main__":
    main()
