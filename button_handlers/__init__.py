# pyright: basic
from typing import Callable, Coroutine
from app import Console
from telethon import TelegramClient, events
from telethon_utils import event_filters
from app.enums import ButtonDataPrefix
from . import home


DATA_BUTTON_HANDLERS_MAP: dict[str, Callable[[events.CallbackQuery.Event], Coroutine[None, None, None]]] = {
    ButtonDataPrefix.HOME: home.home
}


async def setup_data_button_handlers(bot: TelegramClient) -> None:
    for data_starts_with, handler in DATA_BUTTON_HANDLERS_MAP.items():
        bot.add_event_handler(
            handler,
            events.CallbackQuery(
                func=event_filters.query_data_starts_with(data_starts_with)
            ),
        )  # pyright: ignore
    Console.info("Data Button handlers loaded!")
