#!/usr/bin/env python
from itertools import product, permutations


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
    0: tuple(triangle()),
    1: tuple(square()),
    2: tuple(pentagonal()),
    3: tuple(hexagonal()),
    4: tuple(heptagonal()),
    5: tuple(octagonal()),
}


def check_cyclical(*numbers):
    return all(str(numbers[i])[-2:] == str(numbers[(i+1)])[:2]
               for i in range(len(numbers) - 1))


def cyclical():
    for permutation in permutations(range(6)):
        a, b, c, d, e, f = (figurates.get(i) for i in permutation)
        for n1, n2 in product(a, b):
            if not check_cyclical(n1, n2):
                continue
            for n3, n4 in product(c, d):
                if not check_cyclical(n1, n2, n3, n4):
                    continue
                for n5, n6 in product(e, f):
                    if check_cyclical(n1, n2, n3, n4, n5, n6, n1):
                        return n1, n2, n3, n4, n5, n6


def main():
    figurate = cyclical()
    print(figurate, sum(figurate))

if __name__ == "__main__":
    main()
