#!/usr/bin/env python


def reversible_numbers(num_digits=10):
    for i in range(1, num_digits):
        if i % 4 in (0, 2):
            yield 20 * int(pow(30, (i // 2 - 1)))
        elif i % 4 == 3:
            yield 100 * int(pow(500, i // 4))


def main():
    answer = sum(reversible_numbers())
    print(answer)


if __name__ == "__main__":
    main()
