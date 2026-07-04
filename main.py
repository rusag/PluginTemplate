# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.SimpleAction.SimpleAction import SimpleAction
from .actions.TimerAction.TimerAction import TimerAction
from .actions.TeamsAction.AvafinTeams import AvafinTeams
from .actions.counter.counter import Counter

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.simple_action_holder = ActionHolder(
            plugin_base = self,
            action_base = SimpleAction,
            action_id = "dev_core447_Template::SimpleAction", # Change this to your own plugin id
            action_name = "Simple Action",
        )
        self.add_action_holder(self.simple_action_holder)

        self.counter_action_holder = ActionHolder(
            plugin_base = self,
            action_base = Counter,
            action_id = "dev_core447_Template::Counter", # Change this to your own plugin id
            action_name = "Counter",
        )
        self.add_action_holder(self.counter_action_holder)

        self.timer_action_holder = ActionHolder(
            plugin_base = self,
            action_base = TimerAction,
            action_id = "dev_core447_Template::TimerAction", # Change this to your own plugin id
            action_name = "45 Min Timer",
        )
        self.add_action_holder(self.timer_action_holder)

        self.avafin_teams_action_holder = ActionHolder(
            plugin_base = self,
            action_base = AvafinTeams,
            action_id = "dev_core447_Template::AvafinTeams", # Change this to your own plugin id
            action_name = "Avafin Teams",
        )
        self.add_action_holder(self.avafin_teams_action_holder)

        # Register plugin
        self.register(
            plugin_name = "Template",
            github_repo = "https://github.com/rusag/PluginTemplate",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )
