#!/usr/bin/env python
from itertools import product
from collections import defaultdict
from utils.decorators import timeit


@timeit
def solve_it(limit=36):
    grid = [[] for i in range(limit + 1)]
    for p in product(range(10), repeat=4):
        grid[sum(p)].append(p)

    total = 0
    for partial in range(limit + 1):
        columns_12, columns_34 = defaultdict(int), defaultdict(int)
        for a1, b1, c1, d1 in grid[partial]:
            for a2, b2, c2, d2 in grid[partial]:
                columns_12[a1 + a2, b1 + b2, c1 + c2, d1 + d2, a1 + b2, d1 + c2] += 1
                columns_34[a1 + a2, b1 + b2, c1 + c2, d1 + d2, c1 + d2, b1 + a2] += 1
        for columns in columns_12:
            total += (columns_12[columns] *
                      columns_34[tuple(map(lambda i: partial - i, columns))])
    return total


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
