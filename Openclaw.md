[别再用 Ollama 了！OpenClaw 秒级响应方案（vLLM + 本地模型）完全免费！| 零度解说](https://www.youtube.com/watch?v=rHmdJjOytRk)

[OpenClaw 完整攻略：從必設參數到超好用 Skills，一篇搞懂這個 199k Stars 的 AI Agent - HackMD](https://hackmd.io/@BASHCAT/rylaWmGuWe)


1. 安裝 ollama
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

這我不會用好難
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

./start_vllm.sh

### 電腦太爛直接用codeX
