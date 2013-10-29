#!/usr/bin/env python


def fib():
    topa, topb, bota, botb = 1, 1, 1, 1
    while True:
        yield str(botb)[-9:], str(topb)[:9]
        bota, botb = botb, (bota + botb) % 1000000000
        topa, topb = topb, topa + topb
        while topb > 1000000000000000000:
            topa, topb = topa // 10, topb // 10


def pandigital():
    digits, n = set('123456789'), 1
    for top, bot in fib():
        n += 1
        if set(top) == set(bot) == digits:
            return n


def main():
    k = pandigital()
    print(k)


if __name__ == "__main__":
    main()
