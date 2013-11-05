#!/usr/bin/env python
from utils.decorators import timeit


def even_divisors(number):
    total_divs, d = 0, 2
    while d ** 2 < number:
        if not number % (2 * d):
            total_divs += 1
        d += 2
    return total_divs


@timeit
def solve_it(limit=1000000):
    return sum(1 for number in range(4, limit + 1, 4) if even_divisors(number) in range(1, 11))


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
