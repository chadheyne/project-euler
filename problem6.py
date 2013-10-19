#!/usr/bin/env python


def product():
    sum_sq = sum(num**2 for num in range(1, 101))
    sq_sum = sum(num for num in range(1, 101)) ** 2
    return sq_sum - sum_sq


def main():
    diff = product()
    print(diff)


if __name__ == "__main__":
    main()
