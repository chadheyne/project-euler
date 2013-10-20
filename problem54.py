#!/usr/bin/env python
DECK = {
    'H': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'S': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'D': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'),
    'C': ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
}


def hand_rank(hand):
    suits, cards = zip(*hand)
    if len(set(suits)) == 1:
        if DECK[suits[0]]

def main():
    pass

if __name__ == "__main__":
    main()
