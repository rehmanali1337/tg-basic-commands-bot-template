from telethon.events import NewMessage
from app.enums import CommonDataButtons
from telethon_utils.converters import message_ev_to_custom_message_ob
from telethon_utils import stop_event
import text


async def start_command(e: NewMessage.Event) -> None:

    message = message_ev_to_custom_message_ob(e)

    await message.respond(text.START_COMMAND_TEXT, buttons=[CommonDataButtons.home()])

    print(e.stringify())
    return stop_event()
