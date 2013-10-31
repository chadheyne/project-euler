#!/usr/bin/env python


def digit_power_sum(target=30):
    special_numbers = []
    for base in range(2, 400):
        numbers = [pow(base, exponent) for exponent in range(2, 50)]
        for num in numbers:
            if sum(map(int, str(num))) == base:
                special_numbers.append(num)

    return sorted(special_numbers)[29]


def main():
    answer = digit_power_sum()
    print(answer)

if __name__ == "__main__":
    main()
