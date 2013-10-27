#!/usr/bin/env python
import re

REDUCE_ROMAN = re.compile(r'DC{4}|LX{4}|VI{4}|C{4}|X{4}|I{4}')


def fix_romans(data='data/roman.txt'):
    with open(data) as romans:
        numerals = []
        for numeral in romans:
            numerals.append((numeral.strip(), REDUCE_ROMAN.sub('xx', numeral.strip())))

    return sum(len(i[0]) - len(i[1]) for i in numerals)


def main():
    replacements = fix_romans()
    print(replacements)


if __name__ == "__main__":
    main()
