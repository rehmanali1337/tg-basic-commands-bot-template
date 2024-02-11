import os

INPUT_DIR = "Input"
OUTPUT_DIR = "Output"

START_DIRS = [INPUT_DIR, OUTPUT_DIR]


for d in START_DIRS:
    os.makedirs(d, exist_ok=True)

# Input Files


STARTUP_FILES: list[str] = []

for f in STARTUP_FILES:
    if not os.path.exists(f):
        with open(f, "w", encoding="UTF-8") as _:
            pass
