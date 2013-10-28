#!/usr/bin/env python
from collections import Counter


def permuted(start=100):
    while True:
        multiples = (str(start * i) for i in range(1, 7))
        counters = [Counter(m) for m in multiples]
        if all(c1 == c2 for c1 in counters for c2 in counters):
            yield start, counters
        start += 1


def main():
    answer = permuted()
    print(next(answer))

if __name__ == "__main__":
    main()
