#!/usr/bin/env python
from itertools import permutations, islice


def lexicographic(target=1000000):
    return next(islice(permutations(range(10)), target-1, target))


def main():
    millionth = lexicographic()
    print(millionth)


if __name__ == "__main__":
    main()
