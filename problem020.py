#!/usr/bin/env python
from math import factorial


def find_number(number=100):
    return str(factorial(number))


def main():
    number = sum(map(int, find_number(100)))
    print(number)


if __name__ == "__main__":
    main()
