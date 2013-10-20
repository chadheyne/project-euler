#!/usr/bin/env python


def generate_pentagon(n=1):
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def pentagon():
    generate = generate_pentagon()
    seen = set()
    while True:
        number = next(generate)
        seen.add(number)
        for num in seen:
            if number - num in seen and number - 2 * num in seen:
                return number - 2 * num


def main():
    target = pentagon()
    print(target)


if __name__ == "__main__":
    main()
