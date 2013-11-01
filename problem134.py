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


def extended_gcd(a, b):
    """
        Return g, x, y such that a*x + b*y = gcd(a, b) = g
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)


def prime_pair(limit=1000000):
    """
        Solve congruent equation of the form 10 ** length(prime1) * x + prime1 % prime2 == 0
        General formulation from Wikipedia is ax % n == b
        a = 10 ** length(prime1), b = prime2 - prime1, n = prime2
        extended_gcd gives g, x, y s.t. a * x + n * y == g == gcd(a, n)
        our congruence equation then has solution x * b / g -> g == 1
        (x * b % n) * a + prime1
    """
    primes, result = get_primes(5), 0
    p1, p2 = next(primes), next(primes)

    while p1 <= limit:
        a, b, n = pow(10, len(str(p1))), p2 - p1, p2
        g, x, y = extended_gcd(a, n)
        result += ((b * x) % n) * a + p1
        p1, p2 = p2, next(primes)

    return result


def main():
    answer = prime_pair()
    print(answer)


if __name__ == "__main__":
    main()
