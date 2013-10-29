#!/usr/bin/env python
import heapq


def make_graph(data):
    with open(data) as f:
        vertices = {i: {} for i in range(40)}
        for i, line in enumerate(f):
            vertices[i] = {j: int(el) if el != '-' else 0
                           for j, el in enumerate(line.strip().split(','))}
    return vertices


def prims(data='data/network.txt'):
    graph = make_graph(data)
    connections = {i: [] for i in range(40)}
    mst, used, total_cost = [], {0}, sum(v2 for k, v in graph.items() for v2 in v.values())
    for vertex, connected in graph.items():
        connections[vertex] = [(cost, vertex, other) for other, cost in connected.items() if cost]

    usable_edges = connections[0][:]
    heapq.heapify(usable_edges)

    while usable_edges:
        cost, pt1, pt2 = heapq.heappop(usable_edges)
        if pt2 not in used:
            used.add(pt2)
            mst.append((pt1, pt2, cost))

            for other in connections[pt2]:
                if other[2] not in used:
                    heapq.heappush(usable_edges, other)

    return total_cost // 2 - sum(i[2] for i in mst)


def main():
    answer = prims()
    print(answer)

if __name__ == "__main__":
    main()
