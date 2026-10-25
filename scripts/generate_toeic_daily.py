"""產生每日多益 Markdown 與詳細 JSON；由 GitHub Actions 在台灣時間每日執行。"""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
NOTES_DIR = ROOT / "多益高頻單字"
DATA_DIR = NOTES_DIR / "data"
INTERVALS = (1, 3, 7, 14, 30)

# 先提供可持續擴充的 TOEIC 詞庫。若詞庫不足，腳本會明確失敗，不會重複或臨時編造單字。
RAW_BANK = """
accommodate|verb|容納；配合|The hotel can accommodate 200 guests.|想像房間把客人安排進去。
accurate|adjective|準確的|Please make sure the report is accurate.|accurate = correct。
appointment|noun|約會；預約|I have a dentist appointment at three.|常和 make 或 confirm 搭配。
available|adjective|可用的；有空的|The manager is available after lunch.|available = ready to be used。
benefit|noun/verb|好處；受益|Employees receive health benefits.|想成工作帶來的好處。
confirm|verb|確認|Please confirm your reservation by email.|confirm = make sure。
convenient|adjective|方便的|The store is convenient for commuters.|和 convenience 都與方便有關。
department|noun|部門；系|Contact the sales department for details.|公司裡分工的部門。
discount|noun/verb|折扣|Customers receive a ten percent discount.|讓價格往下掉。
document|noun/verb|文件；記錄|Please attach the document to your email.|文件可以被 attach。
effective|adjective|有效的|The new policy is effective immediately.|effective = works well。
equipment|noun|設備|The office purchased new equipment.|equipment 通常不可數。
estimate|noun/verb|估計；估價|The repair estimate is two hundred dollars.|尚未確定的數字。
expense|noun|費用；支出|Travel expenses will be reimbursed.|常和 pay 或 cost 一起出現。
facility|noun|設施；場所|The sports facility opens at six.|提供服務的場所。
frequently|adverb|經常地|The train runs frequently during rush hour.|frequent 的副詞形式。
handle|verb/noun|處理；把手|She handles customer complaints professionally.|handle a problem = 處理問題。
immediately|adverb|立即地|Please reply immediately.|immediately = right away。
improve|verb|改善；進步|The company plans to improve service quality.|常接能力或品質。
increase|noun/verb|增加|Sales increased by fifteen percent.|可以是名詞或動詞。
inform|verb|通知|We will inform you of the decision.|inform someone of something。
ingredient|noun|成分；食材|The label lists every ingredient.|食品標籤常見單字。
maintenance|noun|維護；保養|The elevator is closed for maintenance.|常和 building 或 equipment 搭配。
manager|noun|經理；管理者|Ask the manager for assistance.|管理 team 或 department。
method|noun|方法|This method saves time and money.|method = way of doing something。
notice|noun/verb|注意；通知|Did you notice the change in schedule?|可表示注意到或公告。
obtain|verb|取得|Applicants must obtain a permit.|比 get 更正式。
operate|verb|操作；營運|Only trained staff may operate the machine.|operate a machine or company。
permission|noun|許可|You need permission to enter this area.|常和 ask for 搭配。
prepare|verb|準備|Please prepare the materials before the meeting.|prepare for + 事件。
product|noun|產品|The company launched a new product.|常出現在 sales 或 marketing。
provide|verb|提供|The hotel provides free breakfast.|provide someone with something。
purchase|noun/verb|購買|The department purchased new computers.|比 buy 正式。
recommend|verb|推薦|I recommend this restaurant to visitors.|後面接名詞或動名詞。
request|noun/verb|要求；請求|We received a request for more information.|正式信件常見。
require|verb|需要；要求|The position requires two years of experience.|比 need 正式。
schedule|noun/verb|行程；安排|The meeting is scheduled for Monday.|schedule for + 日期。
shipment|noun|貨物；出貨|The shipment arrived this morning.|和 delivery 有關。
temporary|adjective|暫時的|This is a temporary position.|相反是 permanent。
vacancy|noun|空缺；職缺|The company posted a vacancy online.|職缺廣告常用。
agenda|noun|議程|The agenda includes three topics.|會議開始前先看議程。
assign|verb|分派|The supervisor assigned a task to me.|assign a task。
attend|verb|參加；出席|All employees must attend the meeting.|attend a meeting。
authorize|verb|授權|Only managers can authorize refunds.|authorize = give official permission。
cancel|verb|取消|The airline canceled the flight.|cancel a reservation or event。
candidate|noun|候選人；應徵者|Each candidate submitted a resume.|求職與選舉都會使用。
capacity|noun|容量；能力|The room has a capacity of 80 people.|可容納的人數。
deadline|noun|截止期限|The application deadline is Friday.|deadline 前常搭配 meet。
deliver|verb|遞送；交付|We deliver orders within two days.|deliver an order。
distribute|verb|分發；配送|Staff distributed the forms to visitors.|把東西分給多人。
employee|noun|員工|Every employee receives an identification card.|employ 的人。
employer|noun|雇主|The employer offers flexible hours.|employ 別人的人。
enclose|verb|附上；裝入|Please enclose a copy of your receipt.|正式信件常見。
entrance|noun|入口|The main entrance is on the left.|相反是 exit。
equipment|noun|設備|The laboratory needs safety equipment.|equipment 是不可數名詞。
exhibit|noun/verb|展覽品；展示|The museum will exhibit local artwork.|exhibit artwork。
extend|verb|延長；提供|The store extended its opening hours.|extend a deadline or service。
feedback|noun|回饋|Customers provided positive feedback.|feedback 通常不可數。
flexible|adjective|有彈性的|Our schedule is flexible this week.|可調整、不固定。
forecast|noun/verb|預測|The weather forecast predicts rain.|forecast future conditions。
guarantee|noun/verb|保證|The product comes with a one-year guarantee.|保證品質或結果。
guideline|noun|指導方針|Please follow the safety guidelines.|guideline 是行動規則。
hire|verb|雇用|The company plans to hire two assistants.|hire new staff。
inquiry|noun|詢問|We received an inquiry about delivery.|正式的 question。
install|verb|安裝|Technicians will install the new software.|install equipment or software。
instruction|noun|指示；說明|Read the instructions before use.|instructions 通常用複數。
inventory|noun|庫存|The store checks its inventory weekly.|inventory = stock。
issue|noun/verb|問題；發布|Please report any technical issue.|issue 可表示問題或發布。
location|noun|地點|The new office is in a convenient location.|場所的位置。
membership|noun|會員資格|The gym offers annual membership.|member 的資格。
negotiate|verb|協商|The two companies negotiated a contract.|negotiate a price or contract。
objective|noun/adjective|目標；客觀的|Our main objective is to reduce costs.|objective = goal。
occupy|verb|佔用|The meeting will occupy the whole morning.|占用時間或空間。
option|noun|選項|Customers can choose a payment option.|可選擇的項目。
outstanding|adjective|傑出的；未支付的|Please pay the outstanding balance.|outstanding balance = 未付款項。
packaging|noun|包裝|The new packaging protects the product.|產品外包裝。
policy|noun|政策；規定|The company has a strict privacy policy.|公司正式規定。
postpone|verb|延期|The event was postponed until Monday.|postpone an event。
procedure|noun|程序|Follow the emergency procedure.|正式流程。
professional|adjective/noun|專業的；專業人士|She gave a professional presentation.|專業的表現。
profit|noun|利潤|The business reported a higher profit.|收入扣除成本後的錢。
promote|verb|促銷；升遷|The store will promote its new service.|促銷或升職。
proposal|noun|提案|The board approved the proposal.|正式提案。
recruit|verb/noun|招募；新進人員|The firm is recruiting sales staff.|recruit new employees。
refund|noun/verb|退款|Customers may request a full refund.|退回已支付的錢。
regulation|noun|規章；規定|All drivers must follow traffic regulations.|正式規則。
replace|verb|替換|We need to replace the broken printer.|replace A with B。
reservation|noun|預訂|I made a reservation for two people.|餐廳、旅館、航班都可用。
reschedule|verb|重新安排|Can we reschedule the interview?|重新安排時間。
responsible|adjective|負責的|She is responsible for the budget.|responsible for + 名詞。
retail|noun/adjective|零售|The company operates several retail stores.|retail store。
revenue|noun|收入|Online sales increased the revenue.|企業總收入。
salary|noun|薪資|The position offers a competitive salary.|固定薪資。
submit|verb|提交|Please submit the form by Friday.|submit an application。
supplier|noun|供應商|We changed suppliers last year.|提供商品的公司。
survey|noun/verb|調查|Customers completed a short survey.|問卷調查。
transfer|verb/noun|轉移；轉乘|Please transfer the payment today.|轉帳或轉移。
valid|adjective|有效的|Your passport must be valid.|有效期限內。
warehouse|noun|倉庫|The goods are stored in a warehouse.|存放貨物的地方。
withdraw|verb|撤回；提領|He withdrew his application.|撤回申請或提領金錢。
annual|adjective|每年的|The company holds an annual meeting.|每年一次。
approximately|adverb|大約|The trip takes approximately two hours.|approximately = about。
assistance|noun|協助|Please contact us if you need assistance.|需要幫忙時使用。
branch|noun|分店；分部|The bank opened a new branch.|公司或銀行的分支。
brochure|noun|小冊子|The brochure describes our services.|介紹產品或服務的小冊子。
commercial|adjective/noun|商業的；廣告|The commercial promotes a new car.|commercial break。
complaint|noun|抱怨；申訴|The manager handled the complaint quickly.|customer complaint。
consumption|noun|消耗量|The report measures energy consumption.|消耗能源或資源。
contract|noun/verb|合約；簽約|Both sides signed the contract.|正式法律文件。
destination|noun|目的地|Paris is a popular destination.|旅行最後到達的地方。
discounted|adjective|打折的|Discounted items cannot be returned.|discount 的形容詞形式。
efficient|adjective|有效率的|The new system is more efficient.|少花時間或資源。
feedback|noun|回饋|The manager asked for feedback.|feedback 不可數。
freight|noun|貨運；貨物|Freight costs have increased.|大型貨物運輸。
merchandise|noun|商品|The store displays new merchandise.|商店販售的商品。
priority|noun|優先事項|Safety is our top priority.|最重要的事情。
process|noun/verb|流程；處理|The application process takes a week.|process an application。
production|noun|生產|Production will begin next month.|製造商品的過程。
profitability|noun|獲利能力|The plan improves profitability.|profit 的相關名詞。
qualified|adjective|合格的；有資格的|Only qualified applicants will be contacted.|符合條件。
quarterly|adjective/adverb|每季的|The company releases quarterly results.|一年四次。
renovate|verb|整修|The hotel will renovate its lobby.|翻新建築或房間。
supplier|noun|供應商|The supplier delivered the materials.|供應商品或材料。
transportation|noun|運輸；交通|Public transportation is convenient here.|交通方式的總稱。
urgent|adjective|緊急的|This is an urgent request.|需要立即處理。
verify|verb|驗證；核實|Please verify your contact information.|確認資料是否正確。
volume|noun|數量；音量|The store sells a large volume of goods.|大量或音量。
workshop|noun|研習會；工作坊|Employees attended a safety workshop.|學習或訓練活動。
"""


