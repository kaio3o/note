# -*- coding: utf-8 -*-
"""批次 200-2b: 50 個單字 (federal .. predict) 高品質 TOEIC 資料"""

BATCH_2B = {
    "federal": {
        "phonetic": "/ˈfedərəl/",
        "pos": "adjective",
        "meaning": ["聯邦的", "中央政府的"],
        "topics": ["公司政策", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "All domestic corporate financial statements must strictly comply with federal tax laws.",
            "zh": "所有國內企業的財務報表均必須嚴格遵守聯邦稅法規定。"
        },
        "mnemonic": "聯邦規範與稅務：federal tax (聯邦稅)、federal regulation (聯邦法規)。",
        "collocations": ["federal regulation", "federal government"],
        "roots": ["feder- 聯盟、盟約", "-al 形容詞"]
    },
    "reveal": {
        "phonetic": "/rɪˈviːl/",
        "pos": "verb",
        "meaning": ["揭露", "顯示", "公布"],
        "topics": ["商務會議", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The internal corporate financial audit revealed several opportunities for cost optimization.",
            "zh": "企業內部財務查核結果顯示了數個可供成本優化的絕佳機會。"
        },
        "mnemonic": "re- (反、回) + veal (面紗) ＝ 掀開面紗 ＝ 揭曉、揭露。",
        "collocations": ["reveal information", "survey reveals"],
        "roots": ["re- 反向", "vel- 面紗、覆蓋"]
    },
    "percentage": {
        "phonetic": "/pərˈsentɪdʒ/",
        "pos": "noun",
        "meaning": ["百分比", "比例", "抽成"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "A significant percentage of quarterly corporate revenue is reinvested in research initiatives.",
            "zh": "企業季度營收中有相當高的百分比被重新投入於研發計畫中。"
        },
        "mnemonic": "percent (百分之...) + -age (名詞總稱) ＝ 百分比率。",
        "collocations": ["high percentage", "percentage of"],
        "roots": ["per- 每", "cent- 百", "-age 名詞"]
    },
    "peace": {
        "phonetic": "/piːs/",
        "pos": "noun",
        "meaning": ["平靜", "和平", "安心(peace of mind)"],
        "topics": ["客戶服務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Our comprehensive equipment warranty gives corporate clients complete peace of mind.",
            "zh": "我們全面的設備保固服務為企業客戶帶來完全的安心保障。"
        },
        "mnemonic": "行銷與保固文案極常見搭配：peace of mind (安心、無後顧之憂)。",
        "collocations": ["peace of mind", "peaceful environment"]
    },
    "status": {
        "phonetic": "/ˈsteɪtəs/",
        "pos": "noun",
        "meaning": ["進度狀態", "地位", "身分"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Customers can track the real-time delivery status of their shipments through our portal.",
            "zh": "客戶可透過我們的入口網站即時追蹤其貨物的運送處理狀態。"
        },
        "mnemonic": "stat- (站立、處於) ＝ 事情目前所處的狀況 ＝ 進度狀態 (project status)。",
        "collocations": ["status report", "current status"],
        "roots": ["sta- 站立、處於", "-us 名詞"]
    },
    "crime": {
        "phonetic": "/kraɪm/",
        "pos": "noun",
        "meaning": ["犯罪", "違法行為", "資安犯罪(cybercrime)"],
        "topics": ["公司政策", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The bank invested millions into cutting-edge cybersecurity to combat financial cybercrime.",
            "zh": "該銀行斥資數百萬美元建置先進網路資安系統，以打擊金融科技犯罪。"
        },
        "mnemonic": "資安防護與法規考點：cybercrime (網路犯罪)、fight crime。",
        "collocations": ["cyber crime", "prevent crime"]
    },
    "decline": {
        "phonetic": "/dɪˈklaɪn/",
        "pos": "verb",
        "meaning": ["下降", "衰退", "婉拒", "下滑(名詞)"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The regional sales manager had to decline the invitation due to a scheduling conflict.",
            "zh": "該區域業務經理因行程衝突而不得不婉拒該項邀請。"
        },
        "mnemonic": "de- (向下) + clin (傾斜) ＝ 向下傾斜 ＝ 下降；禮貌婉拒邀請 (decline an offer)。",
        "collocations": ["decline an invitation", "sharp decline"],
        "roots": ["de- 向下", "clin- 傾斜"]
    },
    "decade": {
        "phonetic": "/ˈdekeɪd/",
        "pos": "noun",
        "meaning": ["十年", "十年期間"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Over the past decade, our automotive manufacturing company has doubled its export volume.",
            "zh": "在過去十年間，我們的汽車製造公司的出口貿易量已實現翻倍成長。"
        },
        "mnemonic": "dec- (十) + -ade (名詞) ＝ 十年期間 (over the past decade)。",
        "collocations": ["past decade", "last decade"],
        "roots": ["dec- 十", "-ade 名詞"]
    },
    "launch": {
        "phonetic": "/lɔːntʃ/",
        "pos": "verb",
        "meaning": ["發表/推出(產品)", "發起(活動)", "上市發表會(名詞)"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The technology startup plans to launch its flagship smartphone application next month.",
            "zh": "這家科技新創公司計劃於下個月正式推出其旗艦智慧型手機應用程式。"
        },
        "mnemonic": "產品上市行銷核心詞：launch a product (發表產品)、product launch (產品發表會)。",
        "collocations": ["launch a campaign", "product launch"]
    },
    "warn": {
        "phonetic": "/wɔːrn/",
        "pos": "verb",
        "meaning": ["警告", "提醒", "預先告誡"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Safety signs prominently warn plant technicians to wear protective eyewear at all times.",
            "zh": "安全警示標誌醒目地提醒廠區技術人員必須隨時配戴護目鏡。"
        },
        "mnemonic": "名詞 warning (警報/警告通知)；warn someone about/of (提醒某人某事)。",
        "collocations": ["warn about", "warn in advance"]
    },
    "consumer": {
        "phonetic": "/kənˈsuːmər/",
        "pos": "noun",
        "meaning": ["消費者", "顧客"],
        "topics": ["行銷銷售", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Extensive consumer behavior market surveys helped guide the design of our new packaging.",
            "zh": "廣泛的消費者行為市場調查引導了我們新包裝的設計方向。"
        },
        "mnemonic": "consume (消費、消耗) + -er (人) ＝ 消費者 (consumer confidence / goods)。",
        "collocations": ["consumer demand", "consumer goods"],
        "roots": ["con- 共同", "sum- 拿取、花費", "-er 人"]
    },
    "favor": {
        "phonetic": "/ˈfeɪvər/",
        "pos": "noun",
        "meaning": ["支持", "偏袒", "幫忙", "偏愛/贊成(動詞)"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "A clear majority of board members voted in favor of the international joint venture.",
            "zh": "大多數董事會成員投票贊成這項跨國合資合作案。"
        },
        "mnemonic": "商務表決極高頻片語：in favor of (贊成、支持)；ask a favor (請求協助)。",
        "collocations": ["in favor of", "do a favor"]
    },
    "dry": {
        "phonetic": "/draɪ/",
        "pos": "adjective",
        "meaning": ["乾燥的", "使乾燥(動詞)", "乾洗(dry clean)"],
        "topics": ["旅館住宿", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Hotel guests may drop off executive business garments for same-day dry cleaning service.",
            "zh": "飯店房客可送交商務西裝衣物以享受當日送交取件的乾洗服務。"
        },
        "mnemonic": "飯店服務常用：dry cleaning (乾洗服務)；dry storage (乾貨常溫存放)。",
        "collocations": ["dry cleaning", "keep dry"]
    },
    "partner": {
        "phonetic": "/ˈpɑːrtnər/",
        "pos": "noun",
        "meaning": ["合作夥伴", "合夥人", "與...合作(動詞)"],
        "topics": ["商務會議", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "We established a long-term strategic partnership with a reliable regional logistics provider.",
            "zh": "我們與一家可靠的區域物流供應商建立了長期戰略合作夥伴關係。"
        },
        "mnemonic": "part (部分、股份) + -ner (人) ＝ 共同持股共事的人 ＝ 夥伴 (business partner)。",
        "collocations": ["business partner", "strategic partner"]
    },
    "institution": {
        "phonetic": "/ˌɪnstɪˈtuːʃn/",
        "pos": "noun",
        "meaning": ["機構", "體制", "金融機構"],
        "topics": ["付款財務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Leading financial institutions tightened corporate loan qualification standards this year.",
            "zh": "各大主要金融機構於今年收緊了企業貸款審核資格標準。"
        },
        "mnemonic": "in- (向內) + statut- (設立) + -ion ＝ 設立的公法人組織 ＝ 金融/學術機構。",
        "collocations": ["financial institution", "academic institution"],
        "roots": ["in- 進入", "stat- 建立、站立", "-ion 名詞"]
    },
    "spot": {
        "phonetic": "/spɑːt/",
        "pos": "noun",
        "meaning": ["地點", "車位(parking spot)", "發現/注意到(動詞)"],
        "topics": ["機場交通", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Reserved parking spots are designated specifically for carpool employees and corporate clients.",
            "zh": "預留的專屬停車格位專門規劃給共乘員工與企業客戶使用。"
        },
        "mnemonic": "停車位與現場：parking spot (停車位)、on the spot (當場)。",
        "collocations": ["parking spot", "on the spot"]
    },
    "horse": {
        "phonetic": "/hɔːrs/",
        "pos": "noun",
        "meaning": ["馬匹", "馬力(horsepower)"],
        "topics": ["生產設備", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The industrial plant installed a high-efficiency motor with superior horsepower capability.",
            "zh": "該工業廠區安裝了一台具備卓越馬力效能的高效率馬達。"
        },
        "mnemonic": "工業機械規格常用複合詞：horsepower (馬力，簡寫 HP)。",
        "collocations": ["horsepower", "horse racing"]
    },
    "eventually": {
        "phonetic": "/ɪˈventʃuəli/",
        "pos": "adverb",
        "meaning": ["最終", "終於"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Protracted contract negotiations eventually led to a mutually beneficial long-term agreement.",
            "zh": "長期的合約磋商談判最終促成了一項互利共贏的長期協議。"
        },
        "mnemonic": "event (事件、結果) + -ual + -ly ＝ 事件發展到最後 ＝ 最終。",
        "collocations": ["eventually lead to", "eventually succeed"],
        "roots": ["e- 出", "vent- 來", "-ly 副詞"]
    },
    "heat": {
        "phonetic": "/hiːt/",
        "pos": "noun",
        "meaning": ["熱度", "暖氣", "加熱(動詞)"],
        "topics": ["旅館住宿", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Hotel room heating and air conditioning controls can be regulated using the bedside thermostat.",
            "zh": "客房的暖氣與空調系統可透過床頭溫控器自行調節。"
        },
        "mnemonic": "飯店與工廠設施：heat wave (熱浪)、central heating (中央暖氣)。",
        "collocations": ["central heating", "heat wave"]
    },
    "excite": {
        "phonetic": "/ɪkˈsaɪt/",
        "pos": "verb",
        "meaning": ["使興奮", "激勵", "引起大眾興趣"],
        "topics": ["行銷銷售", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The innovative technological breakthrough excited technology investors across the globe.",
            "zh": "該項創新的技術突破激發了全球科技投資人的極大熱情與興趣。"
        },
        "mnemonic": "ex- (出) + cite (召喚、驅動) ＝ 召喚出熱情 ＝ 激勵 (exciting news)。",
        "collocations": ["excite investors", "greatly excite"],
        "roots": ["ex- 出", "cit- 召喚、喚起"]
    },
    "reader": {
        "phonetic": "/ˈriːdər/",
        "pos": "noun",
        "meaning": ["讀者", "讀卡機/閱讀器(card reader)"],
        "topics": ["辦公室", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees must scan their electronic identification badges across the door badge reader.",
            "zh": "員工進出時必須在門禁感應讀卡機前刷其電子識別證。"
        },
        "mnemonic": "多益雙考點：雜誌讀者 (readers) 或感應讀卡機 (card reader)。",
        "collocations": ["card reader", "general reader"]
    },
    "importance": {
        "phonetic": "/ɪmˈpɔːrtns/",
        "pos": "noun",
        "meaning": ["重要性", "重大意義"],
        "topics": ["商務會議", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The executive director underscored the crucial importance of maintaining workplace safety standards.",
            "zh": "執行主管強調了嚴格貫徹職場安全維護標準的關鍵重要性。"
        },
        "mnemonic": "important 的名詞形式；搭配 attach importance to (重視某事)。",
        "collocations": ["vital importance", "paramount importance"],
        "roots": ["in- 進入", "port- 攜帶", "-ance 名詞"]
    },
    "distance": {
        "phonetic": "/ˈdɪstəns/",
        "pos": "noun",
        "meaning": ["距離", "路程", "遠距離的(形容詞)"],
        "topics": ["機場交通", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The convention hotel is situated within easy walking distance of the central metro station.",
            "zh": "會議飯店地理位置極佳，距離中央捷運站僅需步行即可輕鬆抵達。"
        },
        "mnemonic": "多益飯店/位置常見搭配：within walking distance (步行可達距離)。",
        "collocations": ["walking distance", "long distance"],
        "roots": ["dis- 分開", "sta- 站立", "-ance 名詞"]
    },
    "guide": {
        "phonetic": "/ɡaɪd/",
        "pos": "noun",
        "meaning": ["指南", "導遊/專人引導", "引導/指導(動詞)"],
        "topics": ["客戶服務", "辦公室"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The human resources handbook serves as a comprehensive guide for all newly onboarded staff.",
            "zh": "這本人力資源員工手冊為所有新到職員工提供了全面的指引方針。"
        },
        "mnemonic": "使用者手冊或指引：user guide (使用手冊)、tour guide (導遊專員)。",
        "collocations": ["user guide", "tour guide"]
    },
    "grant": {
        "phonetic": "/ɡrænt/",
        "pos": "noun",
        "meaning": ["補助金", "專款", "准予/授予(動詞)"],
        "topics": ["付款財務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our biotechnology startup was awarded a substantial government research innovation grant.",
            "zh": "我們的生技新創公司獲頒了一筆可觀的政府研發創新專款補助金。"
        },
        "mnemonic": "多益雙重核心義：名詞指政府研究補助款 (research grant)；動詞指准許 (grant permission)。",
        "collocations": ["research grant", "grant permission"]
    },
    "taxi": {
        "phonetic": "/ˈtæksi/",
        "pos": "noun",
        "meaning": ["計程車", "滑行(飛機地面動詞)"],
        "topics": ["機場交通", "旅館住宿"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The hotel concierge can arrange a direct taxi transfer to the airport terminal.",
            "zh": "飯店禮賓服務台可為貴賓安排直達機場航廈的計程車接駁服務。"
        },
        "mnemonic": "出差差旅必考：taxi stand (計程車招呼站)、taxi receipt (搭車報銷收據)。",
        "collocations": ["taxi stand", "take a taxi"]
    },
    "feed": {
        "phonetic": "/fiːd/",
        "pos": "verb",
        "meaning": ["餵食", "供應/輸入(資料)", "資訊摘要串/即時饋送(名詞)"],
        "topics": ["辦公室", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Automated conveyor belts continuously feed raw plastic materials into the molding machine.",
            "zh": "自動輸送帶持續不斷地將塑膠原物料送入模具成型機中。"
        },
        "mnemonic": "動詞指原料/資料輸入 (feed data into)；名詞 news feed (動態消息摘要串)。",
        "collocations": ["feed into", "live feed"]
    },
    "pain": {
        "phonetic": "/peɪn/",
        "pos": "noun",
        "meaning": ["痛苦", "痛點(pain point)", "費盡心思(take pains)"],
        "topics": ["客戶服務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our digital software solution directly addresses the primary operational pain points of retail clients.",
            "zh": "我們的數位軟體解決方案直接針對零售客戶的主要營運痛點對症下藥。"
        },
        "mnemonic": "行銷業務分析必備詞彙：customer pain points (客戶痛點需求)。",
        "collocations": ["pain point", "take pains"]
    },
    "sector": {
        "phonetic": "/ˈsektər/",
        "pos": "noun",
        "meaning": ["部門", "行業領域", "板塊"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Employment hiring demand remains exceptionally resilient across the renewable clean energy sector.",
            "zh": "在可再生潔淨能源產業部門中，人才招聘需求依然展現出極強的韌性。"
        },
        "mnemonic": "sect- (切開、劃分) + -or ＝ 劃分出的產業區塊 ＝ 產業部門 (public/private sector)。",
        "collocations": ["private sector", "public sector"],
        "roots": ["sect- 切、劃分", "-or 物/範疇"]
    },
    "mistake": {
        "phonetic": "/mɪˈsteɪk/",
        "pos": "noun",
        "meaning": ["錯誤", "過失", "誤會/弄錯(動詞)"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The billing clerk apologized promptly for the invoice calculation mistake and issued a credit.",
            "zh": "會計出納人員對發票計算上的錯誤迅速致歉，並開立了折讓單。"
        },
        "mnemonic": "mis- (錯誤) + take (拿、處理) ＝ 弄錯、做錯 (make a mistake)。",
        "collocations": ["make a mistake", "by mistake"],
        "roots": ["mis- 錯誤", "take 拿取"]
    },
    "ensure": {
        "phonetic": "/ɪnˈʃʊr/",
        "pos": "verb",
        "meaning": ["確保", "保證"],
        "topics": ["公司政策", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Rigorous quality inspections ensure that every outbound shipment meets strict international standards.",
            "zh": "嚴密的品質檢驗確保每一批出境貨物均完全符合嚴格的國際標準規範。"
        },
        "mnemonic": "en- (使...) + sure (確定) ＝ 使之萬無一失 ＝ 確保 (ensure compliance)。",
        "collocations": ["ensure compliance", "ensure safety"],
        "roots": ["en- 使成為", "sur- 確定"]
    },
    "satisfy": {
        "phonetic": "/ˈsætɪsfaɪ/",
        "pos": "verb",
        "meaning": ["使滿意", "滿足(需求/條件)"],
        "topics": ["客戶服務", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our expanded product range is tailored specifically to satisfy evolving client demands.",
            "zh": "我們擴大推出的產品系列專門量身打造，以滿足客戶不斷變化的需求。"
        },
        "mnemonic": "satis (足夠) + -fy (使...) ＝ 使之感到足夠 ＝ 滿足要求 (satisfy requirements)。",
        "collocations": ["satisfy requirements", "satisfy customers"],
        "roots": ["satis- 足夠", "-fy 使成為"]
    },
    "chief": {
        "phonetic": "/tʃiːf/",
        "pos": "adjective",
        "meaning": ["主要的", "首席的", "長官/首長(名詞)"],
        "topics": ["人資招聘", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The chief executive officer delivered the keynote strategy presentation at the annual meeting.",
            "zh": "執行長在年度股東會議上發表了核心戰略主題報告。"
        },
        "mnemonic": "高階主管頭銜必備：chief executive officer (CEO)、chief financial officer (CFO)。",
        "collocations": ["chief executive", "chief officer"],
        "roots": ["cap- / capit- 頭 (法語源 chief)"]
    },
    "cool": {
        "phonetic": "/kuːl/",
        "pos": "adjective",
        "meaning": ["涼爽的", "冷靜的", "冷卻(動詞)"],
        "topics": ["生產設備", "旅館住宿"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "All electronic server rooms must be kept in a cool, climate-controlled environment.",
            "zh": "所有電子伺服器機房均必須保持在涼爽且恆溫恆濕的空調環境中。"
        },
        "mnemonic": "設備維護環境：keep cool (保持涼爽)、cooling system (冷卻散熱系統)。",
        "collocations": ["keep cool", "cooling system"]
    },
    "expert": {
        "phonetic": "/ˈekspɜːrt/",
        "pos": "noun",
        "meaning": ["專家", "內行", "熟練的/專家的(形容詞)"],
        "topics": ["人資招聘", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "We hired an independent cybersecurity expert to conduct a thorough vulnerability penetration audit.",
            "zh": "我們聘請了一位獨立的資安專家進行全面的系統漏洞滲透查核。"
        },
        "mnemonic": "ex- (出) + peri (嘗試、經驗) ＝ 經驗極豐富的人 ＝ 專家 (expert advice)。",
        "collocations": ["industry expert", "expert advice"],
        "roots": ["ex- 出", "peri- 嘗試、經驗"]
    },
    "wave": {
        "phonetic": "/weɪv/",
        "pos": "noun",
        "meaning": ["浪潮", "揮手(動詞)", "波浪"],
        "topics": ["行銷銷售", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The newly released generative artificial intelligence tools sparked a massive wave of technological innovation.",
            "zh": "新發表的生成式人工智慧工具引發了一股波瀾壯闊的技術創新浪潮。"
        },
        "mnemonic": "趨勢與潮湧：wave of innovation (創新浪潮)、heat wave (熱浪)。",
        "collocations": ["wave of", "heat wave"]
    },
    "south": {
        "phonetic": "/saʊθ/",
        "pos": "noun",
        "meaning": ["南方", "南方的(形容詞)", "向南(副詞)"],
        "topics": ["機場交通", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The regional distribution logistics terminal is located ten kilometers south of the airport.",
            "zh": "該區域物流集散航廈位於機場以南約十公里處。"
        },
        "mnemonic": "方位導引與出差位置：south of (在...之南)、South America (南美洲)。",
        "collocations": ["south of", "South Wing"]
    },
    "labor": {
        "phonetic": "/ˈleɪbər/",
        "pos": "noun",
        "meaning": ["勞工", "勞動", "勞動力", "辛勤工作(動詞)"],
        "topics": ["人資招聘", "生產設備"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Automation technology investments significantly reduced manufacturing factory operational labor costs.",
            "zh": "自動化技術的投資顯著降低了工廠生產製造中的營運勞動人力成本。"
        },
        "mnemonic": "人資與生產核心字彙：labor cost (勞工成本)、skilled labor (熟練勞工)。",
        "collocations": ["labor cost", "skilled labor"]
    },
    "surface": {
        "phonetic": "/ˈsɜːrfɪs/",
        "pos": "noun",
        "meaning": ["表面", "浮出水面/顯露(動詞)"],
        "topics": ["生產設備", "運輸物流"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Inspectors verified that the titanium component surface was completely free of scratches.",
            "zh": "檢驗人員核實了該鈦金屬零件表面完全沒有任何刮痕瑕疵。"
        },
        "mnemonic": "sur- (在...之上) + face (面) ＝ 最上面那一層 ＝ 表面 (surface mail 地面陸運)。",
        "collocations": ["surface mail", "smooth surface"],
        "roots": ["sur- 在上 (super-)", "fac- 臉、表面"]
    },
    "library": {
        "phonetic": "/ˈlaɪbreri/",
        "pos": "noun",
        "meaning": ["圖書館", "資料庫", "檔案庫"],
        "topics": ["辦公室", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Employees can access the corporate digital training video library through the internal intranet.",
            "zh": "全體員工可透過企業內部網路隨時查閱公司的數位培訓影音資源庫。"
        },
        "mnemonic": "libr- (書本) + -ary (場所) ＝ 圖書室，商務上常指數位資料檔案庫 (digital library)。",
        "collocations": ["digital library", "reference library"],
        "roots": ["libr- 書本", "-ary 場所"]
    },
    "excellent": {
        "phonetic": "/ˈeksələnt/",
        "pos": "adjective",
        "meaning": ["優秀的", "傑出的", "出色的"],
        "topics": ["客戶服務", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The newly recruited marketing specialist demonstrated an excellent command of corporate public relations.",
            "zh": "新招募的行銷專員展現了對企業公共關係處理的極其出色的掌控能力。"
        },
        "mnemonic": "ex- (出) + cel (超越) + -ent ＝ 出類拔萃的 ＝ 優秀的 (excellent service)。",
        "collocations": ["excellent service", "excellent condition"],
        "roots": ["ex- 出", "cel- 超越、高聳", "-ent 形容詞"]
    },
    "edge": {
        "phonetic": "/edʒ/",
        "pos": "noun",
        "meaning": ["優勢", "邊緣", "略勝一籌(動詞)"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Proprietary automated manufacturing processes give our firm a distinct competitive edge.",
            "zh": "專利的自動化製造工藝為我們公司帶來了顯著的市場競爭優勢。"
        },
        "mnemonic": "多益商業核心搭配：competitive edge (競爭優勢)、have an edge over (勝過)。",
        "collocations": ["competitive edge", "sharp edge"]
    },
    "camp": {
        "phonetic": "/kæmp/",
        "pos": "noun",
        "meaning": ["訓練營", "營地", "露營(動詞)"],
        "topics": ["人資招聘", "公司政策"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "New technical recruits attend an intensive two-week software engineering training boot camp.",
            "zh": "新進技術人員需參加為期兩週的密集軟體工程培訓訓練營。"
        },
        "mnemonic": "員工職前培訓常見搭配：training camp / boot camp (培訓訓練營)。",
        "collocations": ["boot camp", "summer camp"]
    },
    "audience": {
        "phonetic": "/ˈɔːdiəns/",
        "pos": "noun",
        "meaning": ["觀眾", "聽眾", "目標客群(target audience)"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The commercial marketing presentation was tailored specifically to appeal to our target corporate audience.",
            "zh": "這場商務行銷簡報經過專門量身規劃，以精準吸引我們的企業目標受眾族群。"
        },
        "mnemonic": "audi- (聽) + -ence (名詞) ＝ 聆聽的受眾群 ＝ 聽眾、目標受眾 (target audience)。",
        "collocations": ["target audience", "large audience"],
        "roots": ["audi- 聽", "-ence 名詞"]
    },
    "lift": {
        "phonetic": "/lɪft/",
        "pos": "verb",
        "meaning": ["提升", "解除(禁令)", "電梯(英式名詞)"],
        "topics": ["公司政策", "付款財務"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "The regulatory commerce committee officially voted to lift export trade restrictions on semiconductors.",
            "zh": "商務監管委員會正式投票通過解除對半導體產品的出口貿易限制。"
        },
        "mnemonic": "多益雙考點：lift restrictions (解除限制禁令) 或英式電梯 (take the lift)。",
        "collocations": ["lift restrictions", "take the lift"]
    },
    "email": {
        "phonetic": "/ˈiːmeɪl/",
        "pos": "noun",
        "meaning": ["電子郵件", "寄電子郵件(動詞)"],
        "topics": ["辦公室", "客戶服務"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "Please send a confirmation email with the signed non-disclosure agreement attached.",
            "zh": "請發送一封隨附已簽署保密合約的確認電子郵件。"
        },
        "mnemonic": "e (electronic) + mail ＝ 電子郵件 (confirmation email)。",
        "collocations": ["send an email", "email attachment"]
    },
    "global": {
        "phonetic": "/ˈɡloʊbl/",
        "pos": "adjective",
        "meaning": ["全球的", "跨國的"],
        "topics": ["行銷銷售", "商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Our international enterprise logistics network serves global corporate clients across five continents.",
            "zh": "我們的跨國企業物流網路為橫跨五大洲的全球企業客戶提供優質服務。"
        },
        "mnemonic": "globe (地球) + -al (形容詞尾) ＝ 全球性的 (global economy / market)。",
        "collocations": ["global market", "global economy"],
        "roots": ["glob- 球體、地球", "-al 形容詞"]
    },
    "struggle": {
        "phonetic": "/ˈstrʌɡl/",
        "pos": "verb",
        "meaning": ["奮鬥", "苦苦掙扎", "艱困奮戰(名詞)"],
        "topics": ["付款財務", "行銷銷售"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Small retail shops often struggle to compete against large multinational discount e-commerce chains.",
            "zh": "小型零售門市在與大型跨國平價電子商務連鎖集團競爭時往往苦苦苦苦支撐。"
        },
        "mnemonic": "商業困境常用：struggle to compete (艱困競爭)、struggle to survive (掙扎求存)。",
        "collocations": ["struggle to", "struggle with"]
    },
    "advertise": {
        "phonetic": "/ˈædvərtaɪz/",
        "pos": "verb",
        "meaning": ["刊登廣告", "宣傳", "宣傳公告"],
        "topics": ["行銷銷售", "人資招聘"],
        "tags": ["TOEIC", "高頻單字", "A2"],
        "example": {
            "en": "The corporate human resources department will advertise the vacant engineering position online.",
            "zh": "企業人力資源部將在網路上刊登招聘該出缺工程師職位的公開徵才廣告。"
        },
        "mnemonic": "ad- (向) + vert (轉向) ＝ 把大眾注意力轉移過來 ＝ 登廣告 (advertise a position)。",
        "collocations": ["advertise a job", "advertise products"],
        "roots": ["ad- 向", "vert- 轉向", "-ise / -ize 動詞"]
    },
    "predict": {
        "phonetic": "/prɪˈdɪkt/",
        "pos": "verb",
        "meaning": ["預測", "預言"],
        "topics": ["商務會議"],
        "tags": ["TOEIC", "高頻單字", "B1"],
        "example": {
            "en": "Analysts predict that sales will rise next quarter.",
            "zh": "分析師預測下一季銷售額將上升。"
        },
        "mnemonic": "pre-（預先）+ dict（說）＝事先說出來。",
        "collocations": ["predict sales", "accurately predict"],
        "roots": ["pre- 預先", "dict 說 → 預言"]
    }
}
