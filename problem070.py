#!/usr/bin/env python
from functools import reduce
from operator import mul

PRIMES = {int(i) for i in open('data/primes.txt').readlines() if int(i) < 10000}


def find_factors(number):
    for p in PRIMES:
        if number % p == 0:
            yield (1 - 1 / p)
        if p > number:
            break


def totient(upper_bound=10000000):
    large_primes = {int(i) for i in open('data/primes.txt').readlines() if int(i) < upper_bound}
    for n in range(2, upper_bound + 1):
        if n in large_primes:
            continue
        else:
            x = int(reduce(mul, find_factors(n), n))
            if sorted(str(x)) == sorted(str(n)) and x != n:
                yield n, x


def main():
    permutation = min(totient(), key=lambda i: i[0] / i[1])
    print(permutation)


if __name__ == "__main__":
    main()
