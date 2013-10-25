#!/usr/bin/env python


def combinations(x, y):
    return (x * (x + 1) * y * (y + 1)) // 4


def rectangles(target=2000000):
    x, y, error = target, 1, 999999999
    while x >= y:
        start = combinations(x, y)
        if abs(start - target) < error:
            best = x * y
            error = abs(start - target)

        if start > target:
            x -= 1
        else:
            y += 1

    return best


def main():
    closest = rectangles()
    print(closest)


if __name__ == "__main__":
    main()
