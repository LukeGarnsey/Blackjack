from card_deck.Hand import Hand

class Player(Hand):

    def __init__(self, startingChips) -> None:
        self.chips = startingChips
        super().__init__("Player")

    def print_chips(self):
        print("Chips: " + str(self.chips))
    
    def chip_count(self):
        return self.chips
    def bet(self):
        input_text = ""
        while(input_text == ""):
            input_text = input("Chips: ({0}) |Bet Amount: ".format(self.chips))
            if input_text.isdigit():
                val = int(input_text)
                if 0 < val <= self.chips:
                    self.chips -= val
                    return val
            
            input_text = ""

    def want_card(self):
        input_text = input("Want Card? _enter 'hit' for card_")
        print(input_text)
        if input_text.lower() == "hit":
            return True
        
        return False