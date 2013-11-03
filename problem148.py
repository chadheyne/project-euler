#!/usr/bin/env python
from math import log


def divisible_pascal(num_rows=10**9, base=7):
    base_log = int(log(num_rows, base))
    perfect_power = base * (base + 1) // 2
    perfect_rows = pow(base, base_log)
    non_zero = pow(perfect_power, base_log)
    while num_rows:
        divisor, num_rows = divmod(num_rows, perfect_rows)
        yield non_zero * divisor * (divisor + 1) // 2
        perfect_rows //= base
        non_zero = non_zero * (divisor + 1) // perfect_power


def main():

    answer = sum(divisible_pascal())
    print(answer)


if __name__ == "__main__":
    main()
