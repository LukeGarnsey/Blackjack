from textual.widgets import Static, Label
from textual.app import ComposeResult
class DealerView(Static):

    def set_model(self, model) -> None:
        self.model = model
        self.mount(Label("I am the view with Data " + self.model.name))

    def on_mount(self) -> None:
        pass
    def compose(self) -> ComposeResult:
        yield Label("I am the dealer!")