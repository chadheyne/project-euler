#!/usr/bin/env python


def sequence_gen(num):
    while num != 1:
        num = num // 2 if not num % 2 else 3 * num + 1
        yield num


def find_longest():
    for n in range(1, 1000000):
        yield n, sum(1 for i in sequence_gen(n))


def main():
    longest = max(find_longest(), key=lambda i: i[1])
    print(longest)


if __name__ == "__main__":
    main()
