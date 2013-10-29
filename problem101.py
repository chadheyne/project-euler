#!/usr/bin/env python
from sympy import symbols, Eq, solve


def base_eq(n):
    return sum(map(lambda p: (-1) ** (p - 1) * n ** (p - 1), range(1, 12)))


def solver():
    vals = {i: base_eq(i) for i in range(1, 12)}
    coefficients = a, b, c, d, e, f, g, h, i, j, k = symbols(','.join('abcdefghijk'))
    (x, n), lhs = symbols('x n'), a
    answer = 1

    for i, element in enumerate(coefficients[1:]):
        lhs = lhs * n + element
        equation = Eq(x, lhs)
        results = solve([equation.subs(dict(n=t, x=vals[t])) for
                         t in range(1, i+3)])
        results[n] = i + 3
        if element != k:
            answer += equation.subs(results).args[1]
    return answer


def main():
    answer = solver()
    print(answer)


if __name__ == "__main__":
    main()
