#!/usr/bin/env python
from itertools import product
from math import factorial

VALID_MOVES = ((0, 1), (1, 0))


def lattice_path(grid_length=20, a=20, b=20):
    '''
        Number of lattice paths from point (0, 0) to (a, b) when
        only North and East movements are allowed is given by
        a + b choose a (combinations)
    '''

    move_paths = product(VALID_MOVES, repeat=a+b)
    for move in move_paths:
        if sum(i[0] for i in move) == a and sum(i[1] for i in move) == b:
            yield move


def number_paths(grid_length=20, a=20, b=20):
    return factorial(a + b) // (factorial(a) * factorial(b))


def main():
    total_moves = number_paths()
    #total_moves = sum(1 for i in lattice_path(20))
    print(total_moves)


if __name__ == "__main__":
    main()
