import math


def n_choose(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
