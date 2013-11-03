#!/usr/bin/env python
from math import sqrt
LIMIT = 10 ** 8


def sum_n_through_m(n, m):
    return (m * (m + 1) - n * (n + 1)) // 2


def sum_regular_divisors(number):
    if number < len(sum_regular_divisors.memo):
        return sum_regular_divisors.memo[number]

    max_d = int(sqrt(number)) or 1
    next_divisor, start = number, 0
    for divisor in range(1, max_d):
        num_div = next_divisor
        next_divisor = number // (divisor + 1)
        start += divisor * (num_div + sum_n_through_m(next_divisor, num_div))

    start += (number // max_d) * max_d
    if number // max_d != max_d:
        start += max_d * sum_n_through_m(number // (max_d + 1), number // max_d)

    return start

sum_regular_divisors.memo = []
sum_regular_divisors.memo = [sum_regular_divisors(number) for number in range(0, 4096)]


def farey(number):
    a, b, c, d = 0, 1, 1, number
    while c <= number:
        k = (number + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        yield (a, b)


def sum_gauss_divisors(number):
    def count_ab_mult(a, b):
        return (2 * (a if a == b else a + b) *
                sum_regular_divisors(number // (a ** 2 + b ** 2)))
    return sum(count_ab_mult(*pair) for pair in farey(int(sqrt(number))))


def find_all_divisors():
    regular, gauss = sum_regular_divisors(LIMIT), sum_gauss_divisors(LIMIT)
    return regular, gauss


def main():
    answer = find_all_divisors()
    print(answer, sum(answer))


if __name__ == "__main__":
    main()
