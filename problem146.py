#!/usr/bin/env python
from multiprocessing import Pool


def calculate(func, args):
    return sum(func(*args))


def sieve(n):
    marked = [i % 2 for i in range(n)]
    marked[1] = 0
    marked[2] = 1
    for value in range(3, n, 2):
        if marked[value] == 1:
            for i in range(value*3, n, value*2):
                marked[i] = 0
    return marked


PRIMES = [number for number, i in enumerate(sieve(150000000)) if i]


def probable_prime(number, good_checks, bad_checks):
    for prime in PRIMES:
        if prime > number:
            break
        sq_number = (number % prime) ** 2
        for check in good_checks:
            if not (sq_number + check) % prime:
                return False
    sq_number = number ** 2
    for check in bad_checks:
        check_num = sq_number + check
        flag = False
        for prime in PRIMES[2:]:
            if prime > number:
                break
            if not check_num % prime:
                flag = True
                break
    return False if not flag else True


def check_primality(number, additional, bad):
    return probable_prime(number, additional, bad)


def generate_number(start, limit):
    additional, bad_additional = (1, 3, 7, 9, 13, 27), (19, 21)
    for number in range(start, limit + 1, 10):
        if pow(number, 2, 3) != 1 and pow(number, 2, 7) not in (2, 3):
            continue
        if not all(pow(number, 2, i) for i in (9, 13, 27)):
            continue
        if not check_primality(number, additional, bad_additional):
            continue
        yield number


def find_primes(limit=150000000):
    yield 10
    pool = Pool()
    step = 1000000

    tasks = [(generate_number, (start, start + step)) for start in range(10, limit, step)]

    results = [pool.apply_async(calculate, task) for task in tasks]
    for r in results:
        yield r.get()


def main():
    answer = sum(find_primes())
    print(answer)


if __name__ == "__main__":
    main()
