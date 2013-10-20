#!/usr/bin/env python


def prime_sequence():
    primes = {int(i) for i in open('data/primes.txt').readlines()
              if len(i.strip()) == 4}
    magical = [num for num in primes
               if num + 3330 in primes and num + 6660 in primes
               and set(str(num)) == set(str(num+3330)) == set(str(num+6660))]
    return magical


def main():
    magic = prime_sequence()
    print(magic)


if __name__ == "__main__":
    main()
