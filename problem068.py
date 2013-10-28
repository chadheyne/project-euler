#!/usr/bin/env python


def five_gon():
    '''
        Using the numbers 1-10 create 5 lines
        of length three that form a pentagon.
        The outer ring needs to be all of the largest
        numbers and the inner will be the smaller.
        The numbers on the inner ring will be counted twice,
        so 2 * (1 + 2 + 3 + 4 + 5) + 6 + 7 + 8 + 9 + 10 = 70
        suggests that all of the lines need to sum to 14.
        Given these conditions, the strings must be:
        (6, 5, 3), (10, 3, 1), (9, 1, 4), (8, 4, 2), (7, 2, 5)
    '''
    return (6, 5, 3), (10, 3, 1), (9, 1, 4), (8, 4, 2), (7, 2, 5)


def main():
    magic = ''.join(str(el) for s in five_gon() for el in s)
    print(magic)


if __name__ == "__main__":
    main()
