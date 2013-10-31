#!/usr/bin/env python
from fractions import Fraction
from functools import reduce
from operator import mul
from itertools import combinations
from math import factorial


def gamble(num_rounds=15):
    """
        Implementation does not scale well at all. Anything above fifteen rounds takes
        an obscene amount of time to run.

        Description of game is: The round starts with 1 red disc and 1 blue disc
        Each successive round, an additional red disc is added. The player wins if
        they draw more blue discs than red discs throughout the number of rounds.
        E.g., with 4 rounds: 1/2, 1/3, 1/4, 1/5 are the ratios of blue/red discs
        and the player needs 3 or 4 blue discs to win. Then the possible winning outcomes are:
        1/2 * 1/3 * 1/4 * 4/5 | 1/2 * 1/3 * 1/5 * 3/4 | 1/2 * 1/4 * 1/5 * 2/3 | 1/2 * 1/3 * 1/4 * 1/5 for n=3
        1/2 * 1/3 * 1/4 * 1/5 for n=4 ----> sum(numerators) / multiply(denominators) = probability of winning
    """
    answer = 0
    for ways_to_win in range(num_rounds // 2 + 1, num_rounds + 1):
        for drawn_blues in combinations(range(2, num_rounds + 2), ways_to_win):
            missing = [k-1 for k in range(2, num_rounds + 2) if k not in drawn_blues]
            answer += Fraction(reduce(mul, missing, 1), factorial(num_rounds+1))

    return answer.numerator, answer.denominator, answer.denominator // answer.numerator


def main():
    answer_string = ("There are {} ways to win out of {} possible outcomes: " +
                     "Yielding the payoff {}")
    play = gamble()
    print(answer_string.format(*play))

if __name__ == "__main__":
    main()
