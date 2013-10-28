#!/usr/bin/env python
from itertools import product


with open('data/primes.txt') as p:
    PRIMES = []
    for line in p:
        if int(line) < 7150:
            PRIMES.append(int(line))
        else:
            break


def prime_sums(highest=50000000):
    seen = set()
    squares = filter(lambda i: i < 7150, PRIMES)
    cubes = filter(lambda i: i < 370, PRIMES)
    quartics = filter(lambda i: i < 84, PRIMES)
    power = lambda a, b, c: a ** 2 + b ** 3 + c ** 4

    for a, b, c in product(squares, cubes, quartics):
        number = power(a, b, c)
        if number < highest:
            seen.add(number)
    return len(seen)


def main():
    total = prime_sums()
    print(total)


if __name__ == "__main__":
    main()
