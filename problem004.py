#!/usr/bin/env python


def generate_palindrome(start):
    if not 100 <= start <= 999:
        return
    pal = next((num for num in range(100, 1000)
                if str(num * start) == str(num * start)[::-1]), None)
    if pal:
        yield (pal, start)
    yield from generate_palindrome(start - 1)


def main():
    pal, start = max(generate_palindrome(999), key=lambda num: int.__mul__(*num))
    print(pal, start)
    print(pal * start)


if __name__ == "__main__":
    main()
