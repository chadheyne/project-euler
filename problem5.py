#!/usr/bin/env python
from itertools import count


def find_products():
    c = count(20, 20)
    cand = next((num for num in c if
                all(num % div == 0 for div in range(1, 21))))
    return cand


def main():
    cand = find_products()
    print(cand)


if __name__ == "__main__":
    main()
