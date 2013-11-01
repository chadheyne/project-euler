#!/usr/bin/env python


def find_special(limit=12):
    """
        x ** 2 + h ** 2 = L ** 2 and h = 2x + 1 or 2x - 1
        can be shortened to
        5 * x ** 2 +- 4 * x + 1 = L ** 2
        Recurrence relation from x0 = 0, L0 = 1
        Xn+1 = -9 * xn - 4 * Ln - 4
        Yn+1 = -20*xn - 9 * Ln - 8
    """
    x, y = 0, -1
    for i in range(limit):
        x, y = -9 * x + -4 * y + 4, -20 * x - 9 * y + 8
        yield abs(y)


def main():
    answer = sum(find_special())
    print(answer)


if __name__ == "__main__":
    main()
