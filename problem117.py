#!/usr/bin/env python
CACHE = {}


def covering(n, m, m2):
    """
        Number of ways to cover a 1xn grid with
        1x2: red tiles
        1x3: green tiles
        1x4: blue tiles
    """
    solutions = 1
    if m > n:
        return solutions
    if n in CACHE:
        return CACHE[n]

    for blocklength in range(m, m2 + 1):
        for start in range(n - blocklength + 1):
            solutions += covering(n - start - blocklength, m, m2)

    CACHE[n] = solutions
    return solutions


def solve_covering(grid_length=50, red=2, green=3, blue=4):
    n = grid_length
    solutions = covering(n, 2, 4)
    return n, solutions


def main():
    solutions = solve_covering()
    print(solutions)

if __name__ == "__main__":
    main()
