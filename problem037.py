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


def find_truncatable(target=11):
    seen = set()
    start = 11
    prime_generator = get_primes(start)
    while len(seen) != target:
        prime = next(prime_generator)
        if all(is_prime(int(str(prime)[i:])) and is_prime(int(str(prime)[:i+1])) for i in range(len(str(prime)))):
            seen.add(prime)
    return seen


def main():
    total = sum(find_truncatable())
    print(total)


if __name__ == "__main__":
    main()
