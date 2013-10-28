#!/usr/bin/env python
from itertools import cycle


def create_ciphers(length=3):
    ciphers = [(i, j, k) for i in range(ord('a'), ord('z') + 1)
               for j in range(ord('a'), ord('z') + 1)
               for k in range(ord('a'), ord('z') + 1)]
    return ciphers


def convert_words(encrypted, cipher):
    repeat_cipher = cycle(cipher)
    for character in encrypted:
        yield chr(int(character) ^ next(repeat_cipher))


def infer_cipher(data='data/cipher1.txt'):
    ciphers = create_ciphers()
    encrypted = open(data).read()
    words = [i for i in encrypted.strip().split(',')]
    for cipher in ciphers:
        yield convert_words(words, cipher)


def main():
    decrypt = infer_cipher()
    for attempt in decrypt:
        words = ''.join(attempt)
        if 'John' in words:
            print(words)
            print(sum(map(lambda x: ord(x), words)))


if __name__ == "__main__":
    main()
