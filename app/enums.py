from telethon_utils.buttons import data_button
from telethon_utils.emojis import Emojis
from telethon.types import KeyboardButtonCallback



class ButtonName:
    HOME = f"{Emojis.CHECK} Home"




class ButtonDataPrefix:
    HOME = "home"



class CommonDataButtons:

    @classmethod
    def home(cls) -> KeyboardButtonCallback:
        return data_button(ButtonName.HOME, ButtonDataPrefix.HOME)




class CommandName:

    START = "start"