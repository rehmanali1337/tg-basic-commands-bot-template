from telethon.events import CallbackQuery

from telethon_utils import stop_event



async def home(e: CallbackQuery.Event) -> None:
    await e.answer("Working on home ...")

    return stop_event()