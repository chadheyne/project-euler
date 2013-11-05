#!/usr/bin/env python
from utils.decorators import timeit


@timeit
def solve_it(limit=1000000):
    total = 0
    for i in range(1, limit//2):
        total += int((i ** 2 + limit) ** 0.5 - i) // 2
    return total


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
