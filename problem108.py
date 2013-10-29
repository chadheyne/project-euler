#!/usr/bin/env python


def find_factors(number):
    PRIMES = [2, 3, 5, 7, 11, 13, 17]
    num_divisors, exponent, remainder = 1, None, number

    for prime in PRIMES:
        if prime ** 2 > number:
            return num_divisors * 2
        exponent = 1

        while not remainder % prime:
            exponent += 2
            remainder /= prime

        num_divisors *= exponent

        if remainder == 1:
            return num_divisors

    return num_divisors


def number_solutions(target=1000):
    """
        Solving reciprocal Diophantine equation of the form 1/x + 1/y = 1/n,
        find the first n such that the number of solutions > 1000.
        In order for the equation to be satisfied, x and y have to be of the form
        x + r, y + s where rs = n ** 2, so we need to find the first number that has over
        1000 sets of factors.
    """
    n, num_solutions = 4, 3
    while (num_solutions + 1) // 2 <= target:
        n += 1
        num_solutions = find_factors(n)

    return n, num_solutions


def main():
    n = number_solutions()
    print(n)

if __name__ == "__main__":
    main()
