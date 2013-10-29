#!/usr/bin/env python
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def sign(p1, p2, p3):
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y) < 0


def origin_inside(data='data/triangles.txt'):
    total_inside = 0
    with open(data) as f:
        for line in f:
            a1, a2, a3, a4, a5, a6 = line.strip().split(',')
            origin = Point(0, 0)
            p1, p2, p3 = Point(int(a1), int(a2)), Point(int(a3), int(a4)), Point(int(a5), int(a6))
            b1, b2, b3 = sign(origin, p1, p2), sign(origin, p2, p3), sign(origin, p3, p1)
            if b1 == b2 == b3:
                total_inside += 1

    return total_inside


def main():
    answer = origin_inside()
    print(answer)


if __name__ == "__main__":
    main()
