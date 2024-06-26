import random

SUITS = ["C", "D", "H", "S"]
VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(suit, value)
        random.shuffle(self.cards)

    