# pyright: basic
import re
from typing import Any, Callable
from app import logger
from telethon import TelegramClient
from telethon.events import CallbackQuery


async def setup_event_handlers(bot: TelegramClient) -> None:
    logger.debug("Event handlers loaded")
