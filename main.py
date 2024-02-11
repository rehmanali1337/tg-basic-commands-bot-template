import asyncio
from app import Console

# from app_db.message import Message
from telethon import TelegramClient  # pyright: ignore [reportMissingTypeStubs]
from button_handlers import setup_data_button_handlers
from app.config_reader import config
from commands import load_commands


async def main() -> None:
    bot = TelegramClient("bot", api_id=int(config.TELEGRAM_API_ID), api_hash=config.TELEGRAM_API_HASH)
    bot.parse_mode = "md"   # pyright: ignore

    await bot.start(bot_token=config.TELEGRAM_BOT_TOKEN)  # pyright: ignore
    Console.info("Bot started!")

    await load_commands(bot)
    await setup_data_button_handlers(bot)


if __name__ == "__main__":
    try:
        loop = asyncio.new_event_loop()
        loop.create_task(main())
        loop.run_forever()

    except (Exception, RuntimeError) as e:
        Console.info(f"ERROR: {e}", exc_info=True, shutdown=True)
