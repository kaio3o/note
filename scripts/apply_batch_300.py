# -*- coding: utf-8 -*-
"""套用 300 個全新 candidate 單字資料至 vocabulary-bank.json 並驗證。"""

from __future__ import annotations

import json
from pathlib import Path

from batch_a_100 import DATA_BATCH_A
from batch_b_100 import DATA_BATCH_B
from batch_c_100 import DATA_BATCH_C

ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "多益高頻單字" / "vocabulary-bank.json"

COMBINED_300 = {**DATA_BATCH_A, **DATA_BATCH_B, **DATA_BATCH_C}


def main():
    print(f"Total words in 300 batch: {len(COMBINED_300)}")
    assert len(COMBINED_300) == 300, f"Expected 300, got {len(COMBINED_300)}"

    bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    words = bank["words"]
    total_before = len(words)
    candidates_before = sum(1 for w in words if w.get("status") == "candidate")
    ready_before = sum(1 for w in words if w.get("status") == "ready")

    print(f"Before update -> Total: {total_before}, Candidates: {candidates_before}, Ready: {ready_before}")

    updated_count = 0
    for w in words:
        word = w["word"]
        if word in COMBINED_300:
            if w.get("status") == "ready":
                print(f"WARNING: {word} is already ready! Skipping to prevent overwrite.")
                continue
            data = COMBINED_300[word]

            # 保持原有不可修改欄位
            # word, id, level, orderInLevel, sourceList, sourceRank, lemma, wordForms, reviewDefaults, sourceRefs
            w["phonetic"] = data["phonetic"]
            w["pos"] = data["pos"]
            w["meaning"] = data["meaning"]
            w["topics"] = data["topics"]
            w["tags"] = data["tags"]
            w["example"] = data["example"]
            w["mnemonic"] = data["mnemonic"]
            w["collocations"] = data["collocations"]
            w["status"] = "ready"
            updated_count += 1

    print(f"Successfully updated {updated_count} candidate words to ready.")
    assert updated_count == 300, f"Expected to update 300 candidates, but updated {updated_count}"

    BANK_PATH.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("vocabulary-bank.json successfully updated with 300 new ready words.")

    # 驗證
    verify_bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    words_after = verify_bank["words"]
    candidates_after = sum(1 for w in words_after if w.get("status") == "candidate")
    ready_after = sum(1 for w in words_after if w.get("status") == "ready")

    print(f"After update -> Total: {len(words_after)}, Candidates: {candidates_after}, Ready: {ready_after}")
    assert len(words_after) == total_before
    assert candidates_after == candidates_before - 300
    assert ready_after == ready_before + 300


if __name__ == "__main__":
    main()
