# pyright: basic
from telethon.tl.custom import Message

from ._basic import CommandBase


class StartCommand(CommandBase):
    async def handler(self, e: Message) -> None:
        await super().handler(e)
