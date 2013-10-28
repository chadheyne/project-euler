#!/usr/bin/env python
from math import factorial


CACHE = {}


def digit_sum(number):
    if number not in CACHE:
        CACHE[number] = sum(map(lambda i: factorial(int(i)), str(number)))
    return CACHE[number]


def factorial_chain(highest=1000000):
    for number in range(2, highest):
        number_chain = {number}
        replacement = number
        while True:
            replacement = digit_sum(replacement)
            if replacement in number_chain:
                break
            number_chain.add(replacement)

        if len(number_chain) == 60:
            yield number, number_chain


def main():
    total_chains = sum(1 for n, nc in factorial_chain())
    print(total_chains)


if __name__ == "__main__":
    main()
