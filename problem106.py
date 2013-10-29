#!/usr/bin/env python
from math import factorial


def catalan(n):
    return factorial(2 * n) // (factorial(n) * factorial(n)) // (n + 1)


def choose_s(n, s):
    return factorial(n) // (factorial(s) * factorial(n - s))


def check_subsets(n=12):
    """
        Only need to check cases where the two subsets have equal length
        as the second condition is already met.
        So, we need to check (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)
        Where x(n, s) = 1 / 2 (n choose s) * (n - s choose s) - Catalan(s) * (n choose 2 * s)
    """
    answer = 0
    for s in range(2, 7):
        answer += choose_s(n, s) * choose_s(n - s, s) // 2 - catalan(s) * choose_s(n, 2 * s)
    return answer


def main():
    answer = check_subsets()
    print(answer)

if __name__ == "__main__":
    main()
