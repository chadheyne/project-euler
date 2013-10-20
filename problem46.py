#!/usr/bin/env python


def generate_composites(n=3):
    while True:
        yield n
        n += 2


def find_factors():
    primes = {int(i) for i in open('data/primes.txt').readlines()}
    composites = generate_composites()
    twice_square = [2 * (j ** 2) for j in range(50000)]
    for number in composites:
        if not any(number - square in primes for square in twice_square):
            yield number


def main():
    number = find_factors()
    print(next(number))

if __name__ == "__main__":
    main()
