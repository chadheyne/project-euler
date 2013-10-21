#!/usr/bin/env python


def read_primes(primes='data/primes.txt'):
    with open(primes) as f:
        for line in f:
            yield int(line)


def generate_spiral(grid_length=1001):
    num_per_side = 3
    start = 1
    while True:
        current = [start + (i + 1) * num_per_side for i in range(4)]
        start = max(current)
        num_per_side += 2
        yield current, num_per_side


def prime_diagonals():
    gen_primes = read_primes()
    gen_grid = generate_spiral()
    diagonals, primes = set(), set()
    diagonals.add(1)

    for i in range(500):
        primes.add(next(gen_primes))

    for row, length in gen_grid:
        for num in row:
            diagonals.add(num)
        while max(row) > max(primes):
            primes.add(next(gen_primes))

        if len(primes.intersection(diagonals)) / len(diagonals) < 0.10:
            return length // 4, len(primes.intersection(diagonals)) / len(diagonals), len(diagonals)


def main():
    highest = prime_diagonals()
    print(highest)


if __name__ == "__main__":
    main()
