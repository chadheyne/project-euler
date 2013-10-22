#!/usr/bin/env python


def triangle_solver():
    TRIANGLE = open('data/triangle.txt').read()
    triangle = [[int(i) for i in row.split(' ')] for row in TRIANGLE.strip().split('\n')]

    for i, j in [(i, j) for i in range(len(triangle)-2, -1, -1) for j in range(i+1)]:
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    return triangle[0]


def main():
    triangle = triangle_solver()
    print(triangle[0])


if __name__ == "__main__":
    main()
