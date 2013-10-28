#!/usr/bin/env python


def cross(lista, listb):
    return [a + b for a in lista for b in listb]


COLS = DIGITS = '123456789'
ROWS = 'ABCDEFGHI'
SQUARES = cross(ROWS, COLS)
UNITLIST = ([cross(ROWS, c) for c in COLS] +
            [cross(r, COLS) for r in ROWS] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
UNITS = dict((s, [u for u in UNITLIST if s in u])
             for s in SQUARES)
PEERS = dict((s, set(sum(UNITS[s], [])) - set([s]))
             for s in SQUARES)


def grid_values(grid):
    chars = [c for c in grid if c in DIGITS or c in ('0', '.')]
    return dict(zip(SQUARES, chars))


def parse_grid(grid):
    values = dict((s, DIGITS) for s in SQUARES)
    for s, d in grid_values(grid).items():
        if d in DIGITS and not assign(values, s, d):
            return False
    return values


def eliminate(values, square, digit):
    if digit not in values[square]:
        return values
    values[square] = values[square].replace(digit, '')
    if len(values[square]) == 0:
        return False
    elif len(values[square]) == 1:
        digit2 = values[square]
        if not (all(eliminate(values, square2, digit2)
                for square2 in PEERS[square])):
            return False
    for u in UNITS[square]:
        dplaces = [s for s in u if digit in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], digit):
                return False
    return values


def assign(values, square, digit):
    other_values = values[square].replace(digit, '')
    if all(eliminate(values, square, digit2) for digit2 in other_values):
        return values
    return False


def some(seq):
    for el in seq:
        if el:
            return el
    return False


def search(values):
    if values is False:
        return False
    elif all(len(values[s]) == 1 for s in SQUARES):
        return values
    n, s = min((len(values[s]), s) for s in SQUARES if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
            for d in values[s])


def solve(grid):
    return search(parse_grid(grid))


def read_file(data='data/sudoku.txt'):
    with open(data) as grids:
        lines = [line.strip() for line in grids]
        puzzles = [''.join(lines[i+1:i+10]) for i in range(0, len(lines), 10)]
    return puzzles


def solve_from_file(data='data/sudoku.txt'):
    puzzles, solved = read_file(data), {}
    for i, puzzle in enumerate(puzzles):
        solved[i] = solve(puzzle)
    return solved


def main():
    solved = solve_from_file()
    reduced = [''.join((puzzle['A1'], puzzle['A2'], puzzle['A3']))
               for puzzle in solved.values()]
    answer = sum(int(row) for row in reduced)
    print(answer)


if __name__ == "__main__":
    main()
