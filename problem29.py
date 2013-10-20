#!/usr/bin/env python


def generate_sequence(a=100, b=100):
    seen = set()
    for base in range(2, a+1):
        for exp in range(2, b+1):
            seen.add(pow(base, exp))
    return seen


def main():
    uniques = generate_sequence()
    print(len(uniques))


if __name__ == "__main__":
    main()
