#!/usr/bin/env python
from collections import defaultdict


def calculate_cover(x, y, z, n):
    return (2 * (x * y + x * z + y * z) +
            (4 * (x + y + z + n - 2) * (n - 1)))


def generate_cuboids(target=1000, limit=30000):
    """
        Convoluted solution. Essentially creating all z, y, x, n pairs
        where z >= y >= x and the nth layer requires less than limit
        cubes to cover
    """
    cuboids = defaultdict(int)
    z, y, x, n = 1, 1, 1, 1

    while calculate_cover(z, z, z, 1) <= limit:
        y = z
        while calculate_cover(z, y, z, 1) <= limit:
            x = y
            while calculate_cover(z, y, x, 1) <= limit:
                n = 1
                while calculate_cover(z, y, x, n) <= limit:
                    cuboids[calculate_cover(z, y, x, n)] += 1

                    n += 1
                x += 1
            y += 1
        z += 1

    return min(filter(lambda i: cuboids[i] == target, cuboids))


def main():
    answer = generate_cuboids()
    print(answer)


if __name__ == "__main__":
    main()
