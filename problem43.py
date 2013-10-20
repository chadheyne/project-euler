#!/usr/bin/env python
from itertools import permutations


def is_magic(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    numbers = [number[i:i+3] for i in range(1, 8)]
    return all(int(num) % prime == 0 for num, prime in zip(numbers, primes))


def pandigitals():
    numbers = permutations('0123456789')
    for number in numbers:
        num = ''.join(number)
        if is_magic(num):
            yield num


def main():
    numbers = sum(int(num) for num in pandigitals())
    print(numbers)


if __name__ == "__main__":
    main()
