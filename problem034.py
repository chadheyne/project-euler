#!/usr/bin/env python
from math import factorial


def find_factorials():
    '''
        2540160 = 7 * 9! which is the greatest number
        that 7 digits can add to
    '''
    for number in range(3, 2540160):
        fact_sum = sum(factorial(int(i)) for i in str(number))
        if fact_sum == number:
            yield number


def main():
    total = sum(find_factorials())
    print(total)


if __name__ == "__main__":
    main()
