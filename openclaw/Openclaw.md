[别再用 Ollama 了！OpenClaw 秒级响应方案（vLLM + 本地模型）完全免费！| 零度解说](https://www.youtube.com/watch?v=rHmdJjOytRk)

[OpenClaw 完整攻略：從必設參數到超好用 Skills，一篇搞懂這個 199k Stars 的 AI Agent - HackMD](https://hackmd.io/@BASHCAT/rylaWmGuWe)
[OpenClaw — Personal AI Assistant](https://openclaw.ai/)

[CanIRun.ai — Can your machine run AI models?](https://www.canirun.ai/)

[如何訓練你的 OpenClaw：社群秘訣與最佳實踐 - topics - Tenten AI](https://university.tenten.co/t/openclaw/2162)

[六个AI相互入侵服务器！谁能杀死对方？](https://www.youtube.com/watch?v=an7Dbkh7no4)

[應用案例 | OpenClaw 台灣 | 台灣 Openclaw 中文網站](https://openclaw.com.tw/use-cases)

[【拒绝伪需求】普通人必看！OpenClaw 提升生产力的10个实战场景 | 10 Real Ways to Boost Productivity with OpenClaw - YouTube](https://www.youtube.com/watch?v=1ORAOfHV4ag&list=WL&index=63)

---
安裝 ollama
```shell
irm https://ollama.com/install.ps1 | iex
```

```shell
# 先安裝git、nodejs
# PowerShell 管理員身分
npm install -g openclaw@latest
```

```shell
# 設定openclaw
openclaw onboard
```
---
```shell
# 開啟openclaw getway
openclaw gateway
openclaw gateway run
openclaw gateway start
openclaw gateway stop
```

```shell
# 錯誤診斷
openclaw doctor
# 修復
openclaw doctor --fix
```

ollama 推薦開啟方式
```shell
ollama launch openclaw
```
---
安裝技能skills
```shell
openclaw skills install file-manager
```

換用WSL + vLLM
```shell
#./start_vllm.sh
#!/bin/bash
# 啟動 vLLM 伺服器 (針對 8GB 顯卡優化版)

python3 -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-3B-Instruct-AWQ \
  --quantization awq \
  --gpu-memory-utilization 0.85 \
  --max-model-len 2048 \
  --enforce-eager \
  --served-model-name qwen
```

```shell
# 進入虛擬環境
source vllm-env/bin/activate
# 執行vllm
./start_vllm.sh
```

### 又改看看LM Studio
下載完成，去Developer 開啟local Server
設定**在本地網路中提供服務**、**啟用 CORS** 開啟並取得IP 即可 還是電腦太爛>:
### 電腦太爛直接用codeX
選擇codeX 並於瀏覽器登入

### 最後選擇
使用WSL + Codex API

```
~/.openclaw/workspace/
├── AGENTS.md # 操作手冊（主要指令文件）
├── SOUL.md # 核心人格與價值觀
├── IDENTITY.md # 外部身份（名字、角色、語氣） 
├── USER.md # 關於你的資訊 
├── MEMORY.md # 長期精煉記憶 
├── TOOLS.md # 本地工具筆記與偏好 
├── HEARTBEAT.md # 定期主動檢查任務 
├── BOOT.md # 每次啟動時的儀式 
├── BOOTSTRAP.md # 首次設定（用完自動刪除） 
├── memory/ # 每日日誌
│ │ 
│ ├── 2026-02-03.md 
│ │ 
│ └── 2026-02-04.md 
└── skills/ # 自訂技能
```
-  **AGENTS.md** — 你的「營運合約」。放穩定的規則、優先順序、邊界和品質標準。不要放臨時任務。
-  **SOUL.md** — 代理的「靈魂」。每次推理循環的開始都會先讀這個檔案，它就像代理的「憲法」。放人格、語氣、價值觀和不可妥協的約束。社群範例：
```
# SOUL.md - 我的核心  ## 首要指令 讓我的人類生活更輕鬆，幫助他們成功。  ## 核心價值 1. 能力優於表演 — 不要假裝有幫助，要真的有幫助 2. 主動性 — 預見需求，不要等被問 3. 誠實溝通 — 不確定就說不確定  ## 反模式（我避免的事） - 🚫 諂媚（「好問題！」「我很樂意幫忙！」） - 🚫 灌水回應 - 🚫 沒嘗試就說「我做不到」 - 🚫 在所有事上都說「看情況」— 要有明確立場
```
-  **USER.md** — 個人化層。放你的溝通偏好、輸出格式、經常性偏好、已知限制。
-  **IDENTITY.md** — 外部面向的身份。名字、emoji、角色定位、說話方式。如果 SOUL.md 是心臟，這就是臉。
-  **MEMORY.md** — 長期精煉的智慧。不是原始對話紀錄，而是提煉過的重要洞察。
-  **TOOLS.md** — 本地工具偏好，例如「思考/規劃用 Claude Opus，寫程式用 Gemini Pro」。
-  **HEARTBEAT.md** — 定義代理應該主動檢查什麼（預設每 30 分鐘一次）。

與Codex、Ollama、LM Studio 差異
### AI 工具核心差異對照表

| 工具名稱                   | 核心特色                                                           | 主要用處                                         | 運行/託管架構                                             |
| :--------------------- | :------------------------------------------------------------- | :------------------------------------------- | :-------------------------------------------------- |
| **Ollama**             | 輕量、命令列優先、極簡本地部署。提供標準 API，是開發者構建本地 Agent 的底層基石。                 | 本地大模型快速下載與管理、為其他 Agent 提供本地 API 核心。          | 本地端 (Local)                                         |
| **LM Studio**          | 圖形介面精美、視覺化模型配置、支援 MCP（模型上下文協定）伺服器與 RAG 測試。                     | 適合模型效能測試、提示詞除錯、無程式碼需求的本地 AI 互動。              | 本地端 (Local)                                         |
| **OpenClaw**           | **完全自主的 24/7 數位管家**。以通訊軟體為 UI，具備背景心跳機制與自主編寫/擴充技能（Skills）的能力。   | 個人數位助理、跨應用的日常自動化（自動回信、排行程、網頁自動化填表、伺服器自動化運維）。 | **自託管 (Self-hosted)**<br>（跑在本地或 VPS，模型可接雲端或 Ollama） |
| **OpenAI Codex**       | **終端優先/雲端沙盒的多 Agent 指令中心**。支援平行工作流（Worktrees）與代碼庫非同步交付。        | 軟體工程端到端交付、程式碼大規模重構、自動化維護 GitHub 專案與 CI/CD。   | 雲端驅動 / 專用桌面端                                        |
| **Google Antigravity** | **Agent-first 中央控制台**。內建瀏覽器自動化，可同時平行調度最多 16 個專業 Agent（前端、測試等）。 | 全疊開發、複雜系統架構規劃、自動化網頁 UI 整合測試與多 Agent 協同作戰。    | 雲端與本地混合 / 獨立 App                                    |




1. OpenClaw 是什麼
2. 可以做什麼
	動態RAG 個人知識資料庫、自動化工作流程
	整理筆記、上網搜尋並整理製成workflow
	叫他自己修自己 
3. Skill/Tool - 與MCP 差異
4. 怎麼用
5. Demo
6. 與其他 AI 工具比較 ← 新增 (AI agent Antigravity、Codex、Gemini ChatGPT...)
7. 優缺點
	幻覺、卡住、工具故障、成本、延遲時間、安全性
8. 未來期望