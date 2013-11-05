#!/usr/bin/env python
from utils import decorators


def p_mult(number, p):
    pcount, i = 0, 1
    while number // p ** i:
        pcount += number // p ** i
        i += 1
    return pcount


def odd_factorial(number, mod_limit=10**5):
    product = 1
    for i in range(1, number + 1):
        if (i % 2 and i % 5):
            product = product * i % mod_limit
    return product


def two_factors(number, mod_limit=10**5):
    product, i = 1, 1
    while 2 ** i <= number:
        product *= odd_factorial((number // 2 ** i) % mod_limit)
        i += 1
    return product


def five_factors(number, mod_limit=10**5):
    product, i = 1, 1
    while 5 ** i <= number:
        product *= odd_factorial((number // 5 ** i) % mod_limit)
        i += 1
    return product


def ten_factors(number, mod_limit=10**5):
    return (odd_factorial(number % mod_limit) * two_factors(number) *
            five_factors(number)) % mod_limit


@decorators.timeit
def solve_it(limit=10**12, mod_limit=10**5):

    result = (odd_factorial(mod_limit) * two_factors(limit) *
              five_factors(limit)) % mod_limit

    for power in range(1, 12):
        result = result * ten_factors(limit // 10 ** power) % mod_limit

    result = (result *
              pow(2, p_mult(limit, 2) - p_mult(limit, 5), mod_limit)
              % mod_limit)

    return result


def main():
    result, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(result, time))


if __name__ == "__main__":
    main()
