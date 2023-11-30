from textual.app import ComposeResult
from card_deck.Deck import DeckBuilder
from blackjack.Dealer import Dealer
from blackjack.Player import Player
from textual.widgets import Static, Button, Label
from .view.GameView import GameView
class Game():
    import time
    def __init__(self) -> None:
        self.deck = DeckBuilder().create_deck()
        self.deck.shuffle()
        self.dealer = Dealer(self.deck)
        self.player = Player(10)
    
    def mount_view(self):
        # self.query_one("#dealer", DealerView).set_model(self.dealer)
        self.view = GameView(id = "gameview")
        self.view.set_model(self)

        self.view.mount(self.dealer.mount_view())

        return self.view
    
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
        print(self.dealer.view_hand(hideDealerCard))
        print("")
        print(self.player.view_hand())
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

from card_deck.Enums import Rank
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