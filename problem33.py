#!/usr/bin/env python
from fractions import Fraction


def find_fractions(a=100, b=100):
    for numerator in range(11, a):
        for denominator in range(numerator + 1, b):
            (num1, num2), (den1, den2) = divmod(numerator, 10), divmod(denominator, 10)
            if not (denominator % 10 and numerator % 10):
                continue
            if num1 in (den1, den2):
                num = num2
                den = den1 if den1 != num1 else den2
            elif num2 in (den1, den2):
                num = num1
                den = den1 if den1 != num2 else den2
            else:
                continue
            expected = num / den
            if numerator / denominator == expected:
                    yield numerator, denominator


def main():
    fractions = find_fractions()
    result = Fraction(1, 1)
    for num, denom in fractions:
        result *= Fraction(num, denom)
    print(result)


if __name__ == "__main__":
    main()
