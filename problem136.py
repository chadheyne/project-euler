#!/usr/bin/env python
from itertools import islice, count


def sieve(limit):
    non_primes = {}
    yield 2
    for candidate in islice(count(3), 0, limit, 2):
        prime = non_primes.pop(candidate, None)
        if prime is None:
            non_primes[candidate ** 2] = candidate
            yield candidate
        else:
            multiple = prime + candidate
            while multiple in non_primes or not multiple % 2:
                multiple += prime
            non_primes[multiple] = prime


def same_differences(limit=50000000):
    for prime in sieve(limit):
        if prime < limit // 4:
            yield 1
        if prime < limit // 16:
            yield 1
        if not (prime - 3) % 4:
            yield 1


def main():
    answer = sum(same_differences())
    print(answer)


if __name__ == "__main__":
    main()
