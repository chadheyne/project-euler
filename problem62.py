#!/usr/bin/env python
from collections import Counter, defaultdict


def cubic(n=345):
    while True:
        yield n, n ** 3
        n += 1


def cubic_perm():
    cubes, cube_gen = Counter(), cubic()
    seen = defaultdict(list)

    for n, cube in cube_gen:
        cube_str = ''.join(sorted(str(cube)))
        cubes[cube_str] += 1
        seen[cube_str].append(cube)
        if cubes.most_common(1)[0][1] == 5:
            return cubes[cube_str], seen[cube_str]


def main():
    answer = cubic_perm()
    print(answer)


if __name__ == "__main__":
    main()
