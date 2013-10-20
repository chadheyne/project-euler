#!/usr/bin/env python

from decimal import localcontext, Decimal

import re


def find_denominator(target=1000):
    regex = re.compile(r"(.+?)\1+")
    with localcontext() as ctx:
        ctx.prec = 2000
        for num in range(1, target+1):
            dec = str(1 / Decimal(num))
            pattern = regex.findall(dec)
            if pattern:
                yield num, max(pattern, key=len)


def main():
    longest = max(find_denominator(), key=lambda i: len(i[1]))
    print(longest)


if __name__ == "__main__":
    main()
