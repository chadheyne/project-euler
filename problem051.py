#!/usr/bin/env python
from itertools import product


def prime_replacement():
    primes = {i.strip() for i in open('data/primes.txt').readlines() if len(i.strip()) == 6}
    replacements = tuple(product(range(2), repeat=6))
    for prime in sorted(primes):
        word = list(prime)
        for rep in replacements:
            changed = {''.join(word[i] if rep[i] else n for i in range(6)) for n in '0123456789'}
            total = len(primes.intersection(changed))
            if total == 8:
                return prime, primes.intersection(changed), rep


def main():
    prime = prime_replacement()
    print(prime)


if __name__ == "__main__":
    main()
