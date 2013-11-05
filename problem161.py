#!/usr/bin/env python
from utils import decorators

def fill_rows(width, a=0, m=0, b=0):
    if width >= 3:
        for (a, m, b) in fill_rows(width - 3, a, m, b):
            a, m, b = a << 3, m << 3, b << 3
            yield (a, m | 0b111, b)

    if width >= 2:
        for (a, m, b) in fill_rows(width - 2, a, m, b):
            a, m, b = a << 2, m << 2, b << 2
            yield (a | 0b10, m | 0b11, b)
            yield (a | 0b01, m | 0b11, b)
            yield (a, m | 0b11, b | 0b10)
            yield (a, m | 0b11, b | 0b01)

    if width >= 1:
        for (a, m, b) in fill_rows(width - 1, a, m, b):
            a, m, b = a << 1, m << 1, b << 1
            yield (a | 0b1, m | 0b1, b | 0b1)
            yield (a, m, b)

    if width == 0:
        yield (a, m, b)


def create_cols(num_cols):
    rows = {}
    for (a, m, b) in fill_rows(num_cols):
        if a in rows:
            rows[a].append((m, b))
        else:
            rows[a] = [(m, b)]
    return rows


def create_rows(num_rows, num_cols, allbits):
    rows = create_cols(num_cols)
    d0 = {(allbits, 0): 1}

    for row in range(num_rows // 2):
        d1 = {}
        for m0, b0 in d0:
            count = d0[m0, b0]
            pairs = rows[m0 ^ allbits]
            for m, b in pairs:
                if b0 & m:
                    continue
                m1, b1 = b0 | m, b
                if (m1, b1) not in d1:
                    d1[m1, b1] = count
                else:
                    d1[m1, b1] += count
        d0 = d1
    return rows, d0


@decorators.timeit
def solve_it(num_rows=12, num_cols=9):
    allbits, count = 2 ** num_cols - 1, 0
    rows, d0 = create_rows(num_rows, num_cols, allbits)
    for m, b in d0:
        bb, mm = allbits ^ m, allbits ^ b
        if (mm, bb) in d0:
            count += d0[m, b] * d0[mm, bb]
    return count


def main():
    answer, time = solve_it(num_rows=12, num_cols=9)
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))

if __name__ == "__main__":
    main()
