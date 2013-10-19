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


def target_prime(target):
    prime_generator = get_primes()
    for i in range(target - 1):
        next(prime_generator)
    return next(prime_generator)


def main():
    prime = target_prime(10001)
    print(prime)


if __name__ == "__main__":
    main()
