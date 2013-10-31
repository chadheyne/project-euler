#!/usr/bin/env python
from fractions import gcd


class Radical(object):
    """
        Radical function implemented as class in order to allow nice comparisons
        as well as redefining attributes which is not available without ugly code
        using namedtuples.
    """
    def __init__(self, rad, number):
        self.rad = rad
        self.number = number

    def __repr__(self):
        return "Radical: rad - {}, number - {}".format(self.rad, self.number)

    def __lt__(self, other):
        return self.rad < other.rad or self.number < other.number

    def __eq__(self, other):
        return self.rad == other.rad and self.number == other.number

    def __gt__(self, other):
        return self.rad > other.rad or self.number > other.number


def calculate_radicals(limit=120000):
    """
        Properties:
        1) gcd(a, b) = gcd(a, c) = gcd(b, c) = 1
        2) a < b
        3) a + b = c
        4) rad(abc) < c --> rad(a) * rad(b) * rad(c) < c
                        --> rad(a) * rad(b) * rad(a + b) < a + b
    """
    radicals = [Radical(1, i) for i in range(limit)]
    result = 0
    for number in range(2, limit):
        if radicals[number].rad == 1:
            radicals[number].rad = number

            for j in range(2 * number, limit, number):
                radicals[j].rad *= number

    sorted_rad = sorted(radicals)[1:]

    for c in range(3, limit):
        rad_c = radicals[c].rad
        half_c = c // 2
        for a in sorted_rad:
            if a.rad * rad_c > half_c:
                break
            if a.number >= half_c:
                continue
            b = radicals[c - a.number]

            if a.rad * b.rad * rad_c < c and gcd(a.rad, b.rad) == 1:
                result += c

    return result


def main():
    answer = calculate_radicals()
    print(answer)


if __name__ == "__main__":
    main()
