#!/usr/bin/env python


def find_factors(number):
    for i in range(1, number//2 + 1):
        if not number % i:
            yield i


def is_amicable(number1):
    result = sum(find_factors(number1))
    if result != number1 and sum(find_factors(result)) == number1:
        return result + number1
    return 0


def find_amicable(limit=10000):
    seen = set()
    for number in range(1, limit):
        if number not in seen:
            yield is_amicable(number)
        seen.add(sum(find_factors(number)))


def main():
    amicable = sum(find_amicable(10000))
    print(amicable)


if __name__ == "__main__":
    main()
