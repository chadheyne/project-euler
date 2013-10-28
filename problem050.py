#!/usr/bin/env python
import collections
import functools


class memoized(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        return self.func.__doc__

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


@memoized
def prime_sum(*nums):
    return sum(nums)


def consecutive():
    primes = sorted([int(i) for i in open('data/primes.txt').readlines() if int(i) <= 1000000])
    candidates = set()
    for pos, prime in enumerate(primes):
        for n in range(pos):
            total = prime_sum(*primes[n:pos])
            if total > 1000000:
                break
            if total in primes:
                candidates.add((total, pos-n))
    return candidates


def main():
    candidates = consecutive()
    print(max(candidates, key=lambda i: i[1]))


if __name__ == "__main__":
    main()
