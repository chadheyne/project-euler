#!/usr/bin/env python

PARTITIONS = {}


def partition(n):
    '''
        Using the recurrence relation http://mathworld.wolfram.com/PartitionFunctionP.html
    '''

    if n < 0:
        return 0

    elif n == 0:
        return 1

    elif n not in PARTITIONS:
        PARTITIONS[n] = sum([(-1) ** (k + 1) * (partition(n - (k * (3 * k - 1) // 2)) +
                             partition(n - (k * (3 * k + 1) // 2))) for k in range(1, n + 1)])

    return PARTITIONS[n]


def main():
    result = partition(100) - 1
    print(result)


if __name__ == "__main__":
    main()
