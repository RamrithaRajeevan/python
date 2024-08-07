# ceate class DeckOfCards with method to initialize a deck(52 cards),shuffle the deck and deal a card(removing it from deck)

import random

class DeckOfCards:
    def __init__(self):
        self.deck = []
        self.initialize_deck()
    
    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [f'{value} of {suit}' for suit in suits for value in values]
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        if not self.deck:
            return "No cards left in the deck"
        return self.deck.pop()

deck = DeckOfCards()
print(f"Initial deck (first 6 cards): {deck.deck[:6]}") 

deck.shuffle_deck()
print(f"Shuffled deck (first 6 cards): {deck.deck[:6]}")

card = deck.deal_card()
print(f"Dealt card: {card}")
print(f"Remaining cards in deck: {len(deck.deck)}")
