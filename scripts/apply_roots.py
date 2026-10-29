# -*- coding: utf-8 -*-
"""把 roots_data.ROOTS 寫入詞庫，並回填既有的每日 JSON（words 與 reviewWords）與 latest.json。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from roots_data import ROOTS

NOTES_DIR = Path(__file__).resolve().parents[1] / "多益高頻單字"
BANK_PATH = NOTES_DIR / "vocabulary-bank.json"
DATA_DIR = NOTES_DIR / "data"


def dump(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    by_word = {w["word"]: w for w in bank["words"]}

    missing = [word for word in ROOTS if word not in by_word]
    for word, roots in ROOTS.items():
        if word in by_word:
            by_word[word]["roots"] = roots
    dump(BANK_PATH, bank)
    print(f"詞庫已寫入 roots：{len(ROOTS) - len(missing)} 字；詞庫中找不到：{missing}")

    for path in sorted(DATA_DIR.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        touched = 0
        for key in ("words", "newWords", "reviewWords"):
            for item in payload.get(key, []):
                roots = by_word.get(item["word"], {}).get("roots")
                if roots and item.get("roots") != roots:
                    item["roots"] = roots
                    touched += 1
        dump(path, payload)
        print(f"{path.name}: 回填 {touched} 筆")


if __name__ == "__main__":
    main()
