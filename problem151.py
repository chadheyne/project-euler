#!/usr/bin/env python


def simulate(a, b, c, d):
    if a == b == c == 0 and d == 1:
        return 0
    if a == b == d == 0 and c == 1:
        return simulate(0, 0, 0, 1) + 1
    if a == c == d == 0 and b == 1:
        return simulate(0, 0, 1, 1) + 1
    if b == c == d == 0 and a == 1:
        return simulate(0, 1, 1, 1) + 1

    pick_a = 0 if a == 0 else a * simulate(a - 1, b + 1, c + 1, d + 1)
    pick_b = 0 if b == 0 else b * simulate(a, b - 1, c + 1, d + 1)
    pick_c = 0 if c == 0 else c * simulate(a, b, c - 1, d + 1)
    pick_d = 0 if d == 0 else d * simulate(a, b, c, d - 1)

    return (pick_a + pick_b + pick_c + pick_d) / (a + b + c + d)


def run_simulations():
    return simulate(1, 1, 1, 1)


def main():
    answer = run_simulations()
    print('{:6f}'.format(answer))


if __name__ == "__main__":
    main()
