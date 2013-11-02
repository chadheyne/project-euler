#!/usr/bin/env python


def find_tilings(limit=100000000):
    """
        Need to find primitive triplets such that
        a ** 2 + (a - d) ** 2 = c ** 2 -->
        2 * a ** 2 - 2 * a * d + d ** 2 --> d ** 2 * y ** 2
        if x = 2 * a / d - 1 then
        x ** 2 - 2 * y ** 2 = -1 --> Pell's equation
        x0, y0 = 1, 1
        xn, yn = 3 * x(n-1) + 4 * y(n-1), 2 * x(n-1) + 3 * y(n-1)
    """
    x, y = 1, 1
    while x + y < limit:
        x, y = 3 * x + 4 * y, 2 * x + 3 * y
        yield limit // (x + y)


def main():
    answer = sum(find_tilings())
    print(answer)


if __name__ == "__main__":
    main()
