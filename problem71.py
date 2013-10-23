#!/usr/bin/env python
from fractions import Fraction


def farey_sequence(start_low=Fraction(5, 12), target_fraction=Fraction(3, 7), max_denom=1000000):
    while True:
        temp = Fraction(start_low.numerator + target_fraction.numerator,
                        start_low.denominator + target_fraction.denominator)
        if temp.denominator > 1000000:
            return start_low
        start_low = temp


def main():
    closest = farey_sequence()
    print(closest)


if __name__ == "__main__":
    main()
