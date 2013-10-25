#!/usr/bin/env python
from collections import defaultdict
import heapq


VALID_MOVES = lambda x, y: ((x+1, y), (x-1, y), (x, y+1), (x, y-1))


def generate_graph(data='data/matrix.txt'):
    graph = defaultdict(dict)
    data = [[int(i) for i in row.strip().split(',')] for row in open(data).readlines()]
    for i, row in enumerate(data):
        for j, entry in enumerate(row):
            for x, y in VALID_MOVES(i, j):
                if 0 <= x < len(row) and 0 <= y < len(row):
                    cost = data[x][y]
                    graph[(i, j)][(x, y)] = cost

    return graph, data[0][0]


def djikstra(graph, start, end, starting_cost=0):
    queue, visited = [(starting_cost, start, ())], set()
    while True:
        cost, vertex, path = heapq.heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == end:
                return cost
            path = (vertex, ) + path
            for (vertex2, cost2) in graph[vertex].items():
                if vertex2 not in visited:
                    heapq.heappush(queue, (cost + cost2, vertex2, path))


def main():
    graph, start_cost = generate_graph()
    distance = djikstra(graph, min(graph), max(graph), start_cost)
    print(distance)


if __name__ == "__main__":
    main()
