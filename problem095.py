#!/usr/bin/env python


def find_factors(number):
    for i in range(1, number//2 + 1):
        if not number % i:
            yield i


def find_chains(limit=1000000):
    """
        From list http://djm.cc/sociable.txt
        we can stop once we reach 14316 otherwise this takes a LONG time
    """
    numbers, maxchain = set(), set()
    for factor in range(2, limit + 1):

        if factor in numbers:
            continue

        temp, chain, broken = factor, [], False

        while temp not in chain:
            chain.append(temp)
            temp = sum(find_factors(temp))
            if temp > limit or temp in numbers:
                broken = True
                break

        print(chain)

        if not broken and len(chain) - chain.index(temp) > len(maxchain):
            maxchain = chain[chain.index(temp):]

        numbers.update(chain)

    return min(maxchain)


def main():
    smallest_element = find_chains()
    print(smallest_element)


if __name__ == "__main__":
    main()
