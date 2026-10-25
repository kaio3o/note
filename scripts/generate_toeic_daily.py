"""產生每日多益 Markdown 與詳細 JSON；由 GitHub Actions 在台灣時間每日執行。"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "多益高頻單字"
DATA_DIR = NOTES_DIR / "data"
BANK_PATH = NOTES_DIR / "vocabulary-bank.json"
INTERVALS = (1, 3, 7, 14, 30)

def is_ready_complete(item: dict) -> bool:
    """檢查單字是否為 status: ready 且具備所有必需欄位。"""
    if item.get("status") != "ready":
        return False
    if not item.get("phonetic"):
        return False
    if not item.get("pos"):
        return False
    meaning = item.get("meaning")
    if not meaning or (isinstance(meaning, list) and len(meaning) == 0):
        return False
    example = item.get("example")
    if not isinstance(example, dict):
        return False
    if not example.get("en") or not example.get("zh"):
        return False
    if not item.get("mnemonic"):
        return False
    collocations = item.get("collocations")
    if not isinstance(collocations, list) or len(collocations) == 0:
        return False
    return True


def load_bank() -> list[dict]:
    payload = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    # 只有 status 為 ready 且欄位完整（phonetic, pos, meaning, example.en, example.zh, mnemonic, collocations）的單字才會進入每日學習。
    return [item for item in payload["words"] if is_ready_complete(item)]


def used_words(exclude: Path | None = None) -> set[str]:
    result = set()
    for path in NOTES_DIR.glob("*.md"):
        if exclude and path == exclude:
            continue
        # 僅讀取 YYYY-MM-DD.md 每日單字檔案，避免讀取 LEXIFOLD_ATTRIBUTION.md 等非單字檔
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", path.name):
            continue
        result.update(line.strip().lower() for line in path.read_text(encoding="utf-8").splitlines() if line.strip().isalpha())
    return result


def due_reviews(target: date) -> list[dict]:
    due = []
    for path in DATA_DIR.glob("*.json"):
        if path.name == "latest.json":
            continue
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for item in payload.get("words", payload.get("newWords", [])):
            if target.isoformat() in item.get("reviewDates", []):
                due.append(item)
    return due


def as_meaning_list(value) -> list[str]:
    if isinstance(value, list):
        return value
    return [part.strip() for part in str(value or "").split("；") if part.strip()]


def as_example(value) -> dict:
    if isinstance(value, dict):
        return value
    return {"en": str(value or ""), "zh": ""}


def daily_item(item: dict, target: date, index: int) -> dict:
    return {
        "id": f"{target:%Y%m%d}_{index:03d}",
        "word": item["word"],
        "phonetic": item.get("phonetic"),
        "pos": item.get("pos"),
        "meaning": as_meaning_list(item.get("meaning")),
        "group": ((index - 1) // 10) + 1,
        "tags": item.get("tags", ["TOEIC", "高頻單字"]),
        "example": as_example(item.get("example")),
        "mnemonic": item.get("mnemonic"),
        "collocations": item.get("collocations", []),
        "reviewDates": [(target + timedelta(days=days)).isoformat() for days in INTERVALS],
        "sourceRefs": item.get("sourceRefs", []),
    }


def build_payload(target: date) -> dict:
    md_path = NOTES_DIR / f"{target.isoformat()}.md"
    json_path = DATA_DIR / f"{target.isoformat()}.json"
    if json_path.exists():
        existing = json.loads(json_path.read_text(encoding="utf-8"))
        if existing.get("version") == "1.0" and "words" in existing:
            return existing

    bank = load_bank()
    bank_by_word = {item["word"]: item for item in bank}
    if md_path.exists():
        existing_words = [line.strip().lower() for line in md_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        selected = [bank_by_word[word] for word in existing_words if word in bank_by_word]
        if len(selected) != 40:
            raise RuntimeError(f"既有 {md_path.name} 必須包含詞庫中已完成的 40 個單字，目前只有 {len(selected)} 個可解析。")
    else:
        used = used_words()
        selected = [item for item in bank if item["word"] not in used][:40]
    if len(selected) < 40:
        raise RuntimeError(f"已完成詞庫只剩 {len(selected)} 個未使用單字，拒絕重複產生；請先補齊 vocabulary-bank.json。")

    new_words = [daily_item(item, target, index) for index, item in enumerate(selected, start=1)]
    reviews = due_reviews(target)
    payload = {
        "version": "1.0",
        "date": target.isoformat(),
        "level": "TOEIC 395 baseline",
        "totalCount": len(new_words),
        "reviewCount": len(reviews),
        "reviewIntervals": list(INTERVALS),
        "words": new_words,
        "reviewWords": reviews,
    }
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(item["word"] for item in new_words) + "\n", encoding="utf-8")
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    json_path.write_text(serialized, encoding="utf-8")
    (DATA_DIR / "latest.json").write_text(serialized, encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="YYYY-MM-DD；未指定時使用台灣日期")
    args = parser.parse_args()
    target = date.fromisoformat(args.date) if args.date else datetime.now(ZoneInfo("Asia/Taipei")).date()
    payload = build_payload(target)
    print(json.dumps({"date": payload["date"], "new": payload["totalCount"], "review": payload["reviewCount"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()

