#!/usr/bin/env python
from itertools import (
    combinations,
    permutations,
    chain,
    product)


def partitions(iterable):
    n, s = len(iterable), iterable
    first, middle, last = [0], range(1, n), [n]
    return ['{}'.join(map(lambda i, j: '(' + '{}'.join(s[i:j]) + ')', chain(first, div), chain(div, last)))
            for i in range(n) for div in combinations(middle, i)]


OPERATIONS = [(op1, op2, op3) for op1, op2, op3 in product(('+', '-', '/', '*'), repeat=3)]


def compute(numbers):
    for operation in OPERATIONS:
        try:
            yield eval(numbers.format(*operation))
        except ZeroDivisionError:
            yield 0


def compute_permuted(number_string):
    for perm in permutations(number_string):
        for partition in partitions(perm):
            yield from compute(partition)


def compute_combined(digits='0123456789'):
    numbers = {}
    for combo in combinations(digits, 4):
        number = ''.join(combo)
        numbers[number] = set()
        for result in compute_permuted(number):
            if result < 0:
                continue
            if isinstance(result, int) or result.is_integer():
                numbers[number].add(int(result))

    for number, results in numbers.items():
        first_missing = min([i for i in results if i+1 not in results])
        numbers[number] = first_missing

    return numbers


def main():
    results = compute_combined()
    print(max(results, key=results.get))


if __name__ == "__main__":
    main()
