#!/usr/bin/env python
from utils.decorators import timeit
from utils.helpers import n_choose as nCr


def recurse(n=18, d=10):
    if d == 1:
        return 0 if n > 3 else 1
    return (sum(recurse(n - reps, d - 1) * nCr(n, reps)
                for reps in range(min(4, n + 1))))


@timeit(noprint=True)
def solve_it(n=18, d=10):
    return recurse(n, d)


def main():
    answer, time = solve_it(n=18, d=10)
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(9 * answer // 10, time))

if __name__ == "__main__":
    main()
