import time
from functools import wraps


def timeit(method=None, noprint=False):
    def timeit_wrapper(method):
        @wraps(method)
        def timed(*args, **kwargs):
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            if not noprint:
                print("{} ({}, {}) {:2.2f} seconds".format(method.__name__, args, kwargs, te-ts))
            return result, te - ts
        return timed
    if not method:
        def waiting_for_func(method):
            return timeit_wrapper(method)
        return waiting_for_func
    else:
        return timeit_wrapper(method)
