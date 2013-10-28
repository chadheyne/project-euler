#!/usr/bin/env python
from itertools import permutations
SQUARES = [str(i**2) for i in range(2, 10001)]


def anagram_squares(word_list, word_hash):
    patterns = [str.maketrans(dict(zip(word_hash, perm)))
               for perm in permutations('0123456789', len(word_hash))]
    t1 = t2 = '0'
    for pattern in patterns:
        t1, t2 = map(lambda word: word.translate(pattern), word_list)

        if len(t1) != len(t2):
            continue

        elif t1 in SQUARES and t2 in SQUARES:
            return max(int(t1), int(t2))

    return "0"


def anagrams(data='data/words.txt'):
    largest = 0
    with open(data) as f:
        words = {}
        for word in f.read().replace('"', '').split(','):
            word_sort = ''.join(sorted(word))
            if word_sort not in words:
                words[word_sort] = [word]
            else:
                words[word_sort].append(word)
        words = {similar: word_pairs for similar, word_pairs in words.items()
                 if len(word_pairs) > 1}

    for word_pair in words:
        if len(words[word_pair]) > 2:
            a, b, c = words[word_pair]
            (s1, s2) = anagram_squares([a, b], set(a)), anagram_squares([b, c], set(a))
        else:
            (s1, s2) = anagram_squares(words[word_pair], set(word_pair)), 0

        largest = max(largest, int(s1), int(s2))

    return largest


def main():
    largest = anagrams()
    print(largest)


if __name__ == "__main__":
    main()
