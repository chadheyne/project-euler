#!/usr/bin/env python


def find_sum(base=2, exponent=1000):
    return pow(base, exponent)


def main():
    digits = str(find_sum())
    sum_digits = sum(int(i) for i in digits)
    print(sum_digits)


if __name__ == "__main__":
    main()
