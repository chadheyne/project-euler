#!/usr/bin/env python
from itertools import permutations, chain
from math import ceil, log

TWO_FACTORS = [pow(2, i) for i in range(1, 18)]


def p_factors(n):
    if n == 0:
        return 0
    if n in p_factors.memo:
        return p_factors.memo[n]
    output = 0
    for i in range(int(log(n, 2))):
        output += n // TWO_FACTORS[i]
    p_factors.memo[n] = output
    return output


p_factors.memo = {}
CONST1 = (list(permutations((4, 1, 0), 3)) + list(permutations((3, 2, 0), 3)) +
          [(3, 1, 1), (1, 3, 1), (1, 1, 3), (2, 2, 1), (2, 1, 2), (1, 2, 2)])
CONST2 = [(4, 4, 2), (4, 2, 4), (2, 4, 4), (4, 3, 3), (3, 4, 3), (3, 3, 4)]
CONST0 = [(0, 0, 0)]


def generate_factors(combo, p1, p2, p3, index):
    total = generate_factors.multiples[index] - combo[index]
    for n in range(5):
        for m in range(5):
            i, j = n + 5 * p1, m + 5 * p2
            k = total - i - j
            if p3 * 5 <= k < p3 * 5 + 5 and i >= j >= k:
                if index == 6:
                    i, j, k = i * 5, j * 5, k * 5
                    if combo[-1] == 2:
                        perms = CONST2
                    elif combo[-1] == 1:
                        perms = CONST1
                    else:
                        perms = CONST0
                    for perm in perms:
                        a, b, c = i + perm[0], j + perm[1], k + perm[2]
                        if p_factors(200000) - p_factors(a) - p_factors(b) - p_factors(c) >= 12:
                            if a >= b >= c:
                                if a == b == c:
                                    generate_factors.count += 1
                                elif a == b or a == c or b == c:
                                    generate_factors.count += 3
                                else:
                                    generate_factors.count += 6
                else:
                    generate_factors(combo, i, j, k, index + 1)

generate_factors.count = 0


def total_divisors(exponent=200000):

    generate_factors.multiples = [exponent // 5 ** i for i in range(1, ceil(log(exponent, 5)))][::-1]
    zeros = [[2] * i + [0] + [2] * (6 - i) for i in range(1, 7)]
    ones = [[2] * i + [1] + [2] * (6 - i) for i in range(1, 7)]
    two_ones = [ones[i][:i+1+j] + [1] + ones[i][i+1+j:-1]
                for i in range(7) for j in range(1, 6-i)]

    for combo in ((0, 0, 0, 1), (1, 0, 0, 1), (1, 1, 0, 1), (2, 0, 0, 1)):
        generate_factors([2] * 7, *combo)
    for combo in chain(zeros, ones, two_ones):
        generate_factors(combo, 0, 0, 0, 1)
    for combo in ones:
        generate_factors(combo, 1, 0, 0, 1)
    return generate_factors.count


def main():
    answer = total_divisors()
    print(answer)


if __name__ == "__main__":
    main()
