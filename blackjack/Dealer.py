from card_deck.Hand import Hand

class Dealer(Hand):

    def __init__(self, deck) -> None:
        self.deck = deck
        super().__init__("Dealer")
    
    def deal_cards(self, player):
        self.hit_player(player)
        self.hit_player(self)
        self.hit_player(player)
        self.hit_player(self)

    def hit_player(self, hand):
        card = self.deck.draw_single()
        hand.add_card(card)
        return card

    def request_chips(self):
        print("Dealer: 'I am going to need chips from you...'")
    
    def view_hand(self, hideSecondCard):
        if hideSecondCard and len(self.hand) == 2:
            toPrint = self.name + " Hand: "
            toPrint += self.hand[0].view_card_string()
            toPrint += "|"+"?"+"|"
            return toPrint
        
        super().view_hand()