#!/usr/bin/env python
from utils.decorators import timeit
from collections import defaultdict
from math import log


def func(number, p2):
    if not number:
        return 1
    if not p2 or number > p2 * 4:
        return 0
    if number in func.cache[p2]:
        return func.cache[p2][number]

    p2a = p2 // 2
    result = func(number, p2a)
    if number >= p2:
        result += func(number - p2, p2a)
    if number >= 2 * p2:
        result += func(number - p2 - p2, p2a)
    func.cache[p2][number] = result
    return result

func.cache = defaultdict(dict)


@timeit
def solve_it(limit=10 ** 25):
    return func(limit, 2 ** int(log(limit) / log(2.0)))


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
