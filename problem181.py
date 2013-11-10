#!/usr/bin/env python
from utils.decorators import timeit


@timeit
def solve_it(BLACK=60, WHITE=40):
    groups = [(b, w) for b in range(BLACK + 1) for w in range(WHITE + 1)]
    counts = dict((g, 0) for g in groups)
    counts[0, 0] = 1
    for groupmax in groups[1:]:
        blackmax, whitemax = groupmax
        for group in groups[-1:0:-1]:
            black_init, white_init = black, white = group
            while True:
                black, white = black - blackmax, white - whitemax
                if black < 0 or white < 0:
                    break
                counts[black_init, white_init] += counts[black, white]
    return counts[BLACK, WHITE]


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
