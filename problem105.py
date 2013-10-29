#!/usr/bin/env python
from itertools import combinations


def optimum(data='data/sets.txt'):
    total_good = 0
    with open(data) as f:
        sets = []
        for line in f:
            sets.append(list(map(int, line.strip().split(','))))

    for solution in sets:

        seen, bad = set(solution), False
        for i in range(2, len(solution)):
            max_seen = max(seen)
            for element in combinations(solution, i):
                subsum = sum(element)
                if subsum in seen or subsum <= max_seen:
                    bad = True
                    break
                seen.add(subsum)

        if not bad:
            total_good += sum(solution)

    return total_good


def main():
    answer = optimum()
    print(answer)

if __name__ == "__main__":
    main()
