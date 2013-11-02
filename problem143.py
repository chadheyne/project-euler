#!/usr/bin/env python
from fractions import gcd
from collections import defaultdict


def find_pairs(limit=120000):
    pairsa, pairsb = defaultdict(set), defaultdict(set)
    allpairs = set()
    for u in range(1, int(limit ** 0.5) + 1):
        for v in range(1, u):
            if gcd(u, v) > 1 or not (u - v) % 3:
                continue
            a, b = 2 * u * v + v * v, pow(u, 2) - pow(v, 2)
            if a + b > limit:
                break
            k = 1
            while k * (a + b) < limit:
                pairsa[k*a].add(k*b)
                pairsb[k*b].add(k*a)
                allpairs.add((k*a, k*b))
                allpairs.add((k*b, k*a))
                k += 1
    return pairsa, pairsb, allpairs


def find_points(limit=120000):
    (pairsa, pairsb, allpairs), solutions = find_pairs(limit), set()

    for a in pairsa:
        for b in pairsb[a]:
            for c in pairsa[a] - {b}:
                if (all((i, j) in allpairs for i, j in ((a, b), (b, c), (a, c))) and
                        a + b + c < limit):
                    solutions.add(a+b+c)

    return sum(solutions)


def main():
    answer = find_points()
    print(answer)


if __name__ == "__main__":
    main()
