from telethon import TelegramClient
from .start import start_command


from telethon import types
from app import Console
from telethon import TelegramClient, events
from telethon_utils.event_filters import private_command
from app.enums import CommandName



COMMAND_HANDLERS_MAP = {CommandName.START: start_command}

async def load_commands(bot: TelegramClient, for_usernames: list[str] = []) -> None:
    user_ids: list[int] = []

    for username in for_usernames:
        try:
            en = await bot.get_entity(username)
            if isinstance(en, types.User):
                user_ids.append(en.id)

        except Exception as e:
            Console.error(f"Failed to get username {username}. {e}", exc_info=True)

    for command, handler in COMMAND_HANDLERS_MAP.items():
        bot.add_event_handler(
            handler,
            events.NewMessage(func=private_command("/" + command, from_users=user_ids)),
        )

    Console.info(f"All commands loaded!")
