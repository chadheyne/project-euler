#!/usr/bin/env python
from math import factorial


def choose_r(number):
    for n in range(1, number+1):
        yield factorial(number) / (factorial(n) * factorial(number - n)) > 1000000


def choose_n(highest=100):
    for i in range(1, highest+1):
        yield from choose_r(i)


def main():
    total = sum(choose_n())
    print(total)


if __name__ == "__main__":
    main()
