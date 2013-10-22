#!/usr/bin/env python


def power_digits():
    '''
        9 ** 21 is the last number that is equal in length and power
    '''
    for i in range(1, 22):
        j = 1
        while len(str(j ** i)) <= i:
            if len(str(j ** i)) == i:
                yield j, i
            j += 1


def main():
    total = 0
    for j, i in power_digits():
        print(j, i, j ** i)
        total += 1
    print(total)


if __name__ == "__main__":
    main()
