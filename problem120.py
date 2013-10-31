#!/usr/bin/env python


def square_remainder(highest_a=1000):
    """
        Given the equation (a - 1) ^ n + (a + 1) ^ n, let r
        be the remainder when divided by a ^ 2, for the values of a from
        3, highest_a find the sum of the maximum rs. E.g., when a=7,
        ((7 - 1) ^ n + (7 + 1) ^ n) % a ^ 2 is maximized when n=3 giving r = 42.
        When expanding the numerator, we can ignore any terms with powers >= 2,
        because the remainder will be zero, then we either have a constant when n is even
        or x*a when n is odd. The max remainder can then be expressed as 2 * a * (a - 1) // 2
    """
    return sum(2 * a * ((a - 1) // 2) for a in range(3, 1001))


def main():
    answer = square_remainder()
    print(answer)

if __name__ == "__main__":
    main()
