#!/usr/bin/env python


def password():
    data = [i.strip() for i in open('data/keylog.txt').readlines()]
    points = {k: {} for k in set(''.join(data))}
    x = ''
    for word in data:
        for i, letter in enumerate(word):
            for j, comp in enumerate(word):
                if letter != comp:
                    points[letter][comp] = j-i
    while points:
        letter = [i for i in points if all(points[j][i] < 0 for j in filter(lambda k: i in points[k], points))]
        if letter:
            letter = min(letter)
            del points[letter]
            for j in filter(lambda k: letter in points[k], points):
                del points[j][letter]
            x += letter

    return x


def main():
    answer = password()
    print(answer)


if __name__ == "__main__":
    main()
