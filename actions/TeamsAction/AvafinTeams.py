# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase
# Import python modules
import os
import subprocess
# Import gtk modules
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw


class AvafinTeams(ActionBase):
    TEAMS_URL = "https://teams.microsoft.com"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_ready(self) -> None:
        icon_path = os.path.join(self.plugin_base.PATH, "assets", "info.png")
        self.set_media(media_path=icon_path, size=0.75)
        self.set_top_label("Teams")

    def on_key_down(self) -> None:
            try:
                subprocess.Popen([
                    "flatpak-spawn", "--host",
                    "--directory=/home/neo",
                    "/snap/bin/chromium", "--new-window", self.TEAMS_URL
                ])
                print("Launched Chromium -> Teams")
            except Exception as e:
                print(f"Failed to launch Chromium: {e}")

    def on_key_up(self) -> None:
        pass