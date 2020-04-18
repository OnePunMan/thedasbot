from .botcommand import BotCommand
from boterror import BotError
from botquery import BotQuery

class HelpCommand(BotCommand):
    def execute(self):
        if self.skip_edited():
            return
        
        self.handle_normal_query("You have invoked the help command!")
