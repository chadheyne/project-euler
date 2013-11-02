#!/usr/bin/env python


def modified_nuggets(limit=30):
    initial_values = ((0, -1), (0, 1), (-3, -2), (-3, 2),
                      (-4, -5), (-4, 5), (2, -7), (2, 7))
    results = set()
    for x, y in initial_values:
        for i in range(30):
            x, y = -9 * x - 4 * y - 14, -20 * x - 9 * y - 28
            if x > 0:
                results.add(x)

    return sorted(results)[:30]


def main():
    answer = modified_nuggets()
    print(answer, sum(answer))


if __name__ == "__main__":
    main()
