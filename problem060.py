#!/usr/bin/env python
from itertools import permutations

with open('data/primes.txt') as f:
    PRIMES = {i.strip() for i in f.readlines() if int(i) < 15000}


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


def prime_list(*check_primes):
    return all(is_prime(int(cp1 + cp2))
               for cp1, cp2 in permutations(check_primes, 2))


def prime_combinations(length=5):
    primes = sorted(PRIMES, key=lambda i: int(i))
    for prime in primes:
        for prime2 in primes[primes.index(prime):]:
            if not prime_list(prime, prime2):
                continue
            for prime3 in primes[primes.index(prime2):]:
                if not prime_list(prime, prime2, prime3):
                    continue
                for prime4 in primes[primes.index(prime3):]:
                    if not prime_list(prime, prime2, prime3, prime4):
                        continue
                    for prime5 in primes[primes.index(prime4):]:
                        if prime_list(prime, prime2, prime3, prime4, prime5):
                            return prime, prime2, prime3, prime4, prime5


def main():
    five_combo = prime_combinations()
    print(five_combo, sum(map(int, five_combo)))

if __name__ == "__main__":
    main()
