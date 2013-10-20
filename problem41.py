#!/usr/bin/env python


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


def get_primes(number=2):
    while True:
        if is_prime(number):
            yield number
        number += 1


def is_pandigital(num):
    numset = set(int(i) for i in str(num))
    return numset == set(range(1, len(str(num))+1))


def pandigital_prime(n=9):
    primes = get_primes(2)
    for prime in primes:
        if prime > 10000000:
            break
        if is_pandigital(prime):
            yield prime


def main():
    largest = max(pandigital_prime())
    print(largest)


if __name__ == "__main__":
    main()
