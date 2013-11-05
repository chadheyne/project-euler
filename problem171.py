#!/usr/bin/env python
from utils.decorators import timeit


def find_digits(digits_left, goal):
    if (digits_left, goal) not in find_digits.cache:
        if not digits_left:
            find_digits.cache[(0, goal)] = (goal == 0, 0)
        else:
            count = total = 0
            for start in filter(lambda n: pow(n, 2) <= goal, range(10)):
                subcount, subtotal = find_digits(digits_left - 1, goal - start ** 2)
                count += subcount
                total += subtotal + (start * 10 ** (digits_left - 1)) * subcount
            find_digits.cache[(digits_left, goal)] = (count, total)
    return find_digits.cache[(digits_left, goal)]

find_digits.cache = {}


@timeit
def solve_it():
    return sum(find_digits(20, pow(n, 2))[1] for n in range(40)) % 10 ** 9


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
