#!/usr/bin/env python


def self_powers(series=1000):
    return sum(pow(num, num) for num in range(1, series+1))


def main():
    last_ten = str(self_powers(1000))[-10:]
    print(last_ten)

if __name__ == "__main__":
    main()
