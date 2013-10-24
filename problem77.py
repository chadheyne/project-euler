#!/usr/bin/env python

with open('data/primes.txt') as f:
    PRIME_FACTORS = []
    for num in f:
        if int(num) <= 1000:
            PRIME_FACTORS.append(int(num))
        else:
            break


def find_change(target=11):

    while True:
        number_ways = [1] + [0] * target
        for prime in PRIME_FACTORS:
            for n in range(prime, target + 1):
                number_ways[n] += number_ways[n - prime]
        if number_ways[target] > 5000:
            return target
        target += 1


def main():
    first5000 = find_change()
    print(first5000)


if __name__ == "__main__":
    main()
