#!/usr/bin/env python
from fractions import Fraction
from utils.decorators import timeit


@timeit
def solve_it(radius=105):
    radius_2, n, slopes = pow(radius, 2), 0, {}
    for x in range(1, radius):
        for y in range(radius):
            rad_r = pow(x, 2) + pow(y, 2)
            if rad_r < radius_2:
                n += 1
                m = Fraction(y, x)
                slopes[m] = slopes[m] + 1 if m in slopes else 1
    triangle_type1 = count1 = same_pairs = 0

    for m in sorted(slopes):
        count = slopes[m]
        count2 = n - count1 - count
        triangle_type1 += count1 * count2 * count
        same_pairs += pow(count, 2)
        count1 += count

    return 4 * (triangle_type1 + n * (pow(n, 2) - same_pairs) // 2)


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
