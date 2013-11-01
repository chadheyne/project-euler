#!/usr/bin/env python


def same_differences(limit=1000000):
    results = {i: 0 for i in range(3, limit + 1)}
    for u in range(1, limit+1):
        v = 1
        while u * v <= limit:
            if not ((u + v) % 4 and (3 * v - u) % 4) and 3 * v > u:
                results[u * v] += 1
            v += 1

    return sum(1 for n in results if results[n] == 10)


def main():
    answer = same_differences()
    print(answer)


if __name__ == "__main__":
    main()
