# -*- coding: utf-8 -*-
"""將第二批 200 個候選單字資料套用至 vocabulary-bank.json 並驗證。"""

from __future__ import annotations

import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "多益高頻單字"
BANK_PATH = NOTES_DIR / "vocabulary-bank.json"

from batch200_3a import BATCH_3A
from batch200_3b import BATCH_3B
from batch200_4a import BATCH_4A
from batch200_4b import BATCH_4B

COMBINED_DATA = {**BATCH_3A, **BATCH_3B, **BATCH_4A, **BATCH_4B}


def main():
    print(f"Total words in update batch: {len(COMBINED_DATA)}")
    assert len(COMBINED_DATA) == 200, f"Expected 200 words, got {len(COMBINED_DATA)}"

    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    words = bank["words"]
    total_before = len(words)
    candidates_before = sum(1 for w in words if w.get("status") == "candidate")
    ready_before = sum(1 for w in words if w.get("status") == "ready")

    print(f"Before update -> Total: {total_before}, Candidates: {candidates_before}, Ready: {ready_before}")

    updated_count = 0
    for w in words:
        word = w["word"]
        if word in COMBINED_DATA:
            if w.get("status") == "ready":
                print(f"WARNING: {word} is already ready! Skipping to prevent overwrite.")
                continue
            data = COMBINED_DATA[word]

            # 保持原始不可修改欄位
            # id, word, lemma, level, orderInLevel, sourceList, sourceRank, wordForms, reviewDefaults, sourceRefs
            w["phonetic"] = data["phonetic"]
            w["pos"] = data["pos"]
            w["meaning"] = data["meaning"]
            w["topics"] = data["topics"]
            w["tags"] = data["tags"]
            w["example"] = data["example"]
            w["mnemonic"] = data["mnemonic"]
            w["collocations"] = data["collocations"]
            w["status"] = "ready"
            if "roots" in data:
                w["roots"] = data["roots"]
            updated_count += 1

    print(f"Successfully updated {updated_count} candidate words to ready.")
    assert updated_count == 200, f"Expected to update 200 candidates, but updated {updated_count}"

    # 寫回檔案 (確保 UTF-8 且格式縮排一致)
    BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("vocabulary-bank.json successfully written.")

    # 統計更新後現況
    verify_bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    v_words = verify_bank["words"]
    ready_after = sum(1 for w in v_words if w.get("status") == "ready")
    candidates_after = sum(1 for w in v_words if w.get("status") == "candidate")
    print(f"After update -> Total: {len(v_words)}, Ready: {ready_after}, Candidates: {candidates_after}")
    assert ready_after == ready_before + 200, f"Expected {ready_before + 200} ready words, got {ready_after}"
    assert candidates_after == candidates_before - 200, f"Expected {candidates_before - 200} candidate words, got {candidates_after}"


if __name__ == "__main__":
    main()
