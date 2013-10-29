#!/usr/bin/env python
from itertools import product, combinations


def optimum(length=7):
    special_6 = [11, 18, 19, 20, 22, 25]
    best_so_far = [99] * 7
    for perm in product(range(-2, 3), repeat=length - 1):
        solution = [20] + [i + j + 20 for i, j in zip(special_6, perm)]
        if sum(solution) > sum(best_so_far):
            continue

        seen, bad = set(solution), False
        for i in range(2, len(solution)):
            max_seen = max(seen)
            for element in combinations(solution, i):
                subsum = sum(element)
                if subsum in seen or subsum <= max_seen:
                    bad = True
                    break
                seen.add(subsum)
        best_so_far = solution if not bad else best_so_far

    return sorted(best_so_far)


def main():
    answer = optimum()
    print(answer)


if __name__ == "__main__":
    main()
