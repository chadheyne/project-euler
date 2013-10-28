#!/usr/bin/env python


def is_prime(num):
    if num > 1:
        if num in (2, 3):
            return True
        if not (num % 2 and num % 3):
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if not num % i:
                return False
        return True
    return False


def generate_spiral(grid_length=1001):
    num_per_side = 3
    start = 2
    while True:
        current = range(start + num_per_side - 2, num_per_side ** 2 + 1, num_per_side - 1)
        start = num_per_side ** 2 + 1
        yield current, num_per_side
        num_per_side += 2


def prime_diagonals():
    gen_grid = generate_spiral()
    diagonals, primes = set(), set()
    diagonals.add(1)

    for row, length in gen_grid:
        for num in row:
            diagonals.add(num)
            if is_prime(num):
                primes.add(num)

        if len(primes.intersection(diagonals)) / len(diagonals) < 0.10:
            return length, len(primes.intersection(diagonals)) / len(diagonals), len(diagonals)


def main():
    highest = prime_diagonals()
    print(highest)


if __name__ == "__main__":
    main()
