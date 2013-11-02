#!/usr/bin/env python
from fractions import gcd


def find_progressive(limit=10**12):
    results = set()
    for a in range(2, int(limit**0.33) + 1):
        for b in range(1, a):
            if pow(a, 3) * pow(b, 2) + pow(b, 2) >= limit:
                break
            if gcd(a, b) != 1:
                continue
            c, n = 1, pow(a, 3) * b + pow(b, 2)
            while n < limit:
                n = pow(a, 3) * b * pow(c, 2) + c * pow(b, 2)
                if (n ** 0.5).is_integer() and n not in results:
                    results.add(n)
                    yield n
                c += 1


def main():
    answer = sum(find_progressive())
    print(answer)


if __name__ == "__main__":
    main()
