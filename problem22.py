#!/usr/bin/env python


def find_value(name):
    return sum(ord(letter)-ord('@') for letter in name)


def names():
    name_file = open('data/names.txt').read()
    names = sorted(name.replace('"', '') for name in name_file.split(","))
    for position, name in enumerate(names):
        yield (position + 1) * find_value(name)


def main():
    total = sum(names())
    print(total)


if __name__ == "__main__":
    main()
