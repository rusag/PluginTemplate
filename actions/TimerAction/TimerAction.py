# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase
# Import python modules
import os
import threading
# Import gtk modules - used for the config rows
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class TimerAction(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timer = None
        self.remaining = 0

    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "info.png")
        self.set_media(media_path=icon_path, size=0.75)
        self.set_top_label("45:00")

    def on_key_down(self) -> None:
        if self.timer is not None:
            # Cancel running timer
            self.timer.cancel()
            self.timer = None
            self.remaining = 0
            self.set_top_label("45:00")
            print("Timer cancelled")
            return

        # Start 45 minute timer
        self.remaining = 45 * 60
        print("Timer started: 45 minutes")
        self._tick()

    def on_key_up(self) -> None:
        pass

    def _tick(self) -> None:
        if self.remaining <= 0:
            self._on_finished()
            return

        minutes, seconds = divmod(self.remaining, 60)
        self.set_top_label(f"{minutes:02d}:{seconds:02d}")

        self.remaining -= 1
        self.timer = threading.Timer(1.0, self._tick)
        self.timer.start()

    def _on_finished(self) -> None:
        self.timer = None
        self.set_top_label("DONE")
        print("Timer finished!")
        # Optional: show a checkmark / alert icon
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "info.png")
        self.set_media(media_path=icon_path, size=0.75)
