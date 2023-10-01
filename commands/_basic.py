# pyright: basic
import os
from telethon import TelegramClient
from telethon.tl.custom import Message
from telethon.events import NewMessage
from telethon import TelegramClient, functions, types

from app import Console


class CommandBase:
    def __init__(self, name: str, description: str, bot: TelegramClient) -> None:
        self.name: str = name
        self.description: str = description
        assert self.name and self.description
        self.bot = bot
        self.bot.add_event_handler(self.handler, NewMessage(incoming=True, pattern=self.name))

        self.resp: Message

    async def handler(self, e: Message) -> None:
        Console.info(f"Using {self.name} command.")

    async def upload(self) -> None:
        result = await self.bot(
            functions.bots.SetBotCommandsRequest(
                scope=types.BotCommandScopeDefault(),
                lang_code="en",
                commands=[types.BotCommand(command=self.name, description=self.description)],
            )
        )
        print(result)

    def remove_file(self, filename: str) -> None:
        try:
            os.remove(filename)

        except Exception:
            pass
