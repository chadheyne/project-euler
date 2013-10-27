#!/usr/bin/env python


SQUARES = {str(c): c ** 2 for c in range(10)}


def chain_loop(number):
    while number not in (1, 89):
        number = sum(SQUARES[i] for i in str(number))
    return number


def square_chains(highest=10000000):
    chains = {}
    for i in range(1, highest+1):
        chains[i] = chain_loop(i)

    return dict(filter(lambda i: i[1] == 89, chains.items()))


def main():
    numbers = square_chains()
    print(len(numbers))


if __name__ == "__main__":
    main()
