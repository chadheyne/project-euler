#!/usr/bin/env python
from itertools import product


def is_prime(num):
    if num > 1:
        if num in (2, 3):
            return True
        if not (num % 2 and num % 3):
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if not num % i:
                return False
        return True
    return False


def get_primes(number=0, a=0, b=0):
    while True:
        formula = number ** 2 + a * number + b
        if is_prime(formula):
            yield formula
        else:
            break
        number += 1


def generate_coeffs(a=1000, b=1000):
    coeffs = product(range(-a, a), range(-b, b))
    for coeffa, coeffb in coeffs:
        primes = get_primes(0, coeffa, coeffb)
        yield coeffa, coeffb, sum(1 for el in primes)


def main():
    quadratics = max(generate_coeffs(1000, 1000), key=lambda i: i[2])
    print(quadratics)


if __name__ == "__main__":
    main()
