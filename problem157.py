#!/usr/bin/env python
from utils import decorators


def count_divisors(number):
    output = 2
    for factor in range(2, int(number ** 0.5) + 1):
        if not number % factor:
            output += 1
            if number // factor != factor:
                output += 1
    return output


@decorators.timeit
def total_solutions(max_n=9):
    answer = 0
    for number in range(1, max_n + 1):
        multiple_ten = pow(10, number)
        for power_two in range(number + 1):
            for power_five in range(number + 1):
                a, b = pow(2, power_two), pow(5, power_five)
                if a > b:
                    a, b = b, a
                if a != 1:
                    cases = [(a, b), (1, a * b)]
                else:
                    cases = [(a, b)]

                for a, b in cases:
                    p = multiple_ten * (a + b) // a // b
                    answer += count_divisors(p)
    return answer


def main():
    answer, time = total_solutions()
    print("Solution is --- {}\nRunning time --- {}".format(answer, time))


if __name__ == "__main__":
    main()
