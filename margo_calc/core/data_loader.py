from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

ALL_JSON_DATA = {}
for file_path in DATA_DIR.glob("*.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        key = file_path.stem
        ALL_JSON_DATA[key] = json.load(f)