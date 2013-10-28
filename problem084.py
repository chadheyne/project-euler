#!/usr/bin/env python
from random import randint


def monopoly(iterations=1000000):
    board = {i: 0 for i in range(40)}
    chances = [0, 10, 11, 24, 39, 5]
    chest = [0, 10]
    chance = lambda: randint(1, 16)
    move = lambda: (randint(1, 4), randint(1, 4))
    next_rail = lambda position: (5 if position < 5 or position >= 35 else
                                  15 if position < 15 else
                                  25 if position < 25 else
                                  35)
    next_utility = lambda position: (12 if position < 12 or position >= 28
                                     else 28)

    double, player, jail = 0, 0, 10

    for _ in range(iterations):
        x, y = move()
        if x == y:
            double += 1
            if double == 3:
                player = jail
        else:
            double = 0
            player = (player + x + y)
            player %= 40

        if player in (7, 22, 36):
            roll_the_dice = chance()
            if roll_the_dice <= 6:
                player = chances[roll_the_dice - 1]
            elif roll_the_dice in (7, 8):
                player = next_rail(player)
            elif roll_the_dice == 9:
                player = next_utility(player)
            elif roll_the_dice == 10:
                player -= 3
                player %= 40

        if player in (2, 17, 33):
            roll_the_dice = chance()
            if roll_the_dice <= 2:
                player = chest[roll_the_dice - 1]
        if player == 30:
            player = jail

        board[player] += 1
    return board


def main():
    most_frequent = monopoly()
    three_common = sorted(most_frequent, key=most_frequent.get, reverse=True)[:3]
    print(three_common)


if __name__ == "__main__":
    main()
