#!/usr/bin/env python
from fractions import gcd


def right_triangles(max_coord=50):
    """
        Special case when P is on Y-axis and Q is on X-axis -- max_coord ** 2  solutions
        or P is on Y-axis and Q is not on X-axis -- max_coord ** 2 solutions
        or Q is on X-axis and P is not on Y-axis -- max_coord ** 2 solutions

    """
    number = max_coord ** 2 * 3
    for x in range(1, max_coord + 1):
        for y in range(1, max_coord + 1):
            possible_cases = gcd(x, y)
            number += min(y * possible_cases // x, (max_coord - x) * possible_cases // y) * 2
    return number


def main():
    total_triangles = right_triangles()
    print(total_triangles)


if __name__ == "__main__":
    main()
