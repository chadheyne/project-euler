#!/usr/bin/env python
from itertools import (
    permutations,
    combinations,
    combinations_with_replacement,
    product,
    chain)


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
    """
        Returns a dictionary of prime numbers of lengths from min(iterable) to max(iterable)
    """
    s = list(iterable)
    n = len(s)
    return {r: list(filter(is_prime, [int(''.join(map(str, comb))) for comb in permutations(s, r)]))
            for r in range(1, n + 1)}


def pandigital_sets():
    """
        Returns the number of sets that can be created of prime numbers where the digits
        1-9 each appear only once
    """
    solutions, base_sets = set(), powerset(range(1, 10))
    set_lengths = [tuple(filter(None, comb)) for comb in
                   combinations_with_replacement(range(10), 10) if sum(comb) == 9]

    for set_length in set_lengths:
        if set_length.count(1) > 4 or set_length.count(9):
            continue
        used = [combinations(base_sets[i], set_length.count(i)) for i in set(set_length)]
        for primes in product(*used):
            primes = list(chain.from_iterable(primes))
            if set(''.join(map(str, primes))) != set('123456789'):
                continue
            solutions.add(tuple(sorted(primes)))

    return len(solutions)


def main():
    answer = pandigital_sets()
    print(answer)

if __name__ == "__main__":
    main()
