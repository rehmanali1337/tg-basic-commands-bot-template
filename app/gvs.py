import os
from warnings import warn

INPUT_DIR = "Input"
OUTPUT_DIR = "Output"

START_DIRS = [INPUT_DIR, OUTPUT_DIR]


for d in START_DIRS:
    os.makedirs(d, exist_ok=True)

# Input Files


TELEGRAM_API_ID = ""
TELEGRAM_API_HASH = ""


if not TELEGRAM_API_HASH or not TELEGRAM_API_HASH:
    warn("Missing Telegram API ID or HASH")

STARTUP_FILES: list[str] = []

for f in STARTUP_FILES:
    if not os.path.exists(f):
        with open(f, "w", encoding="UTF-8") as _:
            pass
