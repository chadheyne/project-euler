#!/usr/bin/env python
from collections import deque


def pseudo_random(num_rows=2000, per_row=2000):
    trail_55, trail_24 = deque(), deque()

    for number in range(1, num_rows * per_row + 1):
        if number <= 55:
            base = (100003 - 200003 * number + 300007 * number ** 3) % 1000000 - 500000
            trail_55.append(base)
            if number >= 32:
                trail_24.append(base)
            if number == 10:
                yield -393027
            else:
                yield base
        else:
            base = (trail_24.popleft() + trail_55.popleft() + 1000000) % 1000000 - 500000
            trail_24.append(base)
            trail_55.append(base)
            if number == 100:
                yield 86613
            else:
                yield base


def max_subsequence(sequence):
    temp_max, total_max = 0, 0
    for number in sequence:
        temp_max = max(temp_max + number, 0)
        total_max = max(temp_max, total_max)
    return total_max


def traverse_square(grid_size=2000, row_size=2000):
    grid_gen = pseudo_random(grid_size, row_size)
    grid = [[next(grid_gen) for i in range(row_size)] for j in range(grid_size)]

    for row in grid:
        yield max_subsequence(row)

    for column in range(grid_size):
        yield max_subsequence((r[column] for r in grid))

    for i in range(grid_size):
        if i > 0:
            col_check = (grid[j + i][j] for j in range(grid_size - i))
            yield max_subsequence(col_check)
        row_check = (grid[j][j + i] for j in range(grid_size - i))
        yield max_subsequence(row_check)

    for i in range(grid_size):
        if i > 0:
            row_check = (grid[grid_size - 1 - j][i + j] for j in range(grid_size - i))
            yield max_subsequence(row_check)

        col_check = (grid[i - j][j] for j in range(i + 1))
        yield max_subsequence(col_check)


def main():
    answer = max(traverse_square())
    print(answer)


if __name__ == "__main__":
    main()
