#!/usr/bin/env python
from itertools import (
    permutations,
    combinations,
    chain,
    combinations_with_replacement,
    product)


def is_prime(num):
    if num > 1:
        if num in (2, 3):
            return True
        if not (num % 2 and num % 3):
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if not num % i:
                return False
        return True
    return False


def powerset(iterable):
    s = list(iterable)
    n = len(s)
    return {r: list(filter(is_prime, [int(''.join(map(str, comb))) for comb in permutations(s, r)]))
            for r in range(1, n + 1)}


def pandigital_sets():
    solutions, base_sets = set(), powerset(range(1, 10))
    set_lengths = [tuple(filter(None, comb)) for comb in
                   combinations_with_replacement(range(10), 10) if sum(comb) == 9]

    for set_length in set_lengths:
        if len(set_length) == 1:
            a, = set_length
            for prime in base_sets[a]:
                solutions.add(prime)
        else:
            a, b, *c = (set_length.count(i) for i in set(set_length))
            c = c[0] if c else None


def main():
    pass

if __name__ == "__main__":
    main()
