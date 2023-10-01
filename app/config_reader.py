
import toml

class config:
    

    data = toml.load("config.toml")
    TELEGRAM_API_HASH = data.get("TELEGRAM_API_HASH", '')
    TELEGRAM_API_ID = data.get("TELEGRAM_API_ID", '')
    TELEGRAM_BOT_TOKEN = data.get("TELEGRAM_BOT_TOKEN", '')