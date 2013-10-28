#!/usr/bin/env python


def shortest_path(data='data/matrix.txt'):
    graph = [[int(i) for i in row.strip().split(',')] for row in open(data).readlines()]
    costs = [row[0] for row in graph]

    for column in range(1, len(graph)):
        for row in range(len(graph)):
            costs[row] = min(costs[row], costs[row-1]) + graph[row][column]
        for row in range(len(graph) - 2, -1, -1):
            costs[row] = min(costs[row], costs[row+1] + graph[row][column])

    return min(costs)


def main():
    shortest = shortest_path()
    print(shortest)


if __name__ == "__main__":
    main()
