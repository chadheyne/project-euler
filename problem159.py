#!/usr/bin/env python
from math import ceil, sqrt
from utils import decorators


def digital_sum(number):
    digit_sum = number % 10
    while number >= 10:
        number //= 10
        digit_sum += number % 10
    if digit_sum < 10:
        return digit_sum
    else:
        return digital_sum(digit_sum)


def maximal_digital_sum(number):
    temp_max = digital_sum(number)
    for d in range(2, int(ceil(sqrt(number))) + 1):
        if not number % d:
            other = (maximal_digital_sum.cache[d] +
                     maximal_digital_sum.cache[number // d])
            temp_max = max(temp_max, other)
    maximal_digital_sum.cache[number] = temp_max


maximal_digital_sum.cache = {i: 0 for i in range(10 ** 6)}


@decorators.timeit
def find_total(limit=10**6):
    for number in range(2, limit):
        maximal_digital_sum(number)
    return sum(maximal_digital_sum.cache.values())


def main():
    answer, time = find_total()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
