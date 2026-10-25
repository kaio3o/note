# -*- coding: utf-8 -*-
"""套用 121 個既有 ready 單字補充資料至 vocabulary-bank.json 與 2026-10-26.json。"""

from __future__ import annotations

import json
from pathlib import Path

from patch_121_data import PATCH_121

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "多益高頻單字" / "vocabulary-bank.json"
DAILY_PATH = ROOT / "多益高頻單字" / "data" / "2026-10-26.json"
LATEST_PATH = ROOT / "多益高頻單字" / "data" / "latest.json"


def main():
    print(f"Total patch items: {len(PATCH_121)}")
    assert len(PATCH_121) == 121, f"Expected 121 items, got {len(PATCH_121)}"

    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    updated_bank_count = 0

    for w in bank["words"]:
        word = w["word"]
        if word in PATCH_121:
            patch = PATCH_121[word]
            w["phonetic"] = patch["phonetic"]
            w["meaning"] = patch["meaning"]
            w["topics"] = patch["topics"]
            w["tags"] = patch["tags"]
            if not isinstance(w.get("example"), dict):
                w["example"] = {"en": "", "zh": patch["example_zh"]}
            else:
                w["example"]["zh"] = patch["example_zh"]
            w["collocations"] = patch["collocations"]
            w["status"] = "ready"
            updated_bank_count += 1

    print(f"Updated {updated_bank_count} words in vocabulary-bank.json.")
    assert updated_bank_count == 121, f"Expected 121, got {updated_bank_count}"
    BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # 同步更新 2026-10-26.json 與 latest.json 中的對應單字資料
    if DAILY_PATH.exists():
        daily = json.loads(DAILY_PATH.read_text(encoding="utf-8"))
        updated_daily_count = 0
        for dw in daily.get("words", []):
            dword = dw["word"]
            if dword in PATCH_121:
                patch = PATCH_121[dword]
                dw["phonetic"] = patch["phonetic"]
                dw["meaning"] = patch["meaning"]
                if not isinstance(dw.get("example"), dict):
                    dw["example"] = {"en": "", "zh": patch["example_zh"]}
                else:
                    dw["example"]["zh"] = patch["example_zh"]
                dw["collocations"] = patch["collocations"]
                updated_daily_count += 1
        serialized = json.dumps(daily, ensure_ascii=False, indent=2) + "\n"
        DAILY_PATH.write_text(serialized, encoding="utf-8")
        LATEST_PATH.write_text(serialized, encoding="utf-8")
        print(f"Updated {updated_daily_count} words in 2026-10-26.json and latest.json.")

    print("Patch 121 completed successfully.")


if __name__ == "__main__":
    main()
