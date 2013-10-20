#!/usr/bin/env python
from itertools import product
DIGITS = '123456789'


def pandigital():
    types = {
                2: tuple(range(1, 101)),
                3: tuple(range(1, 5000))
            }
    seen = set()
    for a, b in product(*types.values()):
        c = str(int(a) * int(b))
        if c in seen:
            continue
        if ''.join(sorted(str(a) + str(b) + c)) == DIGITS:
            yield c
            seen.add(c)


def main():
    total = sum(int(el) for el in pandigital())
    print(total)

if __name__ == "__main__":
    main()
