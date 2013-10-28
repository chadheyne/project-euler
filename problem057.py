#!/usr/bin/env python


def convergents(iterations=1000):
    a, b = 3, 2
    for i in range(iterations):
        yield str(a), str(b)
        a, b = a + 2 * b, a + b


def main():
    long_numerator = sum(1 for a, b in convergents() if len(a) > len(b))
    print(long_numerator)


if __name__ == "__main__":
    main()
