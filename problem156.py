#!/usr/bin/env python
from utils import decorators


def f(n, d):
    """
        Calculate total number of digits that have been written down
        after the number n has been written
    """
    start, m, quotient = 0, 1, n
    while quotient:
        quotient, remainder = divmod(quotient, 10)
        start += quotient * m + (0 if remainder < d else
                                 n - (10 * quotient + remainder) * m + 1 if remainder == d
                                 else m)
        m *= 10
    return start


def s(d):
    """
        Calculate sum of numbers that satisfy f(n, d)
    """
    c = n = 0
    while True:
        delta = f(n, d) - n
        if delta > 10 * n:
            return c
        if not delta:
            c += n
        step = max(abs(delta // 10), 1)
        n += step


@decorators.timeit
def find_solution(max_digit=9):
    return sum(s(digit) for digit in range(1, max_digit + 1))


def main():
    answer, time = find_solution()
    print("Solution is --- {}\nRunning time --- {}".format(answer, time))
    #print("Running time - {:2f}".format(end.seconds))


if __name__ == "__main__":
    main()
