#!/usr/bin/env python


def buckets(target=1000000000000):
    """
        Base equation for choosing two successive elements of the same type
        from N is (b/N) * (b-1/N-1) which we need equal to 1/2.
        Factoring gives us the equation:
        2b**2 - 2b - n ** 2 + n = 0 and we need the first b that solves this
        when n > 1000000000000
        Recurrence relation for solutions is  given by:
        b = 3 * b + 2 * n - 2
        n = 4 * b + 3 * n - 3
        base: b = 15, n = 21
    """
    b, n = 15, 21
    while n < target:
        b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3

    return b


def main():
    answer = buckets()
    print(answer)


if __name__ == "__main__":
    main()
