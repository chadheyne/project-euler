#!/usr/bin/env python
CACHE = {}


def covering(n, m):
    """
        Number of ways to cover a 1xn grid with minimum length 1xm tiles
    """
    solutions = 1
    if m > n:
        return solutions
    if n in CACHE:
        return CACHE[n]

    for start in range(n - m + 1):
        for blocklength in range(m, n - start + 1):
            solutions += covering(n - start - blocklength - 1, m)

    CACHE[n] = solutions
    return solutions


def solve_covering(grid_length=50, minimum_size=3):
    n, m = grid_length, minimum_size
    solutions = covering(n, m)
    return solutions


def main():
    solutions = solve_covering()
    print(solutions)

if __name__ == "__main__":
    main()
