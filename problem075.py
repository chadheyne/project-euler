#!/usr/bin/env python
from fractions import gcd
from collections import defaultdict


def triangle(highest=1500000):
    TRIPLETS = defaultdict(int)
    length = int(highest ** 0.5)

    euler = ((m, n) for m in range(3, length, 2) for n in range(1, m, 2)
             if gcd(m, n) == 1)

    for m, n in euler:
        perimeter = m * n + (m ** 2 - n ** 2) // 2 + (m ** 2 + n ** 2) // 2

        for multiple in range(perimeter, highest + 1, perimeter):
            TRIPLETS[multiple] += 1
    return TRIPLETS


def main():
    unique = triangle()
    print(sum(1 for k, v in unique.items() if v == 1))


if __name__ == "__main__":
    main()
