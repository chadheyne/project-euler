#!/usr/bin/env python
from heapq import heapify, heappop, heappush
from utils.decorators import timeit
CLUES = [
        ('5616185650518293', 2),
        ('3847439647293047', 1),
        ('5855462940810587', 3),
        ('9742855507068353', 3),
        ('4296849643607543', 3),
        ('3174248439465858', 1),
        ('4513559094146117', 2),
        ('7890971548908067', 3),
        ('8157356344118483', 1),
        ('2615250744386899', 2),
        ('8690095851526254', 3),
        ('6375711915077050', 1),
        ('6913859173121360', 1),
        ('6442889055042768', 2),
        ('2321386104303845', 0),
        ('2326509471271448', 2),
        ('5251583379644322', 2),
        ('1748270476758276', 3),
        ('4895722652190306', 1),
        ('3041631117224635', 3),
        ('1841236454324589', 3),
        ('2659862637316867', 2)
        ]
NUMS, STATE = "0123456789", "0" * 16


def cost(state):
    c = 0
    for e, numcorrect in CLUES:
        n = sum(x == y for x, y in zip(e, state))
        c += abs(n - numcorrect)
    return c


def find_next(state):
    for i in range(len(state)):
        for c in NUMS.replace(state[i], ''):
            yield state[:i] + c + state[i + 1:]


@timeit
def solve_it():
    candidates = [(cost(STATE), STATE)]
    heapify(candidates)
    best, num_cand, seen = 1000, 0, set(candidates)
    while True:
        candidate, state = heappop(candidates)
        if candidate < best:
            best = candidate
        if not candidate:
            break
        if len(candidates) - num_cand > 10000:
            num_cand = len(candidates)
        for new_state in find_next(state):
            if new_state not in seen:
                heappush(candidates, (cost(new_state), new_state))
                seen.add(new_state)
    return state, best


def main():
    answer, time = solve_it()
    print("Solution is --- {}\nRunning time --- {:2.2f}".format(answer, time))


if __name__ == "__main__":
    main()
