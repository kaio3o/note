[别再用 Ollama 了！OpenClaw 秒级响应方案（vLLM + 本地模型）完全免费！| 零度解说](https://www.youtube.com/watch?v=rHmdJjOytRk)

[OpenClaw 完整攻略：從必設參數到超好用 Skills，一篇搞懂這個 199k Stars 的 AI Agent - HackMD](https://hackmd.io/@BASHCAT/rylaWmGuWe)

[CanIRun.ai — Can your machine run AI models?](https://www.canirun.ai/)

[如何訓練你的 OpenClaw：社群秘訣與最佳實踐 - topics - Tenten AI](https://university.tenten.co/t/openclaw/2162)

[六个AI相互入侵服务器！谁能杀死对方？](https://www.youtube.com/watch?v=an7Dbkh7no4)

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

### 電腦太爛直接用codeX
選擇codeX 並於瀏覽器登入

### 又改看看LM Studio
下載完成，去Developer 開啟local Server
設定**在本地網路中提供服務**、**啟用 CORS** 開啟並取得IP 即可 還是電腦太爛>:

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

