# -*- coding: utf-8 -*-
"""批次 1: 前 50 個候選單字高品質 TOEIC 資料 (A2~B1 基準，職場/商務情境)"""

DATA_PART_1 = {
    "have": {
        "phonetic": "/hæv/",
        "pos": "verb",
        "meaning": ["擁有", "舉辦", "經歷"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We will have an important staff meeting in the main conference room at two o'clock.",
            "zh": "我們將於下午兩點在主會議室召開一場重要的全體員工會議。"
        },
        "mnemonic": "基礎商務動詞，常與 meeting (開會)、experience (具備經驗) 搭配。",
        "collocations": ["have a meeting", "have experience"]
    },
    "do": {
        "phonetic": "/duː/",
        "pos": "verb",
        "meaning": ["執行", "處理", "從事"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our marketing team will do everything possible to meet the project deadline.",
            "zh": "我們的行銷團隊將竭盡全力在專案截止日前完成。"
        },
        "mnemonic": "職場行動必備動詞，常搭配 business (洽商) 或 research (做市調)。",
        "collocations": ["do business", "do market research"]
    },
    "say": {
        "phonetic": "/seɪ/",
        "pos": "verb",
        "meaning": ["說", "表示", "說明"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The financial director said that our quarterly revenue increased significantly.",
            "zh": "財務總監表示我們本季度的營收顯著成長。"
        },
        "mnemonic": "轉述發言或主管報告重點的關鍵動詞，常接 that 子句。",
        "collocations": ["say that", "have something to say"]
    },
    "go": {
        "phonetic": "/ɡoʊ/",
        "pos": "verb",
        "meaning": ["前往", "進行", "運作"],
        "topics": ["機場交通", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The regional sales manager will go to Chicago on business next Monday.",
            "zh": "區域銷售經理將於下週一前往芝加哥出差。"
        },
        "mnemonic": "出差與行程常客，go on business 意指公務出差。",
        "collocations": ["go on business", "go over"]
    },
    "all": {
        "phonetic": "/ɔːl/",
        "pos": "determiner",
        "meaning": ["全部的", "所有的"],
        "topics": ["公司政策", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All employees must wear their identification badges inside the building.",
            "zh": "所有員工在大樓內部皆必須配戴身分識別證。"
        },
        "mnemonic": "多益公告常見字，搭配複數名詞指全員，如 all staff 或 all employees。",
        "collocations": ["all employees", "all staff members"]
    },
    "one": {
        "phonetic": "/wʌn/",
        "pos": "pronoun",
        "meaning": ["一個", "某個人", "某一事物"],
        "topics": ["人資招聘", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Ms. Clark is one of the most qualified candidates for the managerial opening.",
            "zh": "克拉克女士是該主管職缺中最具資格的應徵者之一。"
        },
        "mnemonic": "多益閱讀與聽力極高頻句型：one of the + 複數名詞 (其中之一)。",
        "collocations": ["one of the", "one another"]
    },
    "about": {
        "phonetic": "/əˈbaʊt/",
        "pos": "preposition",
        "meaning": ["關於", "大約"],
        "topics": ["商務會議", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The department head answered several questions about the proposed annual budget.",
            "zh": "部門主管回答了數個關於擬定之年度預算的問題。"
        },
        "mnemonic": "會議討論主題必備介系詞，或用於數字前表示約略數額。",
        "collocations": ["talk about", "concerned about"]
    },
    "know": {
        "phonetic": "/noʊ/",
        "pos": "verb",
        "meaning": ["知道", "了解", "知悉"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please let us know if you need to modify your flight reservation.",
            "zh": "若您需要修改航班預訂，請儘速告知我們。"
        },
        "mnemonic": "商務書信最標準客套句型：Please let me know / let us know。",
        "collocations": ["let someone know", "know about"]
    },
    "more": {
        "phonetic": "/mɔːr/",
        "pos": "adjective",
        "meaning": ["更多的", "進一步的"],
        "topics": ["客戶服務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "For more information regarding the product launch, please contact our support center.",
            "zh": "如需更多有關產品發布的資訊，請聯絡我們的客服支援中心。"
        },
        "mnemonic": "公告、廣告文宣末尾固定句型：For more information (如需更多資訊)。",
        "collocations": ["more information", "more details"]
    },
    "get": {
        "phonetic": "/ɡɛt/",
        "pos": "verb",
        "meaning": ["獲得", "取得", "收到"],
        "topics": ["行銷銷售", "採購"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Customers who place an order before noon will get a ten percent discount.",
            "zh": "中午前下單的顧客將可享有九折優惠。"
        },
        "mnemonic": "多益商業情境指取得核准 (get approval) 或享有折扣 (get a discount)。",
        "collocations": ["get approval", "get a discount"]
    },
    "like": {
        "phonetic": "/laɪk/",
        "pos": "preposition",
        "meaning": ["如同", "像是"],
        "topics": ["行銷銷售", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our courier service offers premium options like overnight delivery and signature confirmation.",
            "zh": "我們的快遞服務提供諸如隔夜送達與簽收確認等尊榮選項。"
        },
        "mnemonic": "舉例說明服務或產品特色常用的介系詞，意為如同、例如。",
        "collocations": ["would like to", "something like"]
    },
    "think": {
        "phonetic": "/θɪŋk/",
        "pos": "verb",
        "meaning": ["認為", "考慮", "想"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The board members think that opening a branch in Tokyo will boost international sales.",
            "zh": "董事會成員認為在東京設立分公司將有助於推動國際銷售。"
        },
        "mnemonic": "會議中表達商業看法或評估方案的核心動詞。",
        "collocations": ["think about", "think that"]
    },
    "make": {
        "phonetic": "/meɪk/",
        "pos": "verb",
        "meaning": ["進行", "制定", "預約"],
        "topics": ["旅館住宿", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "You can make a hotel reservation directly through our corporate travel portal.",
            "zh": "您可以直接透過我們的企業差旅平台預訂飯店。"
        },
        "mnemonic": "高頻搭配動詞：make a reservation (預約)、make a decision (做決策)。",
        "collocations": ["make a reservation", "make a decision"]
    },
    "time": {
        "phonetic": "/taɪm/",
        "pos": "noun",
        "meaning": ["時間", "時刻", "工時"],
        "topics": ["機場交通", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The flight from London arrived on time despite unfavorable weather conditions.",
            "zh": "儘管天候不佳，自倫敦起飛的班機仍準時抵達。"
        },
        "mnemonic": "交通與會議考點：on time (準時)、in time (及時)。",
        "collocations": ["on time", "part-time"]
    },
    "see": {
        "phonetic": "/siː/",
        "pos": "verb",
        "meaning": ["查閱", "看見", "會面"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please see the attached PDF for a detailed overview of the conference schedule.",
            "zh": "請查閱附件 PDF 以取得會議時程的詳細概述。"
        },
        "mnemonic": "商務書信高頻句型：Please see the attached document (請參閱附件)。",
        "collocations": ["see attached", "see if"]
    },
    "up": {
        "phonetic": "/ʌp/",
        "pos": "adverb",
        "meaning": ["向上", "增加", "準備完畢"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our total online revenue was up fifteen percent in the second quarter.",
            "zh": "我們第二季度的線上總營收成長了百分之十五。"
        },
        "mnemonic": "財報與業績常用 up 表增長，亦常搭配 set up (架設) 或 sign up (報名)。",
        "collocations": ["sign up", "set up"]
    },
    "some": {
        "phonetic": "/sʌm/",
        "pos": "determiner",
        "meaning": ["一些", "若干"],
        "topics": ["採購", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We need to order some replacement toner cartridges for the office printers.",
            "zh": "我們需要為辦公室印表機訂購一些備用碳粉匣。"
        },
        "mnemonic": "採購與庫存對話中常用的數量限定詞，指某些或若干用品。",
        "collocations": ["some of the", "some time"]
    },
    "other": {
        "phonetic": "/ˈʌðər/",
        "pos": "adjective",
        "meaning": ["其他的", "另外的"],
        "topics": ["商務會議", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The manager spoke with two other applicants before reaching a final hiring decision.",
            "zh": "經理在做出最終錄取決定之前，與另外兩位應徵者進行了晤談。"
        },
        "mnemonic": "商務對比或篩選人選常用的形容詞，常與 applicants 或 options 搭配。",
        "collocations": ["in other words", "each other"]
    },
    "out": {
        "phonetic": "/aʊt/",
        "pos": "adverb",
        "meaning": ["在外", "用盡", "不在辦公室"],
        "topics": ["採購", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The popular office chair is temporarily out of stock due to high customer demand.",
            "zh": "由於顧客需求量大，這款熱門辦公椅目前暫時缺貨。"
        },
        "mnemonic": "多益商務必考片語：out of stock (缺貨)、out of office (休假/不在辦公室)。",
        "collocations": ["out of stock", "out of order"]
    },
    "good": {
        "phonetic": "/ɡʊd/",
        "pos": "adjective",
        "meaning": ["良好的", "優良的", "有效的"],
        "topics": ["客戶服務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Maintaining good communication with our suppliers is vital for supply chain stability.",
            "zh": "與供應商保持良好溝通對於供應鏈的穩定至關重要。"
        },
        "mnemonic": "評價服務品質或產品狀況常用的基礎形容詞。",
        "collocations": ["good condition", "good service"]
    },
    "people": {
        "phonetic": "/ˈpiːpəl/",
        "pos": "noun",
        "meaning": ["人員", "員工", "人們"],
        "topics": ["人資招聘", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our human resources division seeks creative people with solid analytical skills.",
            "zh": "我們的人力資源部門正在尋找具備扎實分析能力的創新型人才。"
        },
        "mnemonic": "代表全體同仁或求職者的人才稱呼，商務中指具備專業能力的人才。",
        "collocations": ["sales people", "key people"]
    },
    "year": {
        "phonetic": "/jɪr/",
        "pos": "noun",
        "meaning": ["年", "年度", "會計年度"],
        "topics": ["付款財務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate profit margin improved considerably over the past fiscal year.",
            "zh": "在過去這一個會計年度中，企業的利潤率有了顯著提升。"
        },
        "mnemonic": "財務報表與績效回顧核心詞：fiscal year 代表會計年度。",
        "collocations": ["fiscal year", "calendar year"]
    },
    "take": {
        "phonetic": "/teɪk/",
        "pos": "verb",
        "meaning": ["花費(時間)", "採取(措施)", "搭乘"],
        "topics": ["公司政策", "機場交通"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Management must take immediate action to address workplace safety concerns.",
            "zh": "管理層必須立即採取行動以解決職場安全疑慮。"
        },
        "mnemonic": "多益常考搭配：take action (採取行動)、take advantage of (善用)。",
        "collocations": ["take action", "take advantage of"]
    },
    "well": {
        "phonetic": "/wɛl/",
        "pos": "adverb",
        "meaning": ["良好地", "充分地"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The product presentation went very well and received enthusiastic applause from investors.",
            "zh": "產品發表會進行得非常順利，並獲得投資人熱烈的掌聲。"
        },
        "mnemonic": "評估專案或表現常用的副詞，片語 as well as (以及) 多益極常見。",
        "collocations": ["as well as", "do well"]
    },
    "because": {
        "phonetic": "/bɪˈkɔːz/",
        "pos": "conjunction",
        "meaning": ["因為", "由於"],
        "topics": ["運輸物流", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The express shipment arrived late because the transport flight was grounded by fog.",
            "zh": "快捷貨件延遲送達，是因為運輸班機受到濃霧影響而停飛。"
        },
        "mnemonic": "說明業務延誤、退貨或取消原因的標準連接詞。",
        "collocations": ["because of", "just because"]
    },
    "very": {
        "phonetic": "/ˈvɛri/",
        "pos": "adverb",
        "meaning": ["非常", "很"],
        "topics": ["客戶服務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate client was very satisfied with our comprehensive technical support.",
            "zh": "該企業客戶對我們全面的技術支援服務感到非常滿意。"
        },
        "mnemonic": "加強形容詞語氣的程度副詞，常用於客戶滿意度調查。",
        "collocations": ["very much", "very pleased"]
    },
    "just": {
        "phonetic": "/dʒʌst/",
        "pos": "adverb",
        "meaning": ["剛剛", "正好", "僅僅"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The keynote speaker just finished setting up the projector for the presentation.",
            "zh": "主講嘉賓剛剛為簡報架設好了投影機。"
        },
        "mnemonic": "聽力 Part 1/2 常考時態提示詞，表剛剛完成或正好及時 (just in time)。",
        "collocations": ["just in time", "just now"]
    },
    "come": {
        "phonetic": "/kʌm/",
        "pos": "verb",
        "meaning": ["來臨", "附帶", "產生於"],
        "topics": ["採購", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Every brand new commercial copier comes with an all-inclusive two-year warranty.",
            "zh": "每台全新商用影印機皆附帶為期兩年的全包式保固。"
        },
        "mnemonic": "產品規格與購買條件必備句型：come with (隨附/附帶)。",
        "collocations": ["come with", "come up with"]
    },
    "work": {
        "phonetic": "/wɜːrk/",
        "pos": "verb",
        "meaning": ["工作", "運作", "處理"],
        "topics": ["辦公室", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "He will work closely with the design team to develop our new brand logo.",
            "zh": "他將與設計團隊緊密合作以開發我們的新品牌商標。"
        },
        "mnemonic": "職場核心動詞，搭配 work on (致力於)、work closely with (密切合作)。",
        "collocations": ["work on", "work closely with"]
    },
    "use": {
        "phonetic": "/juːz/",
        "pos": "verb",
        "meaning": ["使用", "運用", "利用"],
        "topics": ["生產設備", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Authorized technicians must use protective gear when operating the heavy machinery.",
            "zh": "合格技術人員在操作重型機具時必須穿戴防護裝備。"
        },
        "mnemonic": "操作設備與落實政策常見動詞，片語 make use of 意為善加利用。",
        "collocations": ["make use of", "use for"]
    },
    "now": {
        "phonetic": "/naʊ/",
        "pos": "adverb",
        "meaning": ["現在", "目前"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Early bird tickets for the international trade summit are now available online.",
            "zh": "國際貿易峰會的早鳥票現在已可於線上購買。"
        },
        "mnemonic": "活動公告高頻副詞，提示當前狀態或促銷開放時機。",
        "collocations": ["right now", "from now on"]
    },
    "then": {
        "phonetic": "/ðɛn/",
        "pos": "adverb",
        "meaning": ["然後", "接著", "那時"],
        "topics": ["辦公室", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please enter your employee credentials and then click the verification button.",
            "zh": "請輸入您的員工憑證，然後點擊驗證按鈕。"
        },
        "mnemonic": "工作流程步驟指南（SOP）中標示前後順序的連接詞。",
        "collocations": ["since then", "until then"]
    },
    "also": {
        "phonetic": "/ˈɔːlsoʊ/",
        "pos": "adverb",
        "meaning": ["也", "並且", "此外"],
        "topics": ["旅館住宿", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate retreat package covers lodging and also includes complimentary meals.",
            "zh": "企業研討營套裝方案涵蓋住宿，並且包含免費餐點。"
        },
        "mnemonic": "合約與宣傳文案補充福利常用的副詞，常配合 not only... but also。",
        "collocations": ["not only but also", "also known as"]
    },
    "into": {
        "phonetic": "/ˈɪntuː/",
        "pos": "preposition",
        "meaning": ["進入", "深入到", "轉化為"],
        "topics": ["行銷銷售", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The software enterprise plans to expand into emerging Southeast Asian markets.",
            "zh": "這家軟體企業計劃拓展進入新興的東南亞市場。"
        },
        "mnemonic": "多益商業擴張考點：expand into (打入市場) 或 look into (調查)。",
        "collocations": ["expand into", "look into"]
    },
    "only": {
        "phonetic": "/ˈoʊnli/",
        "pos": "adverb",
        "meaning": ["只有", "僅僅", "唯一的"],
        "topics": ["公司政策", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "This special corporate parking rate is available only to permanent staff members.",
            "zh": "此專案企業停車優惠僅提供給正職員工。"
        },
        "mnemonic": "規章政策限制條款的核心限定詞，強調專屬性或限制範圍。",
        "collocations": ["only if", "not only"]
    },
    "look": {
        "phonetic": "/lʊk/",
        "pos": "verb",
        "meaning": ["尋找", "注視", "看起來"],
        "topics": ["人資招聘", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our hiring managers are looking for candidates who demonstrate strong leadership.",
            "zh": "我們的招募經理正在尋找展現出卓越領導力的應徵者。"
        },
        "mnemonic": "求職與徵才極高頻片語：look for (尋找)、look forward to (期盼)。",
        "collocations": ["look for", "look forward to"]
    },
    "want": {
        "phonetic": "/wɑːnt/",
        "pos": "verb",
        "meaning": ["想要", "希望", "需求"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "If you want to update your delivery address, please contact customer support immediately.",
            "zh": "若您想要更新配送地址，請立即與客服中心聯繫。"
        },
        "mnemonic": "顧客服務信函常用句型：want to do something (想要做某事)。",
        "collocations": ["want to", "want someone to"]
    },
    "give": {
        "phonetic": "/ɡɪv/",
        "pos": "verb",
        "meaning": ["給予", "發表(簡報/演講)", "提供"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The vice president will give an opening speech at the regional sales conference.",
            "zh": "副總裁將在區域銷售會議上發表開幕致詞。"
        },
        "mnemonic": "多益聽力 Part 3/4 高頻搭配：give a presentation / give a speech (演講/簡報)。",
        "collocations": ["give a presentation", "give feedback"]
    },
    "first": {
        "phonetic": "/fɜːrst/",
        "pos": "adjective",
        "meaning": ["第一的", "最初的", "首要的"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "First quarter earnings reports revealed a ten percent increase in net operating profit.",
            "zh": "第一季財報顯示營業淨利成長了百分之十。"
        },
        "mnemonic": "季度財報專用語：first quarter 指第一季 (Q1)。",
        "collocations": ["first quarter", "first of all"]
    },
    "new": {
        "phonetic": "/nuː/",
        "pos": "adjective",
        "meaning": ["新的", "新進的"],
        "topics": ["人資招聘", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The human resources department scheduled an orientation session for all new employees.",
            "zh": "人力資源部門為所有新進員工安排了一場到職培訓說明會。"
        },
        "mnemonic": "多益職場聽力主角：new employee (新員工)、new product (新產品)。",
        "collocations": ["new employee", "new product"]
    },
    "way": {
        "phonetic": "/weɪ/",
        "pos": "noun",
        "meaning": ["方式", "途徑", "道路"],
        "topics": ["辦公室", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Implementing electronic billing is an efficient way to reduce paper waste.",
            "zh": "導入電子帳單是減少紙張浪費的一種有效途徑。"
        },
        "mnemonic": "商務提案必備詞彙：an efficient way to do something (做某事的有效方式)。",
        "collocations": ["in this way", "on the way"]
    },
    "find": {
        "phonetic": "/faɪnd/",
        "pos": "verb",
        "meaning": ["找到", "發現", "查明"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "You can find all previous project archives stored in the shared cloud folder.",
            "zh": "您可以在共享雲端資料夾中找到所有過往的專案存檔。"
        },
        "mnemonic": "商務對話與辦公指引常用詞，片語 find out 意為查明真相或獲得訊息。",
        "collocations": ["find out", "find a solution"]
    },
    "over": {
        "phonetic": "/ˈoʊvər/",
        "pos": "preposition",
        "meaning": ["超過", "在...期間", "遍及"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our overseas export volume has grown significantly over the past three years.",
            "zh": "在過去這三年期間，我們的海外出口量有了大幅增長。"
        },
        "mnemonic": "多益文法必考：over the past + 時間 (在過去...期間)，需搭配現在完成式。",
        "collocations": ["over the past", "over time"]
    },
    "any": {
        "phonetic": "/ˈɛni/",
        "pos": "determiner",
        "meaning": ["任何的", "若干"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please do not hesitate to reach out if you experience any technical difficulties.",
            "zh": "如果您遇到任何技術困難，請隨時與我們聯絡。"
        },
        "mnemonic": "商務信件結尾標準詢問：if you have any questions (若有任何問題)。",
        "collocations": ["any questions", "at any time"]
    },
    "after": {
        "phonetic": "/ˈæftər/",
        "pos": "preposition",
        "meaning": ["在...之後"],
        "topics": ["商務會議", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "A brief question-and-answer session will be held immediately after the keynote presentation.",
            "zh": "主旨演講結束後將隨即舉行簡短的問答環節。"
        },
        "mnemonic": "會議時程與交貨時間常用時間介系詞，表示在某活動之後。",
        "collocations": ["soon after", "after hours"]
    },
    "day": {
        "phonetic": "/deɪ/",
        "pos": "noun",
        "meaning": ["日", "白天", "工作天"],
        "topics": ["運輸物流", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Online purchases made before noon qualify for free same day delivery service.",
            "zh": "中午前完成的線上購物可享有當日免費宅配到府服務。"
        },
        "mnemonic": "物流出貨重點考詞：same day delivery (當日送達)、business day (工作天)。",
        "collocations": ["business day", "same day delivery"]
    },
    "thing": {
        "phonetic": "/θɪŋ/",
        "pos": "noun",
        "meaning": ["事項", "事物", "物件"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The first thing we should discuss on this morning's agenda is the quarterly expenditure.",
            "zh": "今天上午議程中我們首要討論的事項是季度支出。"
        },
        "mnemonic": "會議討論要點常用口語詞：the first thing on the agenda (議程首要事項)。",
        "collocations": ["first thing", "one more thing"]
    },
    "most": {
        "phonetic": "/moʊst/",
        "pos": "determiner",
        "meaning": ["大多數的", "最多的"],
        "topics": ["行銷銷售", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Most registered attendees arrived early to collect their seminar registration packets.",
            "zh": "大多數已報名的與會者都提早抵達以領取研討會報到資料袋。"
        },
        "mnemonic": "多益閱讀調查結果與問卷統計最常用的形容詞/代名詞。",
        "collocations": ["most of the", "at most"]
    },
    "need": {
        "phonetic": "/niːd/",
        "pos": "verb",
        "meaning": ["需要", "必要", "要求"],
        "topics": ["採購", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We need to order additional packaging materials to fulfill all pending client orders.",
            "zh": "我們需要訂購額外的包裝耗材以完成所有待處理的客戶訂單。"
        },
        "mnemonic": "採購與業務請購必備動詞，片語 in need of 意為需要。",
        "collocations": ["need to", "in need of"]
    },
    "much": {
        "phonetic": "/mʌtʃ/",
        "pos": "determiner",
        "meaning": ["大量的", "許多", "非常"],
        "topics": ["付款財務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "How much funding will be allocated to the employee wellness program this year?",
            "zh": "今年將提撥多少資金給員工身心健康計畫？"
        },
        "mnemonic": "詢問預算與花費的固定問法：how much + 不可數名詞。",
        "collocations": ["how much", "much more"]
    }
}
