#!/usr/bin/env python
from itertools import product
from utils.decorators import timeit


def recurse(*args):
    if args in recurse.cache:
        return recurse.cache[args]
    l, sum_last, last_dig = args
    result = 0
    for i in range(10 - sum_last):
        result += recurse(l - 1, last_dig + i, i)
    recurse.cache[args] = result
    return result

recurse.cache = {(1, i, j): 10 - i for i in range(10) for j in range(10)}


@timeit
def find_solution():
    result = 0
    for t in filter(lambda x: x[0] < 10,
                    map(lambda t: (sum(t), t[1]),
                        product(range(1, 10), range(0, 10)))):
        result += recurse(18, *t)
    return result


def main():
    answer, time = find_solution()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
