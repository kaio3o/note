# -*- coding: utf-8 -*-
"""完整驗證腳本：JSON 格式、重複檢查、ready 欄位完整性檢查與每日生成檢查。"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "多益高頻單字"
BANK_PATH = NOTES_DIR / "vocabulary-bank.json"
DAILY_JSON = NOTES_DIR / "data" / "2026-10-26.json"
LATEST_JSON = NOTES_DIR / "data" / "latest.json"

REQUIRED_FIELDS = ["phonetic", "pos", "meaning", "example", "mnemonic", "collocations"]
DAILY_REQUIRED_KEYS = ["version", "date", "totalCount", "words", "reviewWords"]
WORD_REQUIRED_KEYS = ["id", "word", "group", "example", "mnemonic", "collocations", "reviewDates"]


def valid_roots(value) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    return isinstance(value, list) and len(value) > 0 and all(isinstance(r, str) and r.strip() for r in value)


def run_checks():
    print("=== 1. JSON 格式檢查 ===")
    try:
        bank = json.loads(BANK_PATH.read_text(encoding="utf-8"))
        print(f"✓ vocabulary-bank.json 解析成功，根鍵: {list(bank.keys())}")
    except Exception as e:
        print(f"✗ vocabulary-bank.json 解析失敗: {e}")
        sys.exit(1)

    print("\n=== 2. 單字重複檢查 ===")
    words = bank.get("words", [])
    seen = set()
    duplicates = []
    for w in words:
        word = w["word"].strip().lower()
        if word in seen:
            duplicates.append(word)
        seen.add(word)
    if duplicates:
        print(f"✗ 發現重複單字: {duplicates}")
        sys.exit(1)
    else:
        print(f"✓ 無重複單字，總單字數: {len(words)}")

    print("\n=== 3. ready 欄位完整性檢查 ===")
    readies = [w for w in words if w.get("status") == "ready"]
    candidates = [w for w in words if w.get("status") == "candidate"]
    print(f"Ready 單字總數: {len(readies)}")
    print(f"Candidate 單字總數: {len(candidates)}")

    complete_readies = []
    incomplete_readies = []

    for w in readies:
        word = w["word"]
        errors = []
        if not w.get("phonetic"):
            errors.append("缺少 phonetic")
        if not w.get("pos"):
            errors.append("缺少 pos")
        meaning = w.get("meaning")
        if not meaning or (isinstance(meaning, list) and len(meaning) == 0):
            errors.append("缺少 meaning")
        ex = w.get("example")
        if not isinstance(ex, dict) or not ex.get("en") or not ex.get("zh"):
            errors.append("缺少 example (en 或 zh)")
        if not w.get("mnemonic"):
            errors.append("缺少 mnemonic")
        colloc = w.get("collocations")
        if not isinstance(colloc, list) or len(colloc) == 0:
            errors.append("缺少 collocations")

        if errors:
            incomplete_readies.append((word, errors))
        else:
            complete_readies.append(word)

    print(f"✓ 完整符合七大欄位規格之 ready 單字數: {len(complete_readies)}")
    print(f"ℹ 既有早期（尚未補齊音標/例句中譯/搭配詞）之 ready 單字數: {len(incomplete_readies)}")

    print("\n=== 3b. roots 欄位格式檢查（選填） ===")
    bad_roots = [w["word"] for w in words if "roots" in w and not valid_roots(w["roots"])]
    if bad_roots:
        print(f"✗ roots 格式錯誤（須為非空字串或字串陣列）: {bad_roots}")
        sys.exit(1)
    print(f"✓ 含 roots 的單字數: {sum(1 for w in words if 'roots' in w)}")

    print("\n=== 4. 執行 generate_toeic_daily.py --date 2026-10-26 ===")
    res = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_toeic_daily.py"), "--date", "2026-10-26"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    print(f"Exit code: {res.returncode}")
    print(f"Stdout: {res.stdout.strip()}")
    if res.stderr:
        print(f"Stderr: {res.stderr.strip()}")
    assert res.returncode == 0, f"generate_toeic_daily.py 執行失敗: {res.stderr}"

    print("\n=== 5. 確認產生的每日 JSON 結構完整性 ===")
    daily = json.loads(DAILY_JSON.read_text(encoding="utf-8"))
    for key in DAILY_REQUIRED_KEYS:
        assert key in daily, f"每日 JSON 缺少根欄位: {key}"
        print(f"✓ 根欄位 '{key}' 存在 (值類型: {type(daily[key]).__name__})")

    daily_words = daily.get("words", [])
    print(f"每日單字數量: {len(daily_words)}")
    assert len(daily_words) == 40, f"每日單字應有 40 個，實際有 {len(daily_words)}"

    for idx, w in enumerate(daily_words):
        for wk in WORD_REQUIRED_KEYS:
            assert wk in w, f"單字 [{w.get('word')}] 缺少必要欄位: {wk}"
            assert w[wk] is not None, f"單字 [{w.get('word')}] 欄位 {wk} 為 None"
        # 額外確認 example 包含 en
        assert "en" in w["example"], f"單字 [{w.get('word')}] example 缺少 'en'"

    for w in daily_words:
        if "roots" in w:
            assert valid_roots(w["roots"]), f"單字 [{w.get('word')}] roots 格式錯誤"

    print("✓ 每日 JSON (2026-10-26.json) 所有 40 個單字均包含：")
    for wk in WORD_REQUIRED_KEYS:
        print(f"   - {wk}")

    print("\n=== 全部驗證成功通過！ ===")


if __name__ == "__main__":
    run_checks()
