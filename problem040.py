#!/usr/bin/env python


def champernowne(target=1000000):
    numbers = [str(num) for num in range(100000)]
    indices = (1, 10, 100, 1000, 10000, 100000, 1000000)
    for i, num in enumerate(''.join(numbers)):
        if i in indices:
            yield int(num)


def main():
    value = 1
    for num in champernowne():
        value *= num
    print(value)


if __name__ == "__main__":
    main()
