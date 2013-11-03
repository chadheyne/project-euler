#!/usr/bin/env python


def pseudo_random(num_draws=500500):
    t = 0
    for row in range(1, num_draws + 1):
        t = (615949 * t + 797807) % pow(2, 20)
        yield t - pow(2, 19)


def triangular(num_rows=1000):
    per_row, numbers = 1, pseudo_random()
    for row in range(num_rows):
        yield [next(numbers) for i in range(per_row)]
        per_row += 1


def minimal_sum():
    triangle = list(triangular())
    row_sums = []

    for row in triangle:
        temp = [0]
        for number in row:
            temp.append(temp[-1] + number)
        row_sums.append(temp)

    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            current = 0
            for k in range(i, len(triangle)):
                current += row_sums[k][k - i + 1 + j] - row_sums[k][j]
                yield current


def main():
    answer = min(minimal_sum())
    print(answer)


if __name__ == "__main__":
    main()