def load_bank() -> list[dict[str, str]]:
    bank = []
    seen = set()
    for row in RAW_BANK.strip().splitlines():
        word, pos, meaning, example, tip = row.split("|", 4)
        if word in seen:
            continue
        seen.add(word)
        bank.append({"word": word, "partOfSpeech": pos, "meaning": meaning, "example": example, "tip": tip})
    return bank


def used_words(exclude: Path | None = None) -> set[str]:
    result = set()
    for path in NOTES_DIR.glob("*.md"):
        if exclude and path == exclude:
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
        for item in payload.get("newWords", []):
            if target.isoformat() in item.get("reviewDates", []):
                due.append(item)
    return due


def build_payload(target: date) -> dict:
    md_path = NOTES_DIR / f"{target.isoformat()}.md"
    json_path = DATA_DIR / f"{target.isoformat()}.json"
    if md_path.exists() and json_path.exists():
        return json.loads(json_path.read_text(encoding="utf-8"))

    bank = load_bank()
    bank_by_word = {item["word"]: item for item in bank}
    if md_path.exists():
        existing_words = [line.strip().lower() for line in md_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        selected = [bank_by_word[word] for word in existing_words if word in bank_by_word]
        if len(selected) != 40:
            raise RuntimeError(f"既有 {md_path.name} 必須包含詞庫中的 40 個單字，目前只有 {len(selected)} 個可解析。")
    else:
        used = used_words()
        selected = [item for item in bank if item["word"] not in used][:40]
    if len(selected) < 40:
        raise RuntimeError(f"TOEIC 詞庫只剩 {len(selected)} 個未使用單字，拒絕重複產生。請先擴充 RAW_BANK。")

    new_words = []
    for item in selected:
        new_words.append({
            **item,
            "reviewDates": [(target + timedelta(days=days)).isoformat() for days in INTERVALS],
        })
    reviews = due_reviews(target)
    payload = {
        "date": target.isoformat(),
        "level": "TOEIC 395 baseline",
        "reviewIntervals": list(INTERVALS),
        "newWords": new_words,
        "reviewWords": reviews,
        "newWordCount": len(new_words),
        "reviewWordCount": len(reviews),
        "totalWordCount": len(new_words) + len(reviews),
    }
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    md_path.write_text("\n".join(item["word"] for item in new_words) + "\n", encoding="utf-8")
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (DATA_DIR / "latest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="YYYY-MM-DD；未指定時使用台灣日期")
    args = parser.parse_args()
    target = date.fromisoformat(args.date) if args.date else datetime.now(ZoneInfo("Asia/Taipei")).date()
    payload = build_payload(target)
    print(json.dumps({"date": payload["date"], "new": payload["newWordCount"], "review": payload["reviewWordCount"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
