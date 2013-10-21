#!/usr/bin/env python


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def make_palindrome(number, iterations=50):
    generate_ = lambda number: (number, int(str(number)[::-1]))
    a = number
    for i in range(50):
        a, b = generate_(a)
        if is_palindrome(a + b):
            return (number, i, a, b)
        a += b
    return False


def lychrel(limit=10000):
    for i in range(100, 10000):
        yield make_palindrome(i)


def main():
    num_lychrel = sum(1 for number in lychrel() if not number)
    print(num_lychrel)


if __name__ == "__main__":
    main()
