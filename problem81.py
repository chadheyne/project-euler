#!/usr/bin/env python


def path_traverse():
    graph = [[int(i) for i in row.strip().split(',')] for row in open('data/matrix.txt').readlines()]
    for y in range(len(graph) - 1, -1, -1):
        for x in range(len(graph) - 1, -1, -1):
            if y == x == len(graph) - 1:
                continue
            if x == len(graph) - 1:
                next_step = graph[y+1][x]
            elif y == len(graph) - 1:
                next_step = graph[y][x+1]
            else:
                next_step = min(graph[y][x+1], graph[y+1][x])
            graph[y][x] += next_step
    return graph[0][0]


def main():
    shortest_path = path_traverse()
    print(shortest_path)

if __name__ == "__main__":
    main()
