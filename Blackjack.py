from blackjack.Game import Game
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label, Static
from textual.containers import Container

from blackjack.view.GameView import GameView

class SelectGameApp(App):
    CSS_PATH = "Blackjack.tcss" 

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "play":
            event.button.parent.remove()
            self.active_game = Game()
            self.mount(self.active_game.mount_view())
            
            self.mount(Label(str(self.query_one("#dealer", Static).parent.name)))
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(Button("BLACKJACK", id="play"))


game = SelectGameApp()
game.run()

