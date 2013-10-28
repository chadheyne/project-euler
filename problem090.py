#!/usr/bin/env python
from itertools import combinations, permutations, chain


def cube_digit_pairs():
    numbers = '0123456789'
    required = ['01', '04', '06', '16', '25', '36', '46', '64', '81']
    dice = combinations(combinations(numbers, 6), 2)
    seen_combinations = set()
    for dice1, dice2 in dice:
        if dice1 == dice2 or (dice1, dice2) in seen_combinations:
            continue
        temp1, temp2 = ''.join(dice1).replace('9', '6'), ''.join(dice2).replace('9', '6')
        if not all(num in temp1 + temp2 for num in '01234568'):
            continue
        permuted = [''.join((a, b)) for st in permutations(temp2) for a, b in
                    chain(zip(temp1, st), zip(st, temp1))]
        if not all(el in permuted for el in required):
            continue
        seen_combinations.add((dice1, dice2))

    return len(seen_combinations)


def main():
    total_ = cube_digit_pairs()
    print(total_)


if __name__ == "__main__":
    main()
