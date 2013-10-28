#!/usr/bin/env python
PARTITIONS = {}


def pentagonal(target):
    n = 1
    yield 0, 0
    while True:
        yield n, (3 * n ** 2 - n) // 2
        yield n + 1, (3 * n ** 2 + n) // 2
        n += 2
        if n >= target:
            break


def partition(n):
    '''
        Using the recurrence relation http://mathworld.wolfram.com/PartitionFunctionP.html
        PARTITIONS[n] = sum([(-1) ** (k + 1) * (partition(n - (k * (3 * k - 1) // 2)) +
                            partition(n - (k * (3 * k + 1) // 2))) for k in range(1, n + 1)])
    '''

    if n < 0:
        return n, 0
    elif n == 0:
        return n, 1
    elif n not in PARTITIONS:
        PARTITIONS[n] = partition(n - 1)[1]
        for i, penta in pentagonal(n):
            PARTITIONS[n] += [-1, 1][i % 4 > 1] * partition(n - penta)[1]
    return n, PARTITIONS[n]


def main():
    start = 50
    while True:
        answer, divider = partition(start)
        if divider % 1000000 == 0:
            print(answer)
            break
        start += 1
    print(answer)


if __name__ == "__main__":
    main()
