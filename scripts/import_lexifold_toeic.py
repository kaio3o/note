"""將 Lexifold TOEIC TSV 轉成可追蹤來源的獨立詞庫 JSON。"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BANK_PATH = ROOT / "多益高頻單字" / "vocabulary-bank.json"
DAILY_JSON = ROOT / "多益高頻單字" / "data" / "2026-10-26.json"
SOURCE_URL = "https://lexifold.com/word-lists/toeic.tsv"
LICENSE_URL = "https://creativecommons.org/licenses/by-sa/4.0/"


def load_existing_details() -> dict[str, dict]:
    details: dict[str, dict] = {}
    if DAILY_JSON.exists():
        payload = json.loads(DAILY_JSON.read_text(encoding="utf-8"))
        for item in payload.get("newWords", []):
            details[item["word"].lower()] = item

    # 保留原本 RAW_BANK 中已整理好的詞義、例句與提示，避免匯入候選詞時遺失既有內容。
    script_path = ROOT / "scripts" / "generate_toeic_daily.py"
    spec = importlib.util.spec_from_file_location("toeic_generator", script_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for item in module.load_bank():
            details.setdefault(item["word"].lower(), item)
    return details


def import_tsv(source_path: Path) -> list[dict]:
    existing = load_existing_details()
    result: list[dict] = []
    seen: set[str] = set()
    with source_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            word = row["headword"].strip().lower()
            if not re.fullmatch(r"[a-z]+", word) or word in seen:
                continue
            seen.add(word)
            detail = existing.get(word, {})
            result.append({
                "id": f"lexifold_toeic_{len(result) + 1:04d}",
                "word": word,
                "lemma": word,
                "phonetic": detail.get("phonetic"),
                "pos": detail.get("partOfSpeech"),
                "meaning": detail.get("meaning"),
                "level": row["level_name_en"],
                "orderInLevel": int(row["order_in_level"]),
                "sourceList": row["source_list"],
                "sourceRank": int(row["source_rank"]) if row["source_rank"].strip() else None,
                "wordForms": row["word_forms"].split("|") if row["word_forms"] else [word],
                "topics": [],
                "tags": ["TOEIC", "Lexifold"],
                "example": (
                    {"en": detail["example"], "zh": ""}
                    if detail.get("example")
                    else None
                ),
                "mnemonic": detail.get("tip"),
                "collocations": [],
                "reviewDefaults": [1, 3, 7, 14, 30],
                "status": "ready" if detail.get("meaning") and detail.get("example") else "candidate",
                "sourceRefs": ["Lexifold TOEIC", row["source_list"]],
            })
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Lexifold toeic.tsv 路徑")
    args = parser.parse_args()
    words = import_tsv(args.source)
    payload = {
        "version": "1.0",
        "updatedAt": "2026-10-25",
        "language": "en-US",
        "target": {"exam": "TOEIC Listening & Reading", "estimatedScore": 395},
        "totalCount": len(words),
        "sourcePolicy": {
            "name": "Lexifold TOEIC word list",
            "sourceUrl": SOURCE_URL,
            "license": "CC BY-SA 4.0",
            "licenseUrl": LICENSE_URL,
            "attribution": "Lexifold TOEIC word list; adapted from NGSL 1.2, TSL 1.2 and NAWL 1.2 by Browne, Culligan and Phillips.",
            "note": "Lexifold publishes headwords, levels, order and source information. Meanings, examples, translations and audio are not included in the TSV.",
        },
        "words": words,
    }
    BANK_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ready = sum(item["status"] == "ready" for item in words)
    print(json.dumps({"total": len(words), "ready": ready, "candidate": len(words) - ready}, ensure_ascii=False))


if __name__ == "__main__":
    main()
