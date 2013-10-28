#!/usr/bin/env python


def solve_large_prime():
    coefficient, base, power = 28433, 2, 7830457
    modulus = 10000000000
    answer = (coefficient * pow(base, power, modulus) + 1) % modulus
    return answer


def main():
    answer = solve_large_prime()
    print(answer)


if __name__ == "__main__":
    main()
