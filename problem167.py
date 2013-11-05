#!/usr/bin/env python
from utils.decorators import timeit


def period_length(number):
    v = 2 * number + 1
    cv, cvs = [], 0
    rmask = 1 << v
    wmask = 1 << (v + 1)
    looplst = loopsz = 0
    i, rv, lst = number + 1, 1, 4 * number + 4

    while True:
        r = (rv & 1) + (rv >> v) & 1
        loopsz += r
        if i > v and r:
            cvs += 2 * i + 1 - lst
            lst = 2 * i + 1
            cv += [cvs]

        rv = (rv * 2 + r) & (wmask - 1)
        if rv == rmask - 1:
            if i > 2 * v + 1:
                return (loopsz, 2 * i + 1 - looplst, cv[:loopsz])
            loopsz = 0
            looplst = 2 * i + 1
        i += 1


def ulam_number(number, size):
    v = 2 * number + 1
    headct = number + 4
    (loopct, loopsz, cv) = period_length(number)
    nloop, remloop = divmod(size - headct, loopct)
    f = 4 * number + 4 + nloop * loopsz + cv[remloop - 1]
    print("U(2, {:2d}: period {:7d}, size {:7d} == {})".format(v, loopct, loopsz, f))
    return f


@timeit(noprint=True)
def solve_it(size=10**11):
    total = 1
    for number in range(2, 11):
        total += ulam_number(number, size)
    return total


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
