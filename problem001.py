#!/usr/bin/env python


def generate():
    for i in range(3, 1000):
        if (i % 3 == 0 or i % 5 == 0):
            yield i


def main():
    num = sum(generate())
    print(num)


if __name__ == "__main__":
    main()
