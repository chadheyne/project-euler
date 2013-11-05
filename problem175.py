#!/usr/bin/env python
from fractions import Fraction
from utils.decorators import timeit


def continued_fraction(number):
    c = [int(number)]
    number -= int(number)
    while number:
        number = 1 / number
        c.append(int(number))
        number -= int(number)
    return c


@timeit
def solve_it(numerator=123456789, denominator=987654321):
    cont_fraction = continued_fraction(Fraction(numerator, denominator))[1:]
    if not len(cont_fraction) % 2:
        cont_fraction[-1] -= 1
        cont_fraction += [1]
    return ','.join(str(x) for x in reversed(cont_fraction))


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
