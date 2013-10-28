#!/usr/bin/env python
from decimal import Decimal, getcontext
getcontext().prec = 102


def digital_sum(limit=100):
    total = 0
    for number in range(2, limit + 1):
        if number == int(number ** 0.5) ** 2:
            continue
        number = str(Decimal(number).sqrt()).replace('.', '')[:100]
        total += sum(map(int, number))
    return total


def main():
    answer = digital_sum(100)
    print(answer)


if __name__ == "__main__":
    main()
