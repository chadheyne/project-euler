#!/usr/bin/env python


def find_power(number):
    return sum(pow(int(digit), 5) for digit in str(number))


def generate_numbers(max=355000):
    for number in range(2, max):
        if number == find_power(number):
            yield number


def main():
    total = sum(generate_numbers())
    print(total)


if __name__ == "__main__":
    main()
