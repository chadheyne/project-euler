#!/usr/bin/env python
from operator import mul
from functools import reduce

with open('data/primes.txt') as f:
    PRIME_FACTORS = []
    for num in f:
        if int(num) <= 1000:
            PRIME_FACTORS.append(int(num))
        else:
            break
TOTIENTS = {pow(num, base): pow(num, base) - pow(num, base - 1) for num in PRIME_FACTORS
            for base in range(0, 3)}


def find_factors(number):
    if number <= 1:
        return
    prime = next((x for x in PRIME_FACTORS if not number % x), number)
    yield prime
    yield from find_factors(number // prime)


def find_totient(number):
    numbers = list(find_factors(number))
    for num in set(numbers):
        power = numbers.count(num)
        if num ** power not in TOTIENTS:
            TOTIENTS[num ** power] = pow(num, power) - pow(num, power - 1)
        yield TOTIENTS[num ** power]


def main():
    sequence = sum(reduce(mul, find_totient(number), 1) for number in range(2, 1000001))
    print(sequence)


if __name__ == "__main__":
    main()
