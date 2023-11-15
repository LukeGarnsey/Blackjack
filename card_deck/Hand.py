class Hand:

    def __init__(self, name) -> None:
        self.hand = []
        self.name = name

    def add_cards(self, cards):
        self.hand.extend(cards)
        
    def add_card(self, card):
        self.hand.append(card)
    
    def remove_card(self, card):
        self.hand.remove(card)
    
    def discard_hand(self):
        self.hand.clear()

    def get_ranks(self):
        ranks = []
        for card in self.hand:
            ranks.append(card.get_rank())

        return ranks
    def view_hand(self):
        toPrint = self.name + " Hand: "
        for card in self.hand:
            toPrint += card.view_card_string()

        
        return toPrint