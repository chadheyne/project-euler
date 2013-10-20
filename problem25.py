#!/usr/bin/env python


def generate_fib(target_length=1000):
    a, b, i = 0, 1, 0
    while target_length != len(str(a)):
        a, b = b, a + b
        i += 1
    return i


def main():
    thousand = generate_fib(1000)
    print(thousand)


if __name__ == "__main__":
    main()
