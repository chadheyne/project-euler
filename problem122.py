#!/usr/bin/env python


def backtrack(power, depth, limit=200, COSTS={}, PATH={}):
    """
        Backtracking algorithm to create a tree of minimal
        multiplications to generate n ** i for i in (1, 200)
    """
    if power > limit or depth > COSTS[power]:
        return
    COSTS[power], PATH[depth] = depth, power
    for _power in range(depth, -1, -1):
        backtrack(power + PATH[_power], depth + 1, limit, COSTS, PATH)


def efficient_exponentiation(limit=200):
    COSTS = {i: 999999 for i in range(1, limit+1)}
    PATH = {i: 0 for i in range(0, limit+1)}

    backtrack(1, 0, limit, COSTS, PATH)

    return sum(v for k, v in COSTS.items())


def main():
    answer = efficient_exponentiation()
    print(answer)


if __name__ == "__main__":
    main()
