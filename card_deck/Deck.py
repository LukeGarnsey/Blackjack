import random
class Deck:
   
    def __init__(self, cards) -> None:
        self.cards = cards
        self.drawnCards = []
    
    def __str__(self):
        return str(len(self.cards)) + " : " + str(len(self.drawnCards))
    
    def card_count(self):
        return len(self.cards)
    
    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_single(self):
        c = self.cards.pop()
        self.drawnCards.append(c)
        return c

    def draw(self, amount):
        drawnCards = []
        for _ in range(amount):
           drawnCards.append(self.cards.pop())
        
        self.drawnCards.extend(drawnCards)
        return drawnCards
    
    def place_cards_on_top_of_deck(self, cards):
        self.cards.extend(cards)
        for c in cards:
            self.drawnCards.remove(c)
    
    def place_cards_on_bottom_of_deck(self, cards):
        for c in cards:
            self.cards.insert(0, c)
            self.drawnCards.remove(c)
        
    def reclaim_drawn_cards(self):
        self.cards.extend(self.drawnCards)
        self.drawnCards.clear()

from .Enums import Suit
from .Enums import Rank
from .Card import Card
class DeckBuilder:

    def __init__(self) -> None:
        pass

    def create_deck(self):
        deck = Deck([])
        for s in Suit:
            for r in Rank:
                deck.add_card(Card(s, r))
        
        return deck