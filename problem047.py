#!/usr/bin/env python
from math import sqrt, ceil
from itertools import count, cycle


def find_factors(start):
    if start <= 1:
        return
    prime = next((x for x in range(2, ceil(sqrt(start) + 1)) if not start % x), start)
    yield prime
    yield from find_factors(start//prime)


def distinct_factors(consecutive=4):
    c = count(1)
    sets = [set(), set(), set(), set()]
    for factors in cycle(range(4)):
        sets[factors] = set(find_factors(next(c)))
        if all(len(s) == 4 for s in sets):
            num = next(c)
            return (sets, num-1, num-2, num-3, num-4)


def main():
    four_consec = distinct_factors(4)
    print(four_consec)

if __name__ == "__main__":
    main()
