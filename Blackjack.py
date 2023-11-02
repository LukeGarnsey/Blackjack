#!/usr/bin/env python
# coding: utf-8

# In[1]:


from enum import Enum

class Suit(Enum):
    Spades = "Sp"
    Clubs = "Cl"
    Hearts = "He"
    Diamonds = "Di"

class Rank(Enum):
    Ace = "A"
    Two = "2"
    Three = "3"
    Four = "4" 
    Five = "5"
    Six = "6" 
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Ten = "10"
    Jack = "J"
    Queen = "Q"
    King = "K"

class RankValues:
    
    def __init__(self) -> None:
        pass

    def get_value(self, ranks):
        count = 0
        aceCount = 0
        for rank in ranks:
            if rank == Rank.Ace:
                aceCount += 1
            elif rank == Rank.King or rank == Rank.Queen or rank == Rank.Jack or rank == Rank.Ten:
                count += 10
            else:
                count += int(rank.value)
        
        while aceCount > 0:
            if aceCount > 1:
                count += 1
                aceCount -= 1
                continue
            if count + 11 > 21:
                count += 1
            else:
                count += 11
                
            aceCount -= 1
        return count
    


# In[2]:


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

        print(toPrint)
    


# In[3]:


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


# In[4]:


class DeckBuilder:

    def __init__(self) -> None:
        pass

    def create_deck(self):
        deck = Deck([])
        for s in Suit:
            for r in Rank:
                deck.add_card(Card(s, r))
        
        return deck


# In[5]:


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

            print(toPrint)
            return
        
        super().view_hand()


# In[6]:


class Game:
    import time
    def __init__(self) -> None:
        self.deck = DeckBuilder().create_deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.player = Player(10)
    def another_hand(self):
        loop = True
        while loop:
            text = input("Play another Hand? (y/n)")
            if text.lower() == "y" or text.lower() == "yes":
                return True
            elif text.lower() == "n" or text.lower() == "no":
                return False
            print("I don't understand")
    def dealer_draw(self, rankValues):
        from IPython.display import clear_output
        dealerNumber = rankValues.get_value(self.dealer.get_ranks())
        while dealerNumber <= 16:
            print("Dealer Draws...")
            self.time.sleep(.5)
            drawn = self.dealer.hit_player(self.dealer)
            print("Dealer gets: {0}".format(drawn.view_card_string()))
            self.time.sleep(1)
            dealerNumber = rankValues.get_value(self.dealer.get_ranks())
            clear_output()
            self.time.sleep(.1)
            self.view_table(False)
            self.time.sleep(1.5)

        if dealerNumber > 16:
            print("Dealer Stands with: {0}".format(dealerNumber))
        self.time.sleep(1.5)
        return dealerNumber
    
    def view_table(self, hideDealerCard):
        print("-----")
        self.dealer.view_hand(hideDealerCard)
        print("")
        self.player.view_hand()
        print("-----")

    def run_game(self):
        from IPython.display import clear_output
        self.game = True
        rankValues = RankValues()
        while self.game:
            # print(str(self.deck.card_count()))
            self.time.sleep(.1)
            clear_output()
            
            self.dealer.request_chips()
            self.bet = self.player.bet()
            print("Bet of " + str(self.bet))
            self.dealer.deal_cards(self.player)
            self.view_table(True)
            playerNumber = rankValues.get_value(self.player.get_ranks())
            blackjack = playerNumber == 21
            self.time.sleep(.5)
            while playerNumber < 21:
                self.time.sleep(.1)
                hitMe = self.player.want_card()
                if hitMe:
                    print("HIT ME")
                    self.time.sleep(.5)
                    drawn = self.dealer.hit_player(self.player)
                    print("Player gets: {0}".format(drawn.view_card_string()))
                    self.time.sleep(1)
                    clear_output() 
                    self.time.sleep(.1)
                    self.view_table(True)
                    playerNumber = rankValues.get_value(self.player.get_ranks())
                    self.time.sleep(1)                    
                else:
                    print("Player stands with {0}".format(rankValues.get_value(self.player.get_ranks())))
                    self.time.sleep(2)
                    clear_output() 
                    self.time.sleep(.1)
                    break
            
            
            win = 0
            if blackjack:
                self.time.sleep(.5)
                clear_output()
                self.time.sleep(.1)
                print("Player has Blackjack!")
                self.view_table(False)
                self.time.sleep(.5)

                if rankValues.get_value(self.dealer.get_ranks()) == 21:
                    win = self.bet
                    print("Push, your bet:{0} is returned".format(self.bet))
                else:
                    win = self.bet * 2 + round(self.bet * .5)
                    print("Blackjack!!! Player Wins:{0}".format(win))
            else:
                if playerNumber > 21:
                    print("Player is Bust.")
                else:
                    self.view_table(False)
                    dealerNumber = self.dealer_draw(rankValues)
                    self.time.sleep(.1)
                    if dealerNumber > 21:
                        win = self.bet * 2
                        print("Dealer Bust, Player Wins: {0}".format(win))
                    elif playerNumber == dealerNumber:
                        win = self.bet
                        print("Push, your bet:{0} is returned".format(self.bet))
                    elif dealerNumber > playerNumber:
                        print("Dealer Wins")
                    else:
                        win = self.bet * 2
                        print("Player Wins:{0}".format(win))
            
            self.player.chips += win
            print("---------------------")
            self.time.sleep(.5)
            print("Player chips:{0}".format(self.player.chip_count()))
            self.time.sleep(.5)
            if self.player.chip_count() <= 0:
                self.game = False
                print("OUT of chips!!!")
                continue
            if self.deck.card_count() < 10:
                self.game = False
                print("ending game with too few cards left.")
                continue
            if not self.another_hand():
                self.game = False
            
            self.dealer.discard_hand()
            self.player.discard_hand()


# In[7]:


game = Game()
game.run_game()

