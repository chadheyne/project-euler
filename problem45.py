#!/usr/bin/env python


def triangle(n=1):
    while True:
        yield n * (n + 1) // 2
        n += 1


def pentagonal(n=1):
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def hexagonal(n=1):
    while True:
        yield n * (2 * n - 1)
        n += 1


def find_number():
    tset, pset, hset = set(), set(), set()
    t, p, h = triangle(286), pentagonal(166), hexagonal(144)
    while True:
        tset.add(next(t))
        pset.add(next(p))
        hset.add(next(h))
        if tset.intersection(pset.intersection(hset)):
            return tset.intersection(pset.intersection(hset))


def main():
    number = find_number()
    print(number)


if __name__ == "__main__":
    main()
