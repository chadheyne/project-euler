#!/usr/bin/env python


def partition_factors(number, base=2):
    yield [number]
    for i in (i for i in range(base, int(number**.5) + 1) if not number % i):
        for f in partition_factors(number//i, i):
            yield [i] + f


def product_sum(highest=12000):
    products, number = {}, 2
    while len(products) < highest:
        for factor in partition_factors(number):
            k = len(factor) + number - sum(factor)
            if k not in products and k <= highest:
                products[k] = number

        number += 1

    return sum(set(products.values()))


def main():
    total = product_sum()
    print(total)


if __name__ == "__main__":
    main()
