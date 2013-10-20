#!/usr/bin/env python

CURRENCY = (1, 2, 5, 10, 20, 50, 100, 200)
TARGET = 200


def find_change(target=TARGET):
    number_ways = [1] + [0] * target
    for coin in CURRENCY:
        for i in range(coin, target+1):
            number_ways[i] += number_ways[i-coin]
    return number_ways[target]


def main():
    total_combos = find_change()
    print(total_combos)


if __name__ == "__main__":
    main()
