# -*- coding: utf-8 -*-
"""批次 A: 300 個新單字中的前 100 個高品質 TOEIC 資料 (A2~B1)"""

DATA_BATCH_A = {
    "old": {
        "phonetic": "/oʊld/",
        "pos": "adjective",
        "meaning": ["舊的", "老舊的", "年長的"],
        "topics": ["生產設備", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The facility manager decided to replace the old computer servers with energy-efficient models.",
            "zh": "廠房主管決定將老舊的電腦伺服器更換為節能型機種。"
        },
        "mnemonic": "設備淘汰與更新對話常見詞：replace old equipment (更換老舊設備)。",
        "collocations": ["old equipment", "years old"]
    },
    "each": {
        "phonetic": "/iːtʃ/",
        "pos": "determiner",
        "meaning": ["每個", "各自的"],
        "topics": ["公司政策", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Each team member is expected to submit a weekly progress update by Friday afternoon.",
            "zh": "每位團隊成員均須在週五下午前提交每週進度更新報告。"
        },
        "mnemonic": "多益文法必考：each 後接單數名詞與單數動詞。",
        "collocations": ["each other", "each employee"]
    },
    "school": {
        "phonetic": "/skuːl/",
        "pos": "noun",
        "meaning": ["學校", "培訓學院"],
        "topics": ["人資招聘", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate foundation provides annual scholarships to local vocational school students.",
            "zh": "該企業基金會每年向在地職業學校的學生提供獎學金。"
        },
        "mnemonic": "企業社會責任 (CSR) 與實習招募常考單字。",
        "collocations": ["business school", "after school"]
    },
    "late": {
        "phonetic": "/leɪt/",
        "pos": "adjective",
        "meaning": ["遲到的", "晚期的", "延遲的"],
        "topics": ["機場交通", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Passengers arriving late for boarding will not be permitted to enter the aircraft.",
            "zh": "登機遲到的旅客將不被允許進入機艙。"
        },
        "mnemonic": "交通延誤與繳費罰款必考：late fee (滯納金/逾期罰款)。",
        "collocations": ["late fee", "arrive late"]
    },
    "high": {
        "phonetic": "/haɪ/",
        "pos": "adjective",
        "meaning": ["高的", "高級的", "高額的"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our new marketing strategy generated high customer engagement across digital platforms.",
            "zh": "我們的新行銷策略在各數位平台上帶來了高度的客戶參與。"
        },
        "mnemonic": "評價指標必備詞：high quality (高品質)、high priority (高優先級)。",
        "collocations": ["high quality", "high priority"]
    },
    "different": {
        "phonetic": "/ˈdɪfrənt/",
        "pos": "adjective",
        "meaning": ["不同的", "各式各樣的"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The sales team explored three different distribution channels to reach younger demographics.",
            "zh": "銷售團隊探索了三種不同的經銷管道以觸及年輕消費族群。"
        },
        "mnemonic": "方案比較常用詞：different from (與...不同)。",
        "collocations": ["different from", "different options"]
    },
    "off": {
        "phonetic": "/ɔːf/",
        "pos": "adverb",
        "meaning": ["休假", "折扣", "關閉"],
        "topics": ["行銷銷售", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All clearance items in the retail store are currently marked fifty percent off.",
            "zh": "零售店內的所有清倉商品目前皆標示為半價優惠。"
        },
        "mnemonic": "促銷打折最核心用語：20% off (打八折)；take a day off (請假一天)。",
        "collocations": ["percent off", "day off"]
    },
    "next": {
        "phonetic": "/nɛkst/",
        "pos": "adjective",
        "meaning": ["下一個的", "接下來的"],
        "topics": ["商務會議", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The next executive board meeting will be convened on the second Tuesday of November.",
            "zh": "下一次執行董事會會議將於十一月的第二個星期二召開。"
        },
        "mnemonic": "物流與時程關鍵詞：next day delivery (隔日配送)、next week (下週)。",
        "collocations": ["next day delivery", "next week"]
    },
    "end": {
        "phonetic": "/ɛnd/",
        "pos": "noun",
        "meaning": ["結束", "底端", "終點"],
        "topics": ["辦公室", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All departments must submit their annual expenditure reports before the end of December.",
            "zh": "所有部門必須在十二月底前提交年度支出報告。"
        },
        "mnemonic": "截止時間常考片語：by the end of the month (月底前)。",
        "collocations": ["end of the month", "at the end"]
    },
    "live": {
        "phonetic": "/lɪv/",
        "pos": "verb",
        "meaning": ["居住", "生活", "現場直播(adj)"],
        "topics": ["辦公室", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Many employees choose to live near the subway station to reduce their daily commute time.",
            "zh": "許多員工選擇住在捷運站附近以縮短每日通勤時間。"
        },
        "mnemonic": "員工通勤生活描寫動詞；亦可作形容詞 /laɪv/ live broadcast (現場直播)。",
        "collocations": ["live stream", "live broadcast"]
    },
    "while": {
        "phonetic": "/waɪl/",
        "pos": "conjunction",
        "meaning": ["當...的時候", "然而", "一段時間"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Please keep your mobile phones on silent while the training seminar is in progress.",
            "zh": "培訓研討會進行期間，請將手機保持靜音狀態。"
        },
        "mnemonic": "多益聽力會場公告高頻連接詞：while + 進行中事件。",
        "collocations": ["for a while", "once in a while"]
    },
    "world": {
        "phonetic": "/wɜːrld/",
        "pos": "noun",
        "meaning": ["世界", "全球"],
        "topics": ["行銷銷售", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our international freight service transports electronic parts to destinations around the world.",
            "zh": "我們的國際貨運服務將電子零組件運往世界各地的目的地。"
        },
        "mnemonic": "跨國企業文宣高頻片語：around the world / throughout the world (全球各地)。",
        "collocations": ["around the world", "world market"]
    },
    "week": {
        "phonetic": "/wiːk/",
        "pos": "noun",
        "meaning": ["星期", "週"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The newly hired interns will undergo intensive safety orientation over the next week.",
            "zh": "新聘實習生將在接下來的一週接受密集的安全到職訓練。"
        },
        "mnemonic": "時程規劃基礎詞：twice a week (每週兩次)、next week (下週)。",
        "collocations": ["next week", "twice a week"]
    },
    "play": {
        "phonetic": "/pleɪ/",
        "pos": "verb",
        "meaning": ["扮演(角色)", "播放", "玩"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Effective communication plays an essential role in fostering cross-departmental collaboration.",
            "zh": "有效的溝通在促進跨部門合作中扮演著至關重要的角色。"
        },
        "mnemonic": "多益職場閱讀極高頻片語：play an important role in (在...中扮演要角)。",
        "collocations": ["play a role", "play an important part"]
    },
    "home": {
        "phonetic": "/hoʊm/",
        "pos": "noun",
        "meaning": ["家", "住所", "居家辦公"],
        "topics": ["辦公室", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The company introduced a flexible policy that allows staff to work from home on Fridays.",
            "zh": "公司推出了一項彈性政策，允許員工在週五居家辦公。"
        },
        "mnemonic": "遠距辦公現代多益必考：work from home (WFH, 在家上班)。",
        "collocations": ["work from home", "home page"]
    },
    "never": {
        "phonetic": "/ˈnɛvər/",
        "pos": "adverb",
        "meaning": ["從未", "絕不"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Workers should never operate hazardous machinery without wearing the proper protective goggles.",
            "zh": "工人在未配戴適當防護護目鏡的情況下，絕不得操作危險機具。"
        },
        "mnemonic": "安全規章與禁令強調用語：should never do (絕不應當做某事)。",
        "collocations": ["never before", "almost never"]
    },
    "include": {
        "phonetic": "/ɪnˈkluːd/",
        "pos": "verb",
        "meaning": ["包含", "包括", "列入"],
        "topics": ["旅館住宿", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The room rate includes complimentary high-speed internet access and daily breakfast.",
            "zh": "房費包含免費高速網路連線與每日早餐。"
        },
        "mnemonic": "合約與費用明細核心字：tax included (含稅)、include breakfast (附早餐)。",
        "collocations": ["include tax", "include shipping"]
    },
    "course": {
        "phonetic": "/kɔːrs/",
        "pos": "noun",
        "meaning": ["課程", "路線", "過程"],
        "topics": ["人資招聘", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees who complete the online project management course will receive a recognized certificate.",
            "zh": "完成線上專案管理課程的員工將獲得認可的結業證書。"
        },
        "mnemonic": "在職訓練常用詞：training course (培訓課程)；of course (當然)。",
        "collocations": ["training course", "of course"]
    },
    "house": {
        "phonetic": "/haʊs/",
        "pos": "noun",
        "meaning": ["房屋", "機構", "內部(in-house)"],
        "topics": ["辦公室", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our creative department handles all graphic design in-house rather than hiring an external agency.",
            "zh": "我們的創意部門在內部自行處理所有平面設計，而非外聘外部機構。"
        },
        "mnemonic": "商務極高頻片語：in-house (公司內部自行處理的)。",
        "collocations": ["in-house training", "open house"]
    },
    "report": {
        "phonetic": "/rɪˈpɔːrt/",
        "pos": "noun",
        "meaning": ["報告", "報到(動詞)"],
        "topics": ["付款財務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The financial analyst finalized the quarterly earnings report ahead of the board meeting.",
            "zh": "財務分析師在董事會會議前完成了季度盈餘報告。"
        },
        "mnemonic": "職場最核心名詞/動詞：financial report (財報)、report to (向主管回報)。",
        "collocations": ["financial report", "report to"]
    },
    "group": {
        "phonetic": "/ɡruːp/",
        "pos": "noun",
        "meaning": ["小組", "集團", "團體"],
        "topics": ["商務會議", "旅館住宿"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Special discounted lodging rates are available for corporate travel groups of ten or more.",
            "zh": "十人以上的企業差旅團體可享有專案住宿折扣優惠。"
        },
        "mnemonic": "商務差旅考點：group rate / group discount (團體優惠價)。",
        "collocations": ["group rate", "working group"]
    },
    "case": {
        "phonetic": "/keɪs/",
        "pos": "noun",
        "meaning": ["情況", "案例", "案件", "箱"],
        "topics": ["客戶服務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "In case of severe weather emergencies, staff will be notified via our automated text alert system.",
            "zh": "萬一發生惡劣天候緊急狀況，將透過自動簡訊警報系統通知全體員工。"
        },
        "mnemonic": "多益必考條件句型：in case of (萬一發生/在...情況下)。",
        "collocations": ["in case of", "in any case"]
    },
    "woman": {
        "phonetic": "/ˈwʊmən/",
        "pos": "noun",
        "meaning": ["女士", "女性"],
        "topics": ["人資招聘", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The woman who gave the opening keynote speech serves as chief technology officer of the firm.",
            "zh": "發表開幕主題演講的女士擔任該公司的技術長。"
        },
        "mnemonic": "多益聽力短對話 Part 3 常見提問對象：What does the woman suggest?",
        "collocations": ["business woman", "young woman"]
    },
    "around": {
        "phonetic": "/əˈraʊnd/",
        "pos": "preposition",
        "meaning": ["大約", "在...周圍", "遍及"],
        "topics": ["付款財務", "機場交通"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The scheduled shuttle bus service departs from terminal one around every twenty minutes.",
            "zh": "定時接駁巴士大約每二十分鐘自第一航廈發車一次。"
        },
        "mnemonic": "聽力表示大約時間或費用常客：around three o'clock (大約三點)。",
        "collocations": ["around the clock", "all around"]
    },
    "book": {
        "phonetic": "/bʊk/",
        "pos": "verb",
        "meaning": ["預訂", "預約", "書籍(名詞)"],
        "topics": ["旅館住宿", "機場交通"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Business travelers are strongly advised to book their flight tickets at least two weeks in advance.",
            "zh": "強烈建議商務旅客至少提前兩週預訂機票。"
        },
        "mnemonic": "多益極高頻動詞！book = reserve (預約訂位)：book a flight, book a room。",
        "collocations": ["book a flight", "book a hotel"]
    },
    "family": {
        "phonetic": "/ˈfæməli/",
        "pos": "noun",
        "meaning": ["家庭", "家族"],
        "topics": ["公司政策", "旅館住宿"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The resort hotel provides spacious connecting suites tailored for guests traveling with family.",
            "zh": "該度假飯店提供專為攜眷出遊旅客設計的寬敞連通套房。"
        },
        "mnemonic": "人資福利與飯店套餐考點：family plan (家庭方案)、family leave (家庭照顧假)。",
        "collocations": ["family leave", "family plan"]
    },
    "seem": {
        "phonetic": "/siːm/",
        "pos": "verb",
        "meaning": ["似乎", "看來"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "There seems to be an error in the final calculation of the shipping charges on this invoice.",
            "zh": "這份發票上最終運費的計算似乎出現了一處錯誤。"
        },
        "mnemonic": "商務書信委婉提出問題的用語：There seems to be a problem。",
        "collocations": ["seem like", "seem to be"]
    },
    "let": {
        "phonetic": "/lɛt/",
        "pos": "verb",
        "meaning": ["讓", "准許"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please let the front desk clerk know if you require an iron or extra towels in your room.",
            "zh": "若您客房內需要熨斗或額外毛巾，請告知櫃檯接待人員。"
        },
        "mnemonic": "商務郵件高頻客氣句型：Please let me know (請告知我)。",
        "collocations": ["let someone know", "let someone in"]
    },
    "again": {
        "phonetic": "/əˈɡɛn/",
        "pos": "adverb",
        "meaning": ["再次", "重新"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We sincerely apologize for the inconvenience and thank you again for your patience.",
            "zh": "我們對造成的不便深表歉意，並再次感謝您的耐心配合。"
        },
        "mnemonic": "客服道歉信結尾高頻句：Thank you once again (再次感謝您)。",
        "collocations": ["once again", "never again"]
    },
    "kind": {
        "phonetic": "/kaɪnd/",
        "pos": "noun",
        "meaning": ["種類", "親切的(形容詞)"],
        "topics": ["客戶服務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "What kind of warranty coverage is provided with the commercial laser printer?",
            "zh": "這款商用雷射印表機隨附何種保固保障？"
        },
        "mnemonic": "詢問規格常用：what kind of (哪一種)；形容詞 kind assistance (親切協助)。",
        "collocations": ["what kind of", "kind regards"]
    },
    "keep": {
        "phonetic": "/kiːp/",
        "pos": "verb",
        "meaning": ["保持", "保留", "存檔"],
        "topics": ["公司政策", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please keep your original purchase receipts for at least thirty days to facilitate warranty claims.",
            "zh": "請妥善保留原始購買收據至少三十天，以便辦理保固理賠。"
        },
        "mnemonic": "商務溝通片語：keep in mind (牢記在心)、keep updated (隨時保持最新資訊)。",
        "collocations": ["keep in mind", "keep records"]
    },
    "hear": {
        "phonetic": "/hɪr/",
        "pos": "verb",
        "meaning": ["聽見", "得知"],
        "topics": ["人資招聘", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We were very pleased to hear that your company was awarded the regional trade contract.",
            "zh": "我們非常高興得知貴公司榮獲該區域貿易合約。"
        },
        "mnemonic": "商務社交致賀常客：hear from someone (收到某人來信/消息)。",
        "collocations": ["hear from", "hear about"]
    },
    "system": {
        "phonetic": "/ˈsɪstəm/",
        "pos": "noun",
        "meaning": ["系統", "制度"],
        "topics": ["生產設備", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate headquarters upgraded its internal payroll system to automate tax calculations.",
            "zh": "企業總部升級了內部薪資核算系統，以實現稅額自動計算。"
        },
        "mnemonic": "IT與辦公科技核心詞：computer system (電腦系統)、operating system (作業系統)。",
        "collocations": ["security system", "operating system"]
    },
    "every": {
        "phonetic": "/ˈɛvri/",
        "pos": "determiner",
        "meaning": ["每個", "每隔"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Safety inspectors conduct thorough maintenance checks on factory elevators every six months.",
            "zh": "安全檢查員每六個月對工廠電梯進行一次全面的維護檢查。"
        },
        "mnemonic": "頻率周期考點：every year (每年)、every six months (每六個月)。",
        "collocations": ["every other day", "every employee"]
    },
    "question": {
        "phonetic": "/ˈkwɛstʃən/",
        "pos": "noun",
        "meaning": ["問題", "疑問", "質疑(動詞)"],
        "topics": ["商務會議", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The seminar presenter will answer audience questions during the final twenty minutes of the session.",
            "zh": "研討會主講人將在會議最後二十分鐘回答現場觀眾的提問。"
        },
        "mnemonic": "會議問答標準詞：question and answer (Q&A 問答環節)。",
        "collocations": ["answer questions", "ask questions"]
    },
    "during": {
        "phonetic": "/ˈdʊrɪŋ/",
        "pos": "preposition",
        "meaning": ["在...期間"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees may purchase discounted meals in the company cafeteria during lunch hours.",
            "zh": "員工可以在午休時間於公司員工餐廳購買優惠餐點。"
        },
        "mnemonic": "多益介系詞大考點：during 後接表示期間的名詞 (如 during the meeting)。",
        "collocations": ["during the meeting", "during business hours"]
    },
    "always": {
        "phonetic": "/ˈɔːlweɪz/",
        "pos": "adverb",
        "meaning": ["總是", "一向"],
        "topics": ["客戶服務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our customer support agents are always ready to assist users with technical software issues.",
            "zh": "我們的客戶支援專員隨時準備好協助使用者解決軟體技術問題。"
        },
        "mnemonic": "企業承諾常見頻率副詞，表示持續不變的優質服務態度。",
        "collocations": ["as always", "always available"]
    },
    "big": {
        "phonetic": "/bɪɡ/",
        "pos": "adjective",
        "meaning": ["大的", "重大的"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Securing this overseas government contract was a big milestone for our growing business.",
            "zh": "拿下這筆海外政府合約是我們成長中企業的一個重大里程碑。"
        },
        "mnemonic": "形容商機或規模常用：big opportunity (大好良機)。",
        "collocations": ["big success", "big opportunity"]
    },
    "set": {
        "phonetic": "/sɛt/",
        "pos": "verb",
        "meaning": ["設定", "安排", "一套(名詞)"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The committee agreed to set a firm deadline for the submission of all design bids.",
            "zh": "委員會同意為所有設計競標文件的繳交設定嚴格的最後期限。"
        },
        "mnemonic": "極高頻職場片語：set a deadline (設定截止日期)、set up (架設/創立)。",
        "collocations": ["set a deadline", "set up"]
    },
    "small": {
        "phonetic": "/smɔːl/",
        "pos": "adjective",
        "meaning": ["小型的", "微小的"],
        "topics": ["行銷銷售", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The government launched an initiative to provide low-interest loans to small businesses.",
            "zh": "政府推出了一項向小型企業提供低利貸款的輔導方案。"
        },
        "mnemonic": "商業分類常見名詞：small business (中小型企業)。",
        "collocations": ["small business", "small amount"]
    },
    "study": {
        "phonetic": "/ˈstʌdi/",
        "pos": "noun",
        "meaning": ["研究", "調查", "學習(動詞)"],
        "topics": ["行銷銷售", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "A recent market study shows that consumers prefer eco-friendly packaging for cosmetics.",
            "zh": "最近一項市場研究顯示，消費者偏好化妝品採用環保包裝。"
        },
        "mnemonic": "多益報告常客：market study (市場研究)、conduct a study (進行研究)。",
        "collocations": ["market study", "conduct a study"]
    },
    "follow": {
        "phonetic": "/ˈfɑːloʊ/",
        "pos": "verb",
        "meaning": ["遵循", "跟隨", "追蹤"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All factory operators must strictly follow the safety instructions displayed on the bulletin board.",
            "zh": "所有工廠操作人員皆必須嚴格遵守公告欄上所張貼的安全守則。"
        },
        "mnemonic": "守規矩必備動詞：follow the guidelines / follow the rules (遵守規範)。",
        "collocations": ["follow guidelines", "follow up"]
    },
    "begin": {
        "phonetic": "/bɪˈɡɪn/",
        "pos": "verb",
        "meaning": ["開始", "著手"],
        "topics": ["商務會議", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The keynote presentation is scheduled to begin promptly at nine o'clock in the morning.",
            "zh": "主旨演講預定於上午九點整準時開始。"
        },
        "mnemonic": "會議活動開場動詞：begin promptly at (在...準時開始)。",
        "collocations": ["begin with", "begin promptly"]
    },
    "important": {
        "phonetic": "/ɪmˈpɔːrtnt/",
        "pos": "adjective",
        "meaning": ["重要的", "重大的"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The vice president will announce an important policy change during today's press conference.",
            "zh": "副總裁將在今日的記者會上宣布一項重大的政策變動。"
        },
        "mnemonic": "重要性說明標準詞：play an important role in (扮演要角)。",
        "collocations": ["important factor", "important role"]
    },
    "since": {
        "phonetic": "/sɪns/",
        "pos": "conjunction",
        "meaning": ["自從", "既然", "因為"],
        "topics": ["付款財務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Since the senior project manager was out of the office, her deputy led the client consultation.",
            "zh": "由於資深專案經理不在辦公室，由她的代理人主持客戶諮詢。"
        },
        "mnemonic": "多益雙重考法：表時間「自從」（搭配現在完成式）或表原因「既然/因為」。",
        "collocations": ["ever since", "since then"]
    },
    "run": {
        "phonetic": "/rʌn/",
        "pos": "verb",
        "meaning": ["經營", "運轉", "執行"],
        "topics": ["辦公室", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our marketing division plans to run a promotional campaign on popular social media platforms.",
            "zh": "我們的行銷部門計劃在熱門社群媒體平台上推行一場宣傳促銷活動。"
        },
        "mnemonic": "多益常考「經營管理/執行活動」：run a business (做生意), run a campaign。",
        "collocations": ["run a business", "run a campaign"]
    },
    "under": {
        "phonetic": "/ˈʌndər/",
        "pos": "preposition",
        "meaning": ["在...之下", "在...管理下"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The historical office complex is currently under renovation to improve accessibility for all visitors.",
            "zh": "這座歷史悠久的辦公園區目前正在整修中，以提升所有訪客的無障礙便利性。"
        },
        "mnemonic": "多益超高頻片語結構：under construction (施工中)、under warranty (在保固期內)。",
        "collocations": ["under warranty", "under construction"]
    },
    "turn": {
        "phonetic": "/tɜːrn/",
        "pos": "verb",
        "meaning": ["轉向", "轉變", "輪班(名詞)"],
        "topics": ["辦公室", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees must remember to turn off all air conditioning units and office lights before leaving.",
            "zh": "員工在離開辦公室前務必記得關閉所有冷氣機與辦公室照明。"
        },
        "mnemonic": "關閉與繳交設備動詞片語：turn off (關閉電源)、turn in (呈繳報告)。",
        "collocations": ["turn off", "turn in"]
    },
    "few": {
        "phonetic": "/fjuː/",
        "pos": "determiner",
        "meaning": ["很少的", "幾個(a few)"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Only a few tickets remain available for the annual charity banquet this weekend.",
            "zh": "本週末舉行的年度慈善晚宴目前僅剩為數不多的票券可供購買。"
        },
        "mnemonic": "修飾可數複數名詞：a few (少數幾個/一些)；few (幾乎沒有)。",
        "collocations": ["a few", "quite a few"]
    },
    "bring": {
        "phonetic": "/brɪŋ/",
        "pos": "verb",
        "meaning": ["帶來", "攜帶", "引進"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All workshop attendees should bring their employee identification badges to access the building.",
            "zh": "所有工作坊與會者皆應攜帶其員工識別證以進入大樓。"
        },
        "mnemonic": "商務會談常客：bring about (促成)、bring up (在會議中提出討論)。",
        "collocations": ["bring up", "bring about"]
    },
    "early": {
        "phonetic": "/ˈɜːrli/",
        "pos": "adjective",
        "meaning": ["早的", "提早的", "早期的"],
        "topics": ["行銷銷售", "機場交通"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Passengers who take advantage of our early booking discount can save up to thirty percent.",
            "zh": "善用我們早鳥預訂優惠的旅客最多可節省百分之三十的費用。"
        },
        "mnemonic": "多益促銷經典用法：early bird discount (早鳥優惠)。",
        "collocations": ["early bird", "early retirement"]
    },
    "hand": {
        "phonetic": "/hænd/",
        "pos": "noun",
        "meaning": ["手", "指針", "交給(動詞)"],
        "topics": ["辦公室", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please hand in your finalized expense reimbursement forms to the accounting department by noon.",
            "zh": "請於中午前將填寫完畢的差旅報銷單交至會計部門。"
        },
        "mnemonic": "辦公室交公文必備片語：hand in (繳交)、hand out (發放講義)。",
        "collocations": ["hand in", "hand out"]
    },
    "state": {
        "phonetic": "/steɪt/",
        "pos": "verb",
        "meaning": ["陳述", "說明", "狀態(名詞)"],
        "topics": ["公司政策", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The corporate contract clearly states that all cancellation requests must be submitted in writing.",
            "zh": "企業合約中明確陳述所有取消申請皆必須以書面方式提出。"
        },
        "mnemonic": "正式文件陳述條款動詞；名詞 state of the art (最先進的技術)。",
        "collocations": ["clearly state", "state of the art"]
    },
    "move": {
        "phonetic": "/muːv/",
        "pos": "verb",
        "meaning": ["移動", "搬遷", "措施(名詞)"],
        "topics": ["辦公室", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our regional marketing headquarters will move to a newly constructed office park next month.",
            "zh": "我們的區域行銷總部將於下個月搬遷至新建成的辦公園區。"
        },
        "mnemonic": "辦公室搬遷公告考點：move to a new location (搬遷至新址)。",
        "collocations": ["move forward", "move to"]
    },
    "money": {
        "phonetic": "/ˈmʌni/",
        "pos": "noun",
        "meaning": ["金錢", "款項"],
        "topics": ["付款財務", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We offer a thirty-day money-back guarantee if customers are not completely satisfied with the product.",
            "zh": "若客戶對產品不甚滿意，我們提供三十天內無條件全額退費保證。"
        },
        "mnemonic": "客戶退款保證標準詞彙：money-back guarantee (不滿意退費保證)。",
        "collocations": ["money-back guarantee", "save money"]
    },
    "fact": {
        "phonetic": "/fækt/",
        "pos": "noun",
        "meaning": ["事實", "真相"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The consultant presented verified facts and figures to support the corporate restructuring proposal.",
            "zh": "顧問提出了經過查證的事實與數據，以支持企業組織重整的提案。"
        },
        "mnemonic": "會議提案用片語：facts and figures (事實與數據)、in fact (事實上)。",
        "collocations": ["in fact", "facts and figures"]
    },
    "however": {
        "phonetic": "/haʊˈɛvər/",
        "pos": "adverb",
        "meaning": ["然而", "不過"],
        "topics": ["商務會議", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We intended to dispatch the shipment today; however, severe weather forced a temporary delay.",
            "zh": "我們原定今日發貨；然而，惡劣天候迫使出貨暫時延後。"
        },
        "mnemonic": "多益閱讀轉折語氣之王，標誌著條件受限或狀況生變。",
        "collocations": ["however however", "however possible"]
    },
    "area": {
        "phonetic": "/ˈɛriə/",
        "pos": "noun",
        "meaning": ["區域", "領域", "面積"],
        "topics": ["辦公室", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Unauthorized personnel are strictly prohibited from entering the chemical storage area.",
            "zh": "未經授權人員嚴禁進入化學品儲存區域。"
        },
        "mnemonic": "工廠安全區域標誌：restricted area (管制區)、smoking area (吸菸區)。",
        "collocations": ["reception area", "restricted area"]
    },
    "name": {
        "phonetic": "/neɪm/",
        "pos": "noun",
        "meaning": ["姓名", "名稱", "命名(動詞)"],
        "topics": ["人資招聘", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please print your full legal name clearly on the conference registration badge.",
            "zh": "請在研討會報到識別證上清晰正楷填寫您的法定全名。"
        },
        "mnemonic": "填表必備欄位：full name (全名)；brand name (品牌名稱)。",
        "collocations": ["brand name", "name tag"]
    },
    "read": {
        "phonetic": "/riːd/",
        "pos": "verb",
        "meaning": ["閱讀", "審閱"],
        "topics": ["公司政策", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees should carefully read the revised travel reimbursement policy before booking tickets.",
            "zh": "員工在訂票前應仔細審閱修訂後的差旅費報銷規定。"
        },
        "mnemonic": "簽約或實施政策常客：read carefully (仔細閱讀)。",
        "collocations": ["read carefully", "read through"]
    },
    "friend": {
        "phonetic": "/frɛnd/",
        "pos": "noun",
        "meaning": ["朋友", "友好(friendly)"],
        "topics": ["行銷銷售", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our current staff referral program offers cash incentives when you recommend a friend for an open position.",
            "zh": "我們的內部員工推薦計畫在您推薦朋友應徵職缺成功時提供現金獎勵。"
        },
        "mnemonic": "企業招募方案常用：refer a friend (推薦朋友求職)。",
        "collocations": ["user-friendly", "refer a friend"]
    },
    "month": {
        "phonetic": "/mʌnθ/",
        "pos": "noun",
        "meaning": ["月份", "月"],
        "topics": ["付款財務", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Utility invoices and office rental payments are due on the first day of each month.",
            "zh": "水電費帳單與辦公室租金於每個月的第一天到期應付。"
        },
        "mnemonic": "財務出帳周期：end of the month (月底)、last month (上個月)。",
        "collocations": ["next month", "end of the month"]
    },
    "large": {
        "phonetic": "/lɑːrdʒ/",
        "pos": "adjective",
        "meaning": ["大型的", "大量的"],
        "topics": ["行銷銷售", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The newly opened regional distribution hub can store a large inventory of consumer electronics.",
            "zh": "新啟用的區域經銷物流中心可存放大量的消費性電子產品庫存。"
        },
        "mnemonic": "描述規模常用：large quantity (大量)、at large (普遍地/整體而言)。",
        "collocations": ["large scale", "large number of"]
    },
    "business": {
        "phonetic": "/ˈbɪznəs/",
        "pos": "noun",
        "meaning": ["商業", "企業", "公事"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The regional sales manager will travel to London on business for three consecutive days.",
            "zh": "區域銷售經理將前往倫敦連續出差三天處理公務。"
        },
        "mnemonic": "多益最重要的字首之一：on business (出差)、business hours (營業時間)。",
        "collocations": ["business hours", "on business"]
    },
    "without": {
        "phonetic": "/wɪˈðaʊt/",
        "pos": "preposition",
        "meaning": ["沒有", "無...情況下"],
        "topics": ["公司政策", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Refunds cannot be issued for returned merchandise without an original store receipt.",
            "zh": "退換商品若未檢附原始店家收據，恕無法辦理退款。"
        },
        "mnemonic": "政策限制常見介系詞：without prior notice (恕不另行通知)。",
        "collocations": ["without notice", "without delay"]
    },
    "information": {
        "phonetic": "/ˌɪnfərˈmeɪʃən/",
        "pos": "noun",
        "meaning": ["資訊", "消息", "資料"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "For more detailed information regarding hotel amenities, please inquire at the front desk.",
            "zh": "欲了解更多關於飯店休閒設施的詳細資訊，請向接待櫃檯洽詢。"
        },
        "mnemonic": "多益不可數名詞大考點：for more information (如需更多資訊)。",
        "collocations": ["for more information", "contact information"]
    },
    "open": {
        "phonetic": "/ˈoʊpən/",
        "pos": "verb",
        "meaning": ["開啟", "開始營業", "開放的(adj)"],
        "topics": ["行銷銷售", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our downtown branch will officially open for business next Monday at eight-thirty.",
            "zh": "我們的市中心分行將於下週一上午八點半正式開門營業。"
        },
        "mnemonic": "開店與職缺核心詞：open for business (營業)、job opening (職缺)。",
        "collocations": ["open for business", "grand opening"]
    },
    "order": {
        "phonetic": "/ˈɔːrdər/",
        "pos": "noun",
        "meaning": ["訂單", "順序", "下訂(動詞)"],
        "topics": ["採購", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please include your confirmed order number when contacting customer service regarding delivery.",
            "zh": "就配送問題與客戶服務部聯繫時，請隨附您的確認訂單編號。"
        },
        "mnemonic": "商業採購核心考點：place an order (下訂單)、out of order (故障)。",
        "collocations": ["place an order", "order confirmation"]
    },
    "government": {
        "phonetic": "/ˈɡʌvərnmənt/",
        "pos": "noun",
        "meaning": ["政府", "政府部門"],
        "topics": ["公司政策", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The engineering corporation won a lucrative contract to build government infrastructure facilities.",
            "zh": "這家工程公司贏得了一項興建政府公共基礎設施的巨額標案。"
        },
        "mnemonic": "公家機關與投標常考：government regulation (政府規章)。",
        "collocations": ["government contract", "government regulation"]
    },
    "word": {
        "phonetic": "/wɜːrd/",
        "pos": "noun",
        "meaning": ["話語", "消息", "字詞"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Positive word of mouth from satisfied customers helped our new product gain market traction quickly.",
            "zh": "滿意顧客良好的口耳相傳，幫助我們的新產品迅速在市場上建立聲勢。"
        },
        "mnemonic": "行銷高頻必考片語：word of mouth (口碑行銷)。",
        "collocations": ["word of mouth", "in other words"]
    },
    "market": {
        "phonetic": "/ˈmɑːrkɪt/",
        "pos": "noun",
        "meaning": ["市場", "行銷(動詞)"],
        "topics": ["行銷銷售", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Conducting thorough market research is crucial prior to launching products overseas.",
            "zh": "在向海外推出產品之前，進行徹底的市場調查至關重要。"
        },
        "mnemonic": "商管必背字：market share (市場占有率)、market research (市調)。",
        "collocations": ["market share", "market research"]
    },
    "pay": {
        "phonetic": "/peɪ/",
        "pos": "verb",
        "meaning": ["支付", "付清", "薪水(名詞)"],
        "topics": ["付款財務", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Clients can pay their consulting invoices conveniently via electronic bank transfer.",
            "zh": "客戶可以透過電子銀行轉帳便捷地支付其顧問諮詢費用帳單。"
        },
        "mnemonic": "付款與注意力高頻動詞：pay by credit card (刷卡付款)、pay attention to (注意)。",
        "collocations": ["pay attention", "pay by credit card"]
    },
    "build": {
        "phonetic": "/bɪld/",
        "pos": "verb",
        "meaning": ["建造", "建立", "構築"],
        "topics": ["商務會議", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The enterprise strives to build lasting relationships with its corporate suppliers and clients.",
            "zh": "該企業致力於與其企業供應商及客戶建立長久穩固的合作關係。"
        },
        "mnemonic": "商務擴張與公關常用：build relationships (建立關係)。",
        "collocations": ["build relationships", "build a brand"]
    },
    "hold": {
        "phonetic": "/hoʊld/",
        "pos": "verb",
        "meaning": ["舉行(會議)", "握住", "稍候(電話)"],
        "topics": ["商務會議", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please hold the line while I transfer your call to the technical service department.",
            "zh": "請稍候別掛斷，我將為您把電話轉接至技術服務部。"
        },
        "mnemonic": "電話英語與主辦會議極高頻：hold the line (電話稍候)、hold a meeting (開會)。",
        "collocations": ["hold a meeting", "hold the line"]
    },
    "service": {
        "phonetic": "/ˈsɜːrvɪs/",
        "pos": "noun",
        "meaning": ["服務", "維修保養"],
        "topics": ["客戶服務", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our award-winning customer service department handles inquiries promptly around the clock.",
            "zh": "我們屢獲殊榮的客戶服務部門全天候迅速處理顧客諮詢。"
        },
        "mnemonic": "多益最重要的主題名詞：customer service (客服)、service charge (服務費)。",
        "collocations": ["customer service", "in service"]
    },
    "against": {
        "phonetic": "/əˈɡɛnst/",
        "pos": "preposition",
        "meaning": ["反對", "對照", "緊靠著"],
        "topics": ["商務會議", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Heavy equipment should be placed securely against the back wall of the factory storage bay.",
            "zh": "重型設備應穩固地放置在工廠倉儲區的後牆邊。"
        },
        "mnemonic": "多益聽力 Part 1 常見方位介系詞：leaning against the wall (靠在牆上)。",
        "collocations": ["against the law", "lean against"]
    },
    "believe": {
        "phonetic": "/bɪˈliːv/",
        "pos": "verb",
        "meaning": ["相信", "認為"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Industry experts believe that renewable solar energy adoption will accelerate over the coming decade.",
            "zh": "產業專家認為，在未來的十年間，再生太陽能的普及將會加速。"
        },
        "mnemonic": "商業演說表達樂觀展望時常用：believe that (深信/認為)。",
        "collocations": ["believe that", "firmly believe"]
    },
    "second": {
        "phonetic": "/ˈsɛkənd/",
        "pos": "adjective",
        "meaning": ["第二的", "秒(名詞)"],
        "topics": ["付款財務", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The second quarter fiscal earnings report will be presented to shareholders on Thursday.",
            "zh": "第二季度會計盈餘報告將於週四向股東呈報。"
        },
        "mnemonic": "財報與步驟標記詞：second quarter (第二季/Q2)、second floor (二樓)。",
        "collocations": ["second quarter", "second floor"]
    },
    "though": {
        "phonetic": "/ðoʊ/",
        "pos": "conjunction",
        "meaning": ["雖然", "儘管", "可是(副詞)"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Even though initial production was delayed, the engineering team finished the project ahead of schedule.",
            "zh": "儘管初期生產有所延誤，工程團隊仍提前完成了專案。"
        },
        "mnemonic": "轉折句型重點：even though (即使/儘管)。",
        "collocations": ["even though", "as though"]
    },
    "love": {
        "phonetic": "/lʌv/",
        "pos": "verb",
        "meaning": ["喜愛", "樂意"],
        "topics": ["客戶服務", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We would love to welcome your delegation to our annual international software summit.",
            "zh": "我們非常樂意歡迎貴代表團出席我們的年度國際軟體峰會。"
        },
        "mnemonic": "邀請函常用客氣句型：would love to (非常樂意做某事)。",
        "collocations": ["would love to", "love what you do"]
    },
    "job": {
        "phonetic": "/dʒɑːb/",
        "pos": "noun",
        "meaning": ["工作", "職位", "差事"],
        "topics": ["人資招聘", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Human resources published a job advertisement for a bilingual corporate communications specialist.",
            "zh": "人力資源部門刊登了一則徵求雙語企業傳播專員的徵才廣告。"
        },
        "mnemonic": "徵才招聘核心字：job opening (職缺)、job description (工作職責說明)。",
        "collocations": ["job opening", "job fair"]
    },
    "plan": {
        "phonetic": "/plæn/",
        "pos": "noun",
        "meaning": ["計畫", "方案", "規劃(動詞)"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate steering committee reviewed the proposed marketing plan during this morning's session.",
            "zh": "企業指導委員會在今天上午的會議中審查了擬定的行銷方案。"
        },
        "mnemonic": "職場規劃必備詞：business plan (商業計畫書)、plan to (打算做某事)。",
        "collocations": ["business plan", "plan to"]
    },
    "result": {
        "phonetic": "/rɪˈzʌlt/",
        "pos": "noun",
        "meaning": ["結果", "成效", "導致(動詞)"],
        "topics": ["行銷銷售", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "As a result of the targeted promotional campaign, third quarter retail sales surged twenty percent.",
            "zh": "由於精準推廣活動的成效，第三季零售額大幅增長了百分之二十。"
        },
        "mnemonic": "因果關係極高頻轉折片語：as a result of (由於...的結果)。",
        "collocations": ["as a result", "result in"]
    },
    "away": {
        "phonetic": "/əˈweɪ/",
        "pos": "adverb",
        "meaning": ["離開", "遠離", "出差中"],
        "topics": ["辦公室", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Mr. Sterling is currently away on a business trip, but his assistant can answer your inquiries.",
            "zh": "史特林先生目前出差在外，但他的助理可以回答您的洽詢。"
        },
        "mnemonic": "不在辦公室常用答覆：away on business (出差中)；right away (立刻)。",
        "collocations": ["away on business", "right away"]
    },
    "example": {
        "phonetic": "/ɪɡˈzæmpəl/",
        "pos": "noun",
        "meaning": ["範例", "榜樣"],
        "topics": ["商務會議", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The training seminar leader cited several successful examples of corporate brand turnaround.",
            "zh": "培訓研討會講師列舉了數個企業品牌成功轉型翻身的範例。"
        },
        "mnemonic": "會議舉例最常見片語：for example (例如)。",
        "collocations": ["for example", "set an example"]
    },
    "happen": {
        "phonetic": "/ˈhæpən/",
        "pos": "verb",
        "meaning": ["發生", "碰巧"],
        "topics": ["客戶服務", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "If a delivery disruption happens to occur, customers will receive immediate automated notification.",
            "zh": "萬一碰巧發生出貨配送中斷，顧客將收到即時自動通知。"
        },
        "mnemonic": "事件發生描寫動詞：happen to (碰巧)。",
        "collocations": ["happen to", "what happened"]
    },
    "offer": {
        "phonetic": "/ˈɔːfər/",
        "pos": "verb",
        "meaning": ["提供", "報價", "錄取通知(名詞)"],
        "topics": ["人資招聘", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We are delighted to offer you the position of senior financial analyst at our corporate headquarters.",
            "zh": "我們非常榮幸能向您提供企業總部資深財務分析師的職位。"
        },
        "mnemonic": "求職錄取與商業優惠必備：job offer (錄取通知)、special offer (特別優惠)。",
        "collocations": ["job offer", "special offer"]
    },
    "young": {
        "phonetic": "/jʌŋ/",
        "pos": "adjective",
        "meaning": ["年輕的", "新興的"],
        "topics": ["人資招聘", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The internship program provides promising young professionals with hands-on corporate experience.",
            "zh": "該實習計畫為極具潛力的年輕專業人士提供寶貴的企業實務經驗。"
        },
        "mnemonic": "實習培訓與消費市場客群詞彙：young professionals (青年專業人才)。",
        "collocations": ["young professionals", "young people"]
    },
    "close": {
        "phonetic": "/kloʊz/",
        "pos": "verb",
        "meaning": ["關閉", "打烊", "結案", "接近的(adj)"],
        "topics": ["行銷銷售", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The downtown commercial bank branch closes promptly at five o'clock on weekday afternoons.",
            "zh": "市中心商銀分行於平日下午五點整準時結束營業打烊。"
        },
        "mnemonic": "營業時間公告核心詞：close at 5 PM；片語 close a deal (達成交易)。",
        "collocations": ["close a deal", "close to"]
    },
    "program": {
        "phonetic": "/ˈproʊɡræm/",
        "pos": "noun",
        "meaning": ["計畫", "方案", "程式"],
        "topics": ["人資招聘", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All newly hired administrative employees must attend our comprehensive orientation program.",
            "zh": "所有新聘行政人員皆必須參加我們全面的到職培訓計畫。"
        },
        "mnemonic": "人資培訓方案：training program (培訓計畫)、loyalty program (會員積點計畫)。",
        "collocations": ["training program", "loyalty program"]
    },
    "lead": {
        "phonetic": "/liːd/",
        "pos": "verb",
        "meaning": ["領導", "帶領", "導致"],
        "topics": ["商務會議", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Ms. Reynolds was appointed to lead the international software development initiative.",
            "zh": "雷諾茲女士獲任命領導這項國際軟體開發倡議。"
        },
        "mnemonic": "多益職場領導力與因果搭配：lead to (導致)、lead a team (帶領團隊)。",
        "collocations": ["lead to", "lead a team"]
    },
    "buy": {
        "phonetic": "/baɪ/",
        "pos": "verb",
        "meaning": ["購買", "採購"],
        "topics": ["採購", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Corporate clients can buy office furniture in bulk to receive substantial volume discounts.",
            "zh": "企業客戶可以大宗批量購買辦公家具，以獲得豐厚的量大折扣。"
        },
        "mnemonic": "採購基礎動詞：buy in bulk (大宗購買)、buy online (線上購買)。",
        "collocations": ["buy in bulk", "buy online"]
    },
    "understand": {
        "phonetic": "/ˌʌndərˈstænd/",
        "pos": "verb",
        "meaning": ["理解", "明白", "體諒"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We completely understand your frustration regarding the unexpected shipment delay.",
            "zh": "我們非常能體諒您對於無預警貨物延誤所感到的沮喪。"
        },
        "mnemonic": "客服書信展現同理心必用動詞：understand your concern (體諒您的關切)。",
        "collocations": ["understand customer needs", "fully understand"]
    },
    "thank": {
        "phonetic": "/θæŋk/",
        "pos": "verb",
        "meaning": ["感謝", "致謝"],
        "topics": ["客戶服務", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We would like to thank all participating vendors for their valuable contributions to the trade expo.",
            "zh": "我們由衷感謝所有參展廠商對本次貿易博覽會所做出的寶貴貢獻。"
        },
        "mnemonic": "商務社交信函第一句或結尾句：Thank you for your cooperation (感謝您的合作)。",
        "collocations": ["thank you for", "thank in advance"]
    },
    "far": {
        "phonetic": "/fɑːr/",
        "pos": "adverb",
        "meaning": ["遠地", "極大地", "遙遠的(adj)"],
        "topics": ["機場交通", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate conference center is not far from the international airport terminals.",
            "zh": "該企業會議中心距離國際機場航廈並不遙遠。"
        },
        "mnemonic": "多益聽力短對話方位詞：not far from (離...不遠)；as far as (就...而言)。",
        "collocations": ["as far as", "not far from"]
    },
    "today": {
        "phonetic": "/təˈdeɪ/",
        "pos": "noun",
        "meaning": ["今天", "今日"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Order your replacement supplies today to qualify for free express courier dispatch.",
            "zh": "今日下單訂購您的耗材補充品，即可享有免費快捷快遞出貨服務。"
        },
        "mnemonic": "促銷呼籲行動常客：call us today (今天就致電我們)。",
        "collocations": ["starting today", "as of today"]
    },
    "hour": {
        "phonetic": "/ˈaʊər/",
        "pos": "noun",
        "meaning": ["小時", "營業時間(hours)"],
        "topics": ["辦公室", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Standard corporate office hours are from nine in the morning until five in the evening.",
            "zh": "標準企業辦公營業時間為上午九點至下午五點。"
        },
        "mnemonic": "營業與辦公時間多益必考：business hours / office hours (營業/辦公時間)。",
        "collocations": ["business hours", "rush hour"]
    },
    "student": {
        "phonetic": "/ˈstuːdnt/",
        "pos": "noun",
        "meaning": ["學生", "學員"],
        "topics": ["人資招聘", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Full-time university students are eligible for a twenty percent discount on exhibition passes.",
            "zh": "全職大學生可享有展覽入場證八折優惠。"
        },
        "mnemonic": "學生票價促銷與實習生招募考點：student discount (學生優惠)。",
        "collocations": ["student discount", "college student"]
    },
    "face": {
        "phonetic": "/feɪs/",
        "pos": "verb",
        "meaning": ["面臨", "面向", "面容(名詞)"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Local retailers face intense competition from multinational online e-commerce platforms.",
            "zh": "在地零售商正面臨來自跨國線上電商平台的激烈競爭。"
        },
        "mnemonic": "多益職場商業挑戰動詞：face challenges / face competition (面臨挑戰/競爭)。",
        "collocations": ["face to face", "face challenges"]
    },
    "hope": {
        "phonetic": "/hoʊp/",
        "pos": "verb",
        "meaning": ["希望", "期盼"],
        "topics": ["商務會議", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We hope to conclude the contract negotiations with the overseas supplier by Friday.",
            "zh": "我們期盼能在週五之前敲定與海外供應商的合約談判。"
        },
        "mnemonic": "商務書信期許句型：We hope that... / hope to do something。",
        "collocations": ["hope to", "hope for the best"]
    }
}
