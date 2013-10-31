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


def hexagonal_grid(limit=2000):
    """
        Three cases to consider:
        1) numbers that are on the side of a particular ring; say n = 17
           it has 2 neighbors on the current ring, 2 neighbors on the previous ring
           and 2 neighbors on the outer ring. The 2 neighbors on the same ring are n + 1, n - 1,
           so the difference is 1 -> not prime. The 2 neighbors on the previous ring are consecutive
           as are the 2 neighbors on the outer ring, so maximum 2 primes.
        2) numbers on the corner of a ring, excluding the first corner. r = {1, 2, 3, 4, 5}
           differences are of the form, 6n + r [inner ring], 6n + 5 + r, 6n + 6 + r, 6n + 7 + r [outer ring],
           and self +- 1. All cases of n, r X odd, even result in maximum of 2 primes.
        3) The start and end of a ring, take the form 3*n**2 - 3*n + 2 and 3*n**2 + 3*n + 1.
           The start will have the start from the previous and next ring and self + 1, and these will never be prime, so check
           6n - 1, 6n + 1, 12n + 5 for primality
           the end will have the end from previous and next ring and self + 1, again, never prime differences, so we only have
           to check [Ignore end when n = 1 because 7 violates this rule suggesting that three neighbors are prime]
           6n - 1, 6n + 5, 12n - 7 for primality
    """
    count, ring = 1, 0
    while count < limit:
        ring += 1
        checks_start, checks_end = ((6 * ring - 1, 6 * ring + 1, 12 * ring + 5),
                                    (6 * ring - 1, 6 * ring + 5, 12 * ring - 7))

        if all(is_prime(n) for n in checks_start):
            count += 1

        if all(is_prime(n) for n in checks_end) and ring != 1:
            count += 1

        start, end = (3 * ring ** 2 - 3 * ring + 2,
                      3 * ring ** 2 + 3 * ring + 1)

    return start, end, count, ring


def main():
    start, end, count, ring = hexagonal_grid()
    print(start, end, count, ring)

if __name__ == "__main__":
    main()
