#!/usr/bin/env python
from itertools import count


def factors(num):
    return sum(2 for i in range(1, int(num**0.5)+1) if not num % i)


def find_longest():
    c, start = count(1), 0
    for element in c:
        start += element
        if factors(start) >= 500:
            return start


def main():
    number = find_longest()
    print(number)


if __name__ == "__main__":
    main()
