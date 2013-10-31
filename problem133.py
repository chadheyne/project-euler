#!/usr/bin/env python


def is_prime(num):
    if num > 1:
        if num in (2, 3):
            return True
        if not (num % 2 and num % 3):
            return False
        if num < 25:
            return True
        for i in range(5, int(num**0.5) + 1, 6):
            if not (num % i and num % (i + 2)):
                return False
        return True
    return False


def get_primes(target, number=2):
    while target:
        if is_prime(number):
            yield number
        number, target = number + 1, target - 1


def repunit_factors(prime_limit=100000):
    primes, number = get_primes(prime_limit), pow(10, 16)
    factors, non_factors = set(), set()

    for prime in primes:

        if pow(10, number, 9 * prime) == 1:
            factors.add(prime)

        else:
            non_factors.add(prime)

    return sum(non_factors)


def main():
    answer = repunit_factors()
    print(answer)

if __name__ == "__main__":
    main()
