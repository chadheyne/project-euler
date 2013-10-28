#!/usr/bin/env python


def fractional_coeffs():
    k = 2
    while True:
        yield 1
        yield k
        yield 1
        k += 2


def convergents():
    pn2, pn1, pn = 1, 1, 1
    qn2, qn1, qn = 0, 1, 1
    gen = fractional_coeffs()
    for _ in range(99):
        n = next(gen)
        pn = n * pn1 + pn2
        qn = n * qn1 + qn2
        pn1, pn2 = pn, pn1
        qn1, qn2 = qn, qn1
    return pn + qn, qn


def main():
    term1, term2 = convergents()
    print(term1, term2, sum(map(int, str(term1))))


if __name__ == "__main__":
    main()
