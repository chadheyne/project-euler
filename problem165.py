#!/usr/bin/env python
from utils.decorators import timeit
from collections import namedtuple

Point = namedtuple("Point", ["x1", "y1", "x2", "y2"])


def blum_blum_shub(seed=290797, segments=5000, big_mod=50515093, small_mod=500, point=None):
    for i in range(segments):
        c = []
        for j in range(4):
            seed = seed * seed % big_mod
            c.append(seed % small_mod)
        blum_blum_shub.cache[i] = Point(*c)

blum_blum_shub.cache = {}


def intersect(i, j):
    point1, point2 = blum_blum_shub.cache[i], blum_blum_shub.cache[j]
    d = ((point2.y2 - point2.y1) * (point1.x2 - point1.x1) -
         (point2.x2 - point2.x1) * (point1.y2 - point1.y1))
    if not d:
        return 0
    ua = ((point2.x2 - point2.x1) * (point1.y1 - point2.y2) -
          (point2.y2 - point2.y1) * (point1.x1 - point2.x2)) / d
    ub = ((point1.x2 - point1.x1) * (point1.y1 - point2.y1) -
          (point1.y2 - point1.y1) * (point1.x1 - point2.x1)) / d
    if 0 < ua < 1 and 0 < ub < 1:
        return (round(point1.x1 + ua * (point1.x2 - point1.x1), 10),
                round(point1.y1 + ua * (point1.y2 - point1.y1), 10))
    return 0


@timeit
def solve_it(limit=5000):
    blum_blum_shub()
    points = set()
    for i in range(limit - 1):
        for j in range(i + 1, limit):
            p = intersect(i, j)
            if p:
                points.add(p)
    return len(points)


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
