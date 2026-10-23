---
tags: [Linux, 作業系統, 伺服器架設]
---
# Linux 與發行版

## 重點

- Linux 是核心；完整發行版還包含套件管理器、系統工具、函式庫與服務。
- 伺服器常見 Enterprise Linux 系列：RHEL、Rocky Linux、AlmaLinux。
- 選擇發行版要看支援週期、套件來源、硬體相容性與企業標準。
- 本課程以 Rocky Linux 8／9 類型的 Enterprise Linux 為示範。

## 安裝前檢查

1. 確認 CPU、記憶體、磁碟與網路需求。
2. 取得可信任的 ISO 與校驗資訊。
3. 規劃主機名稱、IP、DNS、磁碟分割與管理帳號。
4. 安裝後更新套件並檢查時間、網路與權限。

- [原始章節](https://hackmd.io/@ntub-class/B12EXeiufx/%2F_QeF6gMSRVmiagdO3gbFMw)

## 從零開始理解

### Linux 到底是什麼？

可以把作業系統想成「使用者與硬體之間的翻譯員」。Linux kernel（核心）負責管理 CPU、記憶體、磁碟、網路卡等硬體；我們平常輸入的 `ls`、`cp`、`systemctl` 則是使用者空間的工具。

「Linux 發行版」不是另一種核心，而是把 Linux 核心、指令、函式庫、套件管理器與預設設定包在一起的完整系統。例如 Rocky Linux、AlmaLinux、RHEL 都屬於 Enterprise Linux 生態系。

### 第一次登入後先做什麼？

不要急著安裝服務，先確認「我在哪裡、我是誰、系統是哪一版」：

```bash
whoami
pwd
hostnamectl
cat /etc/os-release
uname -r
```

- `whoami`：確認目前帳號。
- `pwd`：確認目前所在目錄。
- `hostnamectl`：查看主機名稱與系統概況。
- `/etc/os-release`：查看發行版名稱與版本。
- `uname -r`：查看 Linux 核心版本。

### 初學者常見錯誤

- 把 Linux、Ubuntu、Rocky Linux 當成同一個名詞：Linux 是核心，Ubuntu/Rocky 是發行版。
- 不知道目前帳號就執行管理命令：先用 `whoami`，需要管理權限時再加 `sudo`。
- 未確認版本就照抄教學：不同發行版的套件名稱、設定工具與預設服務可能不同。
- 把安裝 ISO 當成已安裝系統：ISO 是安裝媒體，安裝後才會進入硬碟中的作業系統。

> [!tip] 建議練習
> 先只執行上面的五個查詢指令，將輸出中的「發行版、版本、核心、主機名稱、目前使用者」各自寫成一句話。
