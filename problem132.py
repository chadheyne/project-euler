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


def get_primes(number=2):
    while True:
        if is_prime(number):
            yield number
        number += 1


def find_factors(limit=40):
    """
        Repunit of length k: R(k) = (10 ^ k - 1) / 9. And we want prime factors, so
        (10 ^ k - 1) / 9 % prime = 0 -> 10 ^ k % 9 * prime = 1
    """
    seen, number, primes = 0, pow(10, 9), get_primes()
    prime = next(primes)
    while seen < limit:
        if pow(10, number, 9 * prime) == 1:
            seen += 1
            yield prime
        prime = next(primes)


def main():
    answer = sum(find_factors())
    print(answer)

if __name__ == "__main__":
    main()
