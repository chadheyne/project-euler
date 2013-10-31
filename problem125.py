#!/usr/bin/env python


def generate_squares(limit=10000):
    numbers = []
    for number in range(1, limit + 1):
        i, number = number + 1, number ** 2
        while number < limit ** 2:
            number, i = number + i ** 2, i + 1
            numbers.append(number)
    return set(numbers)


def palindromic(limit=10 ** 8):
    numbers = generate_squares(int(limit ** 0.5))
    return sum(filter(lambda i: str(i) == str(i)[::-1], numbers))


def main():
    answer = palindromic()
    print(answer)


if __name__ == "__main__":
    main()
