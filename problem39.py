#!/usr/bin/env python
from itertools import combinations


def is_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def max_triangle(highest=1001):
    for i in range(120, highest, 60):
        possible = combinations(range(i//2+1), 3)
        yield i, sum(1 for triangle in possible if sum(triangle) == i and is_triangle(*sorted(triangle)))


def main():
    most = max(max_triangle(), key=lambda i: i[1])
    print(most)


if __name__ == "__main__":
    main()
