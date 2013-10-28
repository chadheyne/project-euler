#!/usr/bin/env python
from math import sqrt


def cuboids(target=1000000):
    '''
        Reference for combinatorial arguments found at:
        http://www.mathblog.dk/project-euler-86-shortest-path-cuboid/
    '''

    side_l, count = 2, 0
    while count < target:
        side_l += 1
        for side_wh in range(3, 2 * side_l + 1):
            path = sqrt(side_wh ** 2 + side_l ** 2)
            if path.is_integer():
                count += (side_wh // 2 if side_wh <= side_l
                          else 1 + (side_l - (side_wh + 1) // 2))

    return side_l


def main():
    closest = cuboids()
    print(closest)


if __name__ == "__main__":
    main()
