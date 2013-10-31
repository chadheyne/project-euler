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


def square_remainders(target=10**10):
    primes, n = get_primes(71060), 7038
    for prime in primes:
        n += 1
        r = 2 * prime * n
        if r > target:
            return n


def main():
    answer = square_remainders()
    print(answer)


if __name__ == "__main__":
    main()
