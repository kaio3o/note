import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from batch500_1 import BATCH_1
from batch500_2 import BATCH_2
from batch500_3 import BATCH_3
from batch500_4 import BATCH_4
from batch500_5 import BATCH_5

ALL_BATCHES = {}
for b in [BATCH_1, BATCH_2, BATCH_3, BATCH_4, BATCH_5]:
    ALL_BATCHES.update(b)

print(f"Loaded {len(ALL_BATCHES)} patch entries.")

bank_path = Path(__file__).resolve().parent.parent / "多益高頻單字" / "vocabulary-bank.json"
with open(bank_path, "r", encoding="utf-8") as f:
    data = json.load(f)

words = data.get("words", [])
applied_count = 0
not_found = []

for w in words:
    word_text = w.get("word")
    if word_text in ALL_BATCHES:
        patch = ALL_BATCHES[word_text]
        # 更新欄位，同時確保 Lexifold 原始欄位完整保留
        w["phonetic"] = patch["phonetic"]
        w["pos"] = patch["pos"]
        w["meaning"] = patch["meaning"]
        w["topics"] = patch["topics"]
        w["tags"] = patch["tags"]
        w["example"] = patch["example"]
        w["mnemonic"] = patch["mnemonic"]
        w["collocations"] = patch["collocations"]
        w["status"] = "ready"
        applied_count += 1

print(f"Applied updates to {applied_count} words in vocabulary-bank.json.")

# 統計現況
ready_count = sum(1 for w in words if w.get("status") == "ready")
candidate_count = sum(1 for w in words if w.get("status") == "candidate")
print(f"Total ready: {ready_count}")
print(f"Total candidate: {candidate_count}")
print(f"Total words: {len(words)}")

with open(bank_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("vocabulary-bank.json successfully written.")
