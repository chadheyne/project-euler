#!/usr/bin/env python


def square_check(n):
    return n > 0 and (n ** 0.5).is_integer()


def perfect_square():
    """
        x + y = a
        x - y = b
        x + z = c
        x - z = d
        y + z = e
        y - z = f
        ---------
        x = (a + b) / 2 --> must be square
        y = (e + f) / 2
        z = (c - d) / 2
    """
    i = 4
    while True:
        a = i ** 2
        for j in range(3, i):
            c = j ** 2
            f = a - c
            if not square_check(f):
                continue
            k = 1 if j % 2 == 1 else 2
            while k < j:
                d = k ** 2
                e = a - d
                b = c - e
                k += 2
                if not (square_check(e) and square_check(b)):
                    continue
                return (d + c) // 2, (e + f) // 2, (c - d) // 2

        i += 1


def main():
    answer = perfect_square()
    print(answer, sum(answer))


if __name__ == "__main__":
    main()
