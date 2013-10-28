#!/usr/bin/env python


def generate_spiral(grid_length=1001):
    grid = [[1]]
    num_per_side = 3
    while num_per_side <= grid_length:
        start = max(grid[-1])
        current = list(range(start + 1, num_per_side**2 + 1))
        grid.append(current)
        num_per_side += 2
    return grid


def diagonals():
    grid = generate_spiral(1001)
    for row in grid:
        length = len(row)
        if length == 1:
            yield tuple((1, ))
        else:
            start = length // 4
            yield tuple(row[start-1::start])


def main():
    total = sum(sum(row) for row in diagonals())
    print(total)


if __name__ == "__main__":
    main()
