import re
from pathlib import Path

path = Path("note/scripts/generate_toeic_daily.py")
content = path.read_text(encoding="utf-8")

old_code = """def load_bank() -> list[dict]:
    payload = json.loads(BANK_PATH.read_text(encoding="utf-8"))
    # 只有完成中文、例句與基本資料的 ready 單字才會進入每日學習，避免 PWA 顯示半成品。
    return [item for item in payload["words"] if item.get("status") == "ready"]


def used_words(exclude: Path | None = None) -> set[str]:
    result = set()
    for path in NOTES_DIR.glob("*.md"):
        if exclude and path == exclude:
            continue
        result.update(line.strip().lower() for line in path.read_text(encoding="utf-8").splitlines() if line.strip().isalpha())
    return result"""

new_code = """def is_ready_complete(item: dict) -> bool:
    \"\"\"檢查單字是否為 status: ready 且具備所有必需欄位。\"\"\"
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
        if not re.fullmatch(r"\\d{4}-\\d{2}-\\d{2}\\.md", path.name):
            continue
        result.update(line.strip().lower() for line in path.read_text(encoding="utf-8").splitlines() if line.strip().isalpha())
    return result"""

content_normalized = content.replace("\r\n", "\n")
old_code_normalized = old_code.replace("\r\n", "\n")

if old_code_normalized in content_normalized:
    updated = content_normalized.replace(old_code_normalized, new_code)
    # Check if re is imported
    if "import re" not in updated:
        updated = updated.replace("import json\n", "import json\nimport re\n")
    path.write_text(updated.replace("\n", "\r\n"), encoding="utf-8")
    print("SUCCESS: generate_toeic_daily.py updated.")
else:
    print("FAILED: old code not found.")
