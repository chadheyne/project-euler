#!/usr/bin/env python
from utils.decorators import timeit

MAX_DIGITS = 100
LASTDIGITS = 5


def rotate_digits(lastdigit, multiple):
    s, nextdigit, carry = '', lastdigit, 0
    while len(s) < MAX_DIGITS:
        s = str(nextdigit) + s
        term = nextdigit * multiple + carry
        carry, nextdigit = divmod(term, 10)
        if not carry and nextdigit == lastdigit:
            return s
    return None


def sum_answers(s):
    strlen_s = len(s)
    answers = [(s * (strlen_a // strlen_s))[-LASTDIGITS:]
               for strlen_a in range(strlen_s, MAX_DIGITS+1, strlen_s)]
    return sum(int(a) for a in answers if int(a) > 10)


@timeit
def solve_it(limit=10):
    total = 0
    for multiple in range(1, limit):
        for lastdigit in range(1, limit):
            s = rotate_digits(lastdigit, multiple)
            if s and s[0] != '0':
                total += sum_answers(s)
    return total % 100000


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
