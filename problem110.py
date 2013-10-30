#!/usr/bin/env python
from functools import reduce
from operator import mul


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
LIMIT = 2 * 4000000 - 1


def find_factors(exponents):
    num_divisors, exponents[0] = 1, 0

    for exponent in exponents:
        num_divisors *= 2 * exponent + 1

    exponents[0] = (LIMIT // num_divisors - 1) // 2

    while num_divisors * (2 * exponents[0] + 1) < LIMIT:
        exponents[0] += 1

    return exponents


def compute_number(exponents, result):
    number = 1

    for prime, exponent in zip(PRIMES, exponents):
        if exponent == 0:
            break
        number *= pow(prime, exponent)

    return number if number <= result else result + 1


def number_solutions():

    n, result, exponents = 1, reduce(mul, PRIMES), [1] * 6 + [0] * (len(PRIMES) - 6)
    while True:

        exponents = find_factors(exponents)
        if exponents[0] < exponents[1]:
            n += 1
        else:
            result = min(compute_number(exponents, result), result)
            n = 1
        if n >= len(exponents):
            break

        exponents[n] += 1
        exponents = [exponents[n] if i < n else e for i, e in enumerate(exponents)]

    return result


def main():
    n = number_solutions()
    print(n)

if __name__ == "__main__":
    main()
