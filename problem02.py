#!/usr/bin/env python


def generate_fib(highest):
    a, b = 0, 1
    while highest >= a:
        if not a % 2:
            yield a
        a, b = b, a + b


def main():
    total = sum(el for el in generate_fib(4000000))
    print(total)


if __name__ == "__main__":
    main()
