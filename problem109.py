#!/usr/bin/env python
from itertools import product


DARTS = {i + str(j): j*1 if i == 'S' else j*2 if i == 'D' else j*3
         for i, j in product(['S', 'D', 'T'], range(1, 21))}
DARTS['SB'], DARTS['DB'] = 25, 50


def dart_throw(darts):
    """
        Return score of darts thrown
    """
    return sum(map(DARTS.get, darts))


def checkout(max_score=100):
    possible_scores = {i: set() for i in range(1, max_score+1)}

    for num_hits in range(1, 4):
        for throw in product(DARTS, repeat=num_hits):
            if 'D' not in throw[-1]:
                continue
            (*before, last), score = throw, dart_throw(throw)
            if score >= max_score:
                continue
            throw = sorted(before) + [last]
            possible_scores[dart_throw(throw)].add(tuple(throw))

    return possible_scores


def main():
    total_checkouts = checkout()
    print(sum(len(l) for k, l in total_checkouts.items()))


if __name__ == "__main__":
    main()
