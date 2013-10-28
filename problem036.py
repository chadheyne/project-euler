#!/usr/bin/env python


def calculate_palindromes(highest=1000000):
    for number in range(1, highest):
        numbin = bin(number).split('b')[-1]
        if str(number) == str(number)[::-1] and numbin == numbin[::-1]:
            yield number


def main():
    total = sum(calculate_palindromes())
    print(total)


if __name__ == "__main__":
    main()
