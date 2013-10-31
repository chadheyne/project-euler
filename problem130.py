#!/usr/bin/env python
from math import ceil, sqrt


def not_prime(start):
    return any(start % x == 0 for x in range(2, ceil(sqrt(start) + 1)))


def divisible_repunit(n, k=1, x=1):
    while x:
        x = (x * 10 + 1) % n
        k += 1
    return k


def generate_repunits(target=25):
    ns, hits = [11, 13, 17, 19], 0
    while hits < target:
        for n in filter(not_prime, ns):
            if ((n - 1) / divisible_repunit(n)).is_integer():
                hits += 1
                yield n
        ns = [i + 10 for i in ns]


def main():
    answer = sum(generate_repunits())
    print(answer)


if __name__ == "__main__":
    main()
