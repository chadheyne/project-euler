#!/usr/bin/env python
from itertools import product


def pyth_triplet():
    possible = filter(lambda nums: sum(nums) == 1000 and nums == sorted(nums),
                      product(range(1, 1000), repeat=3))
    return next((poss for poss in possible if poss[0]**2+poss[1]**2 == poss[2]**2))


def main():
    a, b, c = pyth_triplet()
    print((a, b, c), a * b * c)

if __name__ == "__main__":
    main()
