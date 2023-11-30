from textual.app import ComposeResult
from card_deck.Deck import DeckBuilder
from blackjack.Dealer import  Dealer, DealerView
from blackjack.Player import Player
from textual.widgets import Static, Button, Label

class GameView(Static):
    def set_model(self, model) -> None:
        self.model = model
    def on_mount(self) -> None:
        # self.query_one("#dealer", DealerView).set_model(self.dealer)
        pass

    def compose(self) -> ComposeResult:
        yield Label("You are playing blackjack", id="gameviewlabel")