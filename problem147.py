#!/usr/bin/env python
from itertools import product


def calculate_trivial(board):
    board_x, board_y = board
    for size_x in range(1, board_x + 1):
        for size_y in range(1, board_y + 1):
            yield (board_x - (size_x - 1)) * (board_y - (size_y - 1))


def calculate_diagonal(board):
    longest, shortest = max(board), min(board)
    yield ((2 * longest - shortest) * (4 * shortest ** 2 - 1) - 3) * shortest // 6


def find_total(board_max=(47, 43)):
    max_x, max_y = board_max
    for board in product(range(1, max_x + 1), range(1, max_y + 1)):
        yield from calculate_diagonal(board)
        yield from calculate_trivial(board)


def main():
    answer = sum(find_total())
    print(answer)


if __name__ == "__main__":
    main()
