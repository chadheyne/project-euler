#!/usr/bin/env python


def solve_pells(highest=1000000000):
    """
        Pell's equation of the form
        x ** 2 - 3 * y ** 2 = 1
    """
    x1, y1 = 2, 1
    xk, yk = x1, y1
    result = 0

    while 2 * xk - 1 < highest:
        side_plus, side_minus = 2 * xk + 1, 2 * xk - 1
        area_plus, area_minus = yk * (xk + 2),  yk * (xk - 2)

        if ((side_minus > 0 and area_minus > 0) and
                (side_minus % 3 == 0 and area_minus % 3 == 0)):
            result += side_minus - 1

        if ((side_plus > 0 and area_plus > 0) and
                (side_plus % 3 == 0 and area_plus % 3 == 0)):
            result += side_plus + 1

        xk, yk = x1 * xk + 3 * y1 * yk, x1 * yk + y1 * xk

    return result


def main():
    answer = solve_pells()
    print(answer)


if __name__ == "__main__":
    main()
