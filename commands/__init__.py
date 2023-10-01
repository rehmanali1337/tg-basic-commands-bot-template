# pyright: basic
import re
from typing import Any, Callable
from app import logger
from telethon import TelegramClient
from telethon.events import CallbackQuery
from .start import StartCommand


async def load_commands(bot: TelegramClient) -> None:
    # await reset_bot_commands(bot)
    StartCommand(name="/start", description="Start the bot", bot=bot)
