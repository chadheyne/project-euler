#!/usr/bin/env python


def convert_word(word):
    return sum(ord(letter) - ord('@') for letter in word)


def triangle_numbers():
    for i in range(1, 150000):
        yield int(0.5 * i * (i+1))


def count_words():
    triangles = list(triangle_numbers())
    with open('data/words.txt') as f:
        words = f.read().replace('"', '').split(",")
        for word in words:
            if convert_word(word) in triangles:
                yield word


def main():
    number = sum(1 for word in count_words())
    print(number)


if __name__ == "__main__":
    main()
