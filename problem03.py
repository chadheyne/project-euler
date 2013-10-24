#!/usr/bin/env python
from math import sqrt, ceil


def find_factors(start):
    if start <= 1:
        return
    prime = next((x for x in range(2, ceil(sqrt(start) + 1)) if not start % x), start)
    yield prime
    yield from find_factors(start//prime)


def main():
    start = max(find_factors(600851475143))
    print(start)


if __name__ == "__main__":
    main()
