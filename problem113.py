#!/usr/bin/env python
from math import factorial


def choose(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


def non_bouncy(target_below=(10, 100)):
    """
        Number of non-bouncy numbers below a googol (10 ** 100):
        Case 1) Increasing number - (100 + 9) choose (9) - 1 ways
        Case 2) Decreasing number - (100 + 10) choose (10) - 1 - 100 ways
                as we can have 0 in the front or back of number.
        Case 3) Both increasing and decreasing - 1-9, 11-99, 111-999, etc.
                There are 9 such numbers for each power of 10
    """
    occurrences, num_digits = target_below

    increasing = choose(num_digits + occurrences - 1, occurrences - 1) - 1

    decreasing = choose(num_digits + occurrences, occurrences) - 1 - num_digits

    overlapping = (occurrences - 1) * num_digits

    return increasing + decreasing - overlapping


def main():
    answer = non_bouncy()
    print(answer)

if __name__ == "__main__":
    main()
