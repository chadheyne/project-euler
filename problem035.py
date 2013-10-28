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


def find_circular(max_num=1000000):
    all_primes = {str(num) for num in range(2, max_num) if is_prime(num)}
    circular = set()
    for prime in all_primes:
        if prime in circular:
            continue
        if all(prime[i:] + prime[:i] in all_primes for i in range(len(prime))):
            for i in range(len(prime)):
                circular.add(prime[i:] + prime[:i])
    return circular


def main():
    total = find_circular()
    print(total, len(total))


if __name__ == "__main__":
    main()
