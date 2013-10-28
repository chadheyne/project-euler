#!/usr/bin/env python


def compute_digital_sum(number):
    return sum(int(num) for num in str(number))


def compute_powers(base=100, exponent=100):
    for a in range(1, base):
        for b in range(1, exponent):
            yield compute_digital_sum(pow(a, b))


def main():
    highest_sum = max(compute_powers())
    print(highest_sum)


if __name__ == "__main__":
    main()
