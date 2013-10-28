#!/usr/bin/env python

DIGITS = '123456789'


def is_pandigital(number):
    target, base = 2, number
    number = str(number)
    while len(number) <= 9:
        if ''.join(sorted(number)) == DIGITS:
            yield int(number)
        number, target = number + str(base * target), target + 1
    yield 0


def gen_pandigital(highest=1000000):
    for number in range(9, highest):
        yield from is_pandigital(number)


def main():
    number = max(gen_pandigital())
    print(number)


if __name__ == "__main__":
    main()
