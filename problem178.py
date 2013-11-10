#!/usr/bin/env python
from utils.decorators import timeit


def find_table(height, width=40):
    table = [[0] * (width - 1) + [1] for _ in range(height)]
    for x in range(width - 2, -1, -1):
        for y in range(height):
            table[y][x] += table[y + 1][x + 1] if y + 1 < height else 0
            table[y][x] += table[y - 1][x + 1] if y - 1 >= 0 else 0
    return table


@timeit
def solve_it(size=40):
    table1, table2, table3 = map(find_table, (10, 9, 8))
    s1 = sum(sum(row) for row in table1[:-1])
    s2a = sum(sum(row) for row in table2)
    s2b = s2a - sum(table2[-1])
    s3 = sum(sum(row) for row in table3)

    return (s1 + s3) - (s2a + s2b)


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f} seconds".format(answer, time))

if __name__ == "__main__":
    main()
