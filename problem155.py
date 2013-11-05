#!/usr/bin/env python
import fractions


class fraction:
    def __init__(self, num, den):
        self.gcd = fractions.gcd(num, den)
        self.num = num // self.gcd
        self.den = den // self.gcd

    def __add__(self, other):
        return fraction(self.num * other.den + other.num * self.den,
                        self.den * other.den)

    def add_inv(self, other):
        return fraction(self.num * other.num,
                        self.den * other.num + other.den * self.num)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

    def __hash__(self):
        return self.num * 10000 + self.den


def serial(a, b):
    return a.add_inv(b)


def parallel(a, b):
    return a + b


def find_capacitors(n):
    for k in range(1, n // 2 + 1):
        for p1 in find_capacitors.cache[k]:
            for p2 in find_capacitors.cache[n - k]:
                par_cap = parallel(p1, p2)
                ser_cap = serial(p1, p2)
                if par_cap not in find_capacitors.cache['overall']:
                    find_capacitors.cache[n].append(par_cap)
                    find_capacitors.cache['overall'].add(par_cap)
                if ser_cap not in find_capacitors.cache['overall']:
                    find_capacitors.cache[n].append(ser_cap)
                    find_capacitors.cache['overall'].add(ser_cap)

    return find_capacitors.cache['overall']


find_capacitors.cache = {i: [] for i in range(19)}
find_capacitors.cache[1].append(fraction(1, 1))
find_capacitors.cache['overall'] = set([fraction(1, 1)])


def total_capacitors(total=18):
    for n in range(2, total + 1):
        find_capacitors(n)
        print("{} ------ {}".format(n, len(find_capacitors.cache[n])))
    return len(find_capacitors.cache['overall'])


def main():
    answer = total_capacitors()
    print(answer)


if __name__ == "__main__":
    main()
