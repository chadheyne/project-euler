#!/usr/bin/env python


def num_hex(length=16):
    for n in range(3, length+1):
        yield 15 * 16 ** (n - 1) + 41 * 14 ** (n - 1) - (43 * 15 ** (n - 1) + 13 ** n)


def main():
    answer = sum(num_hex())
    print(hex(answer))


if __name__ == "__main__":
    main()
