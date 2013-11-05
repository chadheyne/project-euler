#!/usr/bin/env python
from itertools import permutations
from fractions import gcd
from utils.decorators import timeit


def pandigital(n, a, b):
    s = ''.join(map(str, (n, a, b)))
    return set(s) == set('0123456789') and len(s) == 10


def find_triplets(a, b):
    g = gcd(a, b)
    if g == 1:
        return False
    for i in range(2, g + 1):
        if g % i:
            continue
        if pandigital(i, a // i, b // i):
            return True
    return False


def find_pairs(s):
    for i in range(1, len(s)):
        if s[i] != '0':
            if find_triplets(int(s[:i]), int(s[i:])):
                return s
    return None


@timeit
def solve_it():
    for perm in permutations("9876543210"):
        if find_pairs("".join(perm)):
            return "".join(perm)


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
