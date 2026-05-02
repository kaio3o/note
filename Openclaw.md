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


./start_vllm.sh