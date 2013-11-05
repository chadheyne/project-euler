import time


def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()

        print("{} ({}, {}) {:2.2f} seconds".format(method.__name__, args, kwargs, te-ts))
        return result, te - ts
    return timed
