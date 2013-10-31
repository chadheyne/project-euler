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


def prime_partners(limit=1000000):
    """
        Primes of the form n ** 3 + p * n ** 2 = x ** 3.
        Simplifying gives x = n * (p + n) ** (1 / 3)
                                  ------------------
                                        n ** (1/3)
        so p + n and n must be perfect cubes for x to be an integer.
        Let k = p + n and y = n, then p = k ** 3 - y ** 3 -> p = (k - y)(k + y) ** 2
        p / (k - y) but p is prime, so k - y must be 1 and we only need to check consecutive
        cubes of the form (n + 1) ** 3 - n ** 3 for primality [Note 578 ** 3 - 577 ** 3 > 1000000]
    """
    for cube in range(1, 577):
        if is_prime(pow(cube + 1, 3) - pow(cube, 3)):
            yield cube


def main():
    answer = sum(1 for cube in prime_partners())
    print(answer)


if __name__ == "__main__":
    main()
