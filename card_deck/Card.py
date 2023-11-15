class Card:

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + " of " + str(self.suit)

    def get_rank(self):
        return self.rank

    def view_card_string(self):
        return "|"+self.rank.value  + "|"# " + self.suit.value + "|"