#!/usr/bin/env python
from collections import Counter

DECK = {
    'H': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'S': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'D': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'C': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
}

straights = ['A2345'] + [''.join(DECK['H'][i:i+5]) for i in range(9)]


def hand_rank(hand):
    position = lambda card: DECK['H'].index(card)
    suits, cards = zip(*hand)

    if len(set(suits)) == 1:
        if ''.join(cards) not in straights:
            return (6, max(position(card) for card in cards), 0)
        elif ''.join(cards) in straights[:-1]:
            if ''.join(cards) == straights[0]:
                return(9, 3)
            return (9, max(position(card) for card in cards), 0)
        else:
            return (10, 0, 0)

    if ''.join(cards) in straights:
        return (5, max(position(card) for card in cards), 0)

    counts = Counter(cards)
    a, b, *c = counts.most_common(5)
    if a[1] == 4:
        return (8, position(a[0]), position(b[0]))
    elif a[1] == 3:
        if not c:
            return (7,  position(a[0]), position(b[0]))
        return (4, position(a[0]), position(b[0]), position(c[0][0]))
    elif a[1] == 2:
        c = c[0]
        if b[1] == 2:
            return (3, position(a[0]), position(b[0]), position(c[0]))
        if position(b[0]) < position(c[0]):
            b, c = c, b
        return (2, position(a[0]), position(b[0]), position(c[0]))
    return (1, max(position(card) for card in cards), 0)


def play_poker(game_file="data/poker.txt"):
    player1, player2 = 0, 0
    with open(game_file) as games:
        for game in games:
            game = game.strip('\n').split(' ')
            hand1, hand2 = game[:5], game[5:]
            hand1 = sorted(tuple((suit, card) for card, suit in hand1), key=lambda i: DECK[i[0]].index(i[1]))
            hand2 = sorted(tuple((suit, card) for card, suit in hand2), key=lambda i: DECK[i[0]].index(i[1]))
            if hand_rank(hand1) > hand_rank(hand2):
                player1 += 1
            elif hand_rank(hand2) > hand_rank(hand1):
                player2 += 1

    return player1, player2


def main():
    player1, player2 = play_poker()
    print(player1, player2)

if __name__ == "__main__":
    main()
