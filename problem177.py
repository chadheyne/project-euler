#!/usr/bin/env python
from math import sin, pi
from utils.decorators import timeit


def n(x):
    y = tuple(reversed(x))
    one = [x] + [x[i:] + x[:i] for i in (2, 4, 6)]
    two = [y] + [y[i:] + y[:i] for i in (2, 4, 6)]
    return min(one + two)


@timeit
def solve_it():
    total = 0
    calc_sin = lambda n: sin(pi * n / 180)
    for a in range(1, 91):
        s = {}
        for b in range(1, 180 - a):
            for c in range(1, a):
                x = round(calc_sin(b) *
                          calc_sin(a - c) /
                          calc_sin(c) /
                          calc_sin(a + b), 9)
                if x in s:
                    s[x].append((b, c))
                else:
                    s[x] = [(b, c)]
        total += len({n((x[0], x[1], a - x[1], 180 - a - y[0],
                         y[0], y[1], a - y[1], 180 - a - x[0]))
                    for xx, yy in zip(sorted(s.items()), reversed(sorted(s.items())))
                    for x in xx[1] for y in yy[1]})
    return total


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))


if __name__ == "__main__":
    main()
