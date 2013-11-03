#!/usr/bin/env python
from functools import reduce
from fractions import Fraction, gcd
from itertools import takewhile


LIMIT = 80


def prime_sieve():
    for i in (2, 3, 5, 7):
        yield i
    primes = (prime for prime in prime_sieve())
    prime = next(primes) and next(primes)
    cross, sieve, number = prime ** 2, {}, 9
    while True:
        if number not in sieve:
            if number < cross:
                yield number
            else:
                multiple = cross + 2 * prime
                while multiple in sieve:
                    multiple += 2 * prime
                sieve[multiple] = 2 * prime
                prime = next(primes)
                cross = prime ** 2
        else:
            s = sieve.pop(number)
            multiple = number + s
            while multiple in sieve:
                multiple += s
            sieve[multiple] = s
        number += 2


PRIMES = list(takewhile(lambda prime: prime <= LIMIT, prime_sieve()))


def least_common_multiple(a, b):
    return a * b // gcd(a, b)


def max_prime(numbers):
    for prime in reversed(PRIMES):
        for number in reversed(numbers):
            if not number % prime:
                return number


def find_subsets():
    subset = [Fraction(0)]
    numbers = list(range(2, LIMIT + 1))
    while numbers:
        number = max_prime(numbers)
        numbers.remove(number)
        limit = reduce(least_common_multiple, numbers, 2)
        subset = [x for x in subset + [x + Fraction(1, number ** 2) for x in subset]
                  if not (limit ** 2) % x.denominator]

    return list(filter(lambda i: i == Fraction(1, 2), subset))


def main():
    answer = find_subsets()
    print(len(answer))


if __name__ == "__main__":
    main()
