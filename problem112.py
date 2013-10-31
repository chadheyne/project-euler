#!/usr/bin/env python


def is_bouncy(number):
    return not (sorted(str(number)) == list(str(number)) or
                sorted(str(number), reverse=True) == list(str(number)))


def count_bouncy(proportion=99):
    bouncy, total, number = 19602, 21780, 21781
    while bouncy * 100 < proportion * total:
        if is_bouncy(number):
            bouncy += 1
        total, number = total + 1, number + 1

    return total


def main():
    answer = count_bouncy()
    print(answer)


if __name__ == "__main__":
    main()
