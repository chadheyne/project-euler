#!/usr/bin/env python
CACHE = {}


def covering(n, m):
    """
        Number of ways to cover a 1xn grid with 3 different colors:
        red: length two
        green: length three
        blue: length four
    """
    solutions = 0
    if m > n:
        return solutions
    if (n, m) in CACHE:
        return CACHE[(n, m)]

    for start in range(n - m + 1):
        solutions += 1
        solutions += covering(n - start - m, m)

    CACHE[(n, m)] = solutions
    return solutions


def solve_covering(grid_length=50, red=2, green=3, blue=4):
    n, solutions = grid_length, 0
    for color in (red, green, blue):
        solutions += covering(n, color)
    return n, solutions


def main():
    solutions = solve_covering()
    print(solutions)

if __name__ == "__main__":
    main()
