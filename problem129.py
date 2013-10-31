#!/usr/bin/env python


def divisible_repunit(n, k=1, x=1):
    while x:
        x = (x * 10 + 1) % n
        k += 1
    return k


def generate_repunits(limit=1000000):
    ns = [limit + 1, limit + 3, limit + 7, limit + 9]
    while True:
        for n in ns:
            if divisible_repunit(n) > limit:
                return n
        ns = [i + 10 for i in ns]


def main():
    answer = generate_repunits()
    print(answer)

if __name__ == "__main__":
    main()
