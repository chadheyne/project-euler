#!/usr/bin/env python
from itertools import product, permutations
from collections import defaultdict


def triangle(n=45):
    '''
        Generate triangle numbers: n = 45 -> 140 yield 4 digit numbers
    '''
    while n <= 140:
        yield n * (n + 1) // 2
        n += 1


def square(n=32):
    '''
        Generate squares: n = 32 -> 99 yield 4 digit numbers
    '''
    while n <= 99:
        yield n * n
        n += 1


def pentagonal(n=26):
    '''
        Generate pentagonal numbers: 26 -> 81 yield 4 digit numbers
    '''
    while n <= 81:
        yield n * (3 * n - 1) // 2
        n += 1


def hexagonal(n=23):
    '''
        Gemerate hexagonal numbers: 23 -> 70 yield 4 digit numbers
    '''
    while n <= 70:
        yield n * (2 * n - 1)
        n += 1


def heptagonal(n=21):
    '''
        Generate heptagonal numbers: 21 -> 63 yield 4 digit numbers
    '''
    while n <= 63:
        yield n * (5 * n - 3) // 2
        n += 1


def octagonal(n=19):
    '''
        Generate octagonal numbers: 19 -> 58 yield 4 digit numbers
    '''
    while n <= 58:
        yield n * (3 * n - 2)
        n += 1

figurates = {
    0: set(filter(lambda n: n % 100 > 10, set(triangle()))),
    1: set(filter(lambda n: n % 100 > 10, set(square()))),
    2: set(filter(lambda n: n % 100 > 10, set(pentagonal()))),
    3: set(filter(lambda n: n % 100 > 10, set(hexagonal()))),
    4: set(filter(lambda n: n % 100 > 10, set(heptagonal()))),
    5: set(filter(lambda n: n % 100 > 10, set(octagonal()))),
}


def check_cyclical(*numbers):
    return all(str(numbers[i])[2:] == str(numbers[(i+1) % len(numbers)])[:2]
               for i in range(len(numbers)))


def cyclical():
    for permutation in permutations(range(1, 6)):
        permutation = (0, ) + permutation
        els = map(figurates.get, permutation)
        for el in product(*els):
            if check_cyclical(*el):
                return el


def main():
    figurate = cyclical()
    print(figurate)

if __name__ == "__main__":
    main()
