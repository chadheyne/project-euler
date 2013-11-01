#!/usr/bin/env python
from math import sqrt, pow


def nth_fib(n):

    return ((pow((1 + sqrt(5)) / 2, n) - pow((1 - sqrt(5)) / 2, n))
            / sqrt(5))


def find_nuggets(target=15):
    for n in range(1, target + 1):
        yield int(nth_fib(2 * n) * nth_fib(2 * n + 1))


def main():
    for i, nugget in enumerate(find_nuggets()):
        print(i + 1, nugget)


if __name__ == "__main__":
    main()
