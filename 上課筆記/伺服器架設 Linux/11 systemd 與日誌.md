---
tags: [Linux, systemd, systemctl, journalctl, rsyslog, 日誌]
source: https://hackmd.io/@ntub-class/B12EXeiufx
---
# systemd 與日誌

> [!abstract] 這章要學會什麼
> 1. systemd 是什麼、為什麼取代了 SysV init
> 2. 用 `systemctl` 管理服務：`start / stop / restart / reload / status / enable / disable / mask`
> 3. 看懂 syslog 的 **Facility（類別）** 與 **Severity（層級）**
> 4. 用 `journalctl` 查日誌，以及它和 `rsyslog` 的差別
> 5. 用 `logger` 自己寫一筆系統日誌
>
> 總目錄：[[伺服器架設與規劃]]。安裝服務的套件管理見 [[10 RPM 與 dnf 套件管理]]。

原始章節：[systemd 開機機制](https://hackmd.io/@ntub-class/B12EXeiufx/%2Flm09SUiCT5GoxwX1bxJfSg)、[systemctl 與服務管理](https://hackmd.io/@ntub-class/B12EXeiufx/%2FbRIPVHIERvazp-vfsogMoA)、[journal 與日誌檢查](https://hackmd.io/@ntub-class/B12EXeiufx/%2F3vdOFzG8SaCVi5hb3KBMLg)

> [!warning] 「systemd 開機機制」那一頁我讀不到
> 該頁在 HackMD 回傳 403（權限不足，可能是尚未公開），所以下面「開機流程」的部分是我依一般 RHEL／Rocky 的 systemd 知識整理的**補充**，並非原頁內容。老師公開後建議再對照原頁。

---

## 一、為什麼有 systemd？

**Init system（初始化系統）** 是 Linux 開機後核心啟動的**第一個行程（PID 1）**，負責把整個系統「拉起來」：掛載磁碟、啟動網路、啟動各種服務。

| | SysV init（舊） | systemd（新，EL7 起） |
|---|---|---|
| 啟動方式 | 一個個依序啟動（腳本） | **同時（平行）啟動**，開機快很多 |
| 相依性 | 靠腳本編號順序 | 明確宣告「誰要在誰後面」 |
| 管理介面 | `service`、`chkconfig` 各自為政 | **`systemctl` 統一** |
| 日誌 | 各服務自己寫 `/var/log/` | 集中到 **journal** |
| 資源控制 | 無 | 可限制 CPU、記憶體（cgroup） |
| 失敗處理 | 要自己寫監控 | 可自動重啟（`Restart=on-failure`） |

> 因為雲端、容器、現代硬體的發展，SysV init 顯得陳舊，所以 **RHEL 7 開始**主流發行版都改用 systemd。

### 服務（Service）是什麼？

**長時間在背景執行的程式**，又叫 **daemon（守護行程）**：例如 SSH（`sshd`）、網頁伺服器（`httpd`）、資料庫（`mariadb`）、校時（`chronyd`）、排程（`crond`）。通常名稱結尾是 `d`（daemon）。

---

## 二、（補充）systemd 開機流程與 Target

> 此節為依一般知識整理的補充，原頁無法讀取。

```text
電源 → BIOS/UEFI → 開機載入器 GRUB2 → 載入 Linux 核心 + initramfs
     → 核心啟動 PID 1 = systemd → 依 default.target 啟動所需的服務與掛載
     → 登入畫面
```

**Target（目標）** 取代了舊的 runlevel，一個 target = 一群 unit 的集合，代表系統「要到達的狀態」。

| Target | 舊 runlevel | 說明 |
|---|---|---|
| `poweroff.target` | 0 | 關機 |
| `rescue.target` | 1 | 單人救援模式 |
| `multi-user.target` | 3 | 多人、**純文字**（伺服器預設） |
| `graphical.target` | 5 | 多人、圖形介面 |
| `reboot.target` | 6 | 重新開機 |

```bash
systemctl get-default                       # 目前預設
sudo systemctl set-default multi-user.target
sudo systemctl isolate rescue.target         # 立即切換（小心！會中斷其他使用者）
systemd-analyze                              # 開機總花費時間
systemd-analyze blame                        # 哪個服務最慢
systemd-analyze critical-chain               # 關鍵相依路徑
```

**Unit 的類型**

| 類型 | 副檔名 | 說明 |
|---|---|---|
| service | `.service` | 服務（最常用） |
| socket | `.socket` | 有人連 Port 才啟動服務 |
| timer | `.timer` | 排程（可取代 cron） |
| mount | `.mount` | 掛載點（由 `/etc/fstab` 產生） |
| target | `.target` | 一組 unit |

Unit 檔案位置：

- `/usr/lib/systemd/system/`：套件預設（不要改）
- `/etc/systemd/system/`：管理員自訂與覆寫（**優先**）

---

## 三、`systemctl` 管理服務

### 與 SysV init 對照

| 功能 | systemd（`systemctl`） | 舊式 SysV |
|---|---|---|
| 啟動 | `systemctl start 服務` | `service 服務 start` |
| 停止 | `systemctl stop 服務` | `service 服務 stop` |
| 重新啟動 | `systemctl restart 服務` | `service 服務 restart` |
| 重新載入設定 | `systemctl reload 服務` | `service 服務 reload` |
| 查看狀態 | `systemctl status 服務` | `service 服務 status` |
| 開機啟動 | `systemctl enable 服務` | `chkconfig 服務 on` |
| 取消開機啟動 | `systemctl disable 服務` | `chkconfig 服務 off` |
| 列出所有服務 | `systemctl list-units --type=service` | `chkconfig --list` |
| 看日誌 | `journalctl -u 服務` | 翻 `/var/log/` |
| 完全封鎖服務 | `systemctl mask 服務` | （無） |

> 服務名稱後面的 `.service` 可以省略：`httpd` = `httpd.service`。

### 演練：httpd

```bash
sudo dnf install -y httpd
sudo systemctl start httpd          # 1. 啟動
sudo systemctl stop httpd           # 2. 停止
sudo systemctl restart httpd        # 3. 重新啟動（先停再啟，連線會中斷）
sudo systemctl reload httpd         # 4. 重新載入設定（不中斷服務，前提是服務支援）
sudo systemctl status httpd         # 5. 看狀態
sudo systemctl enable httpd         # 6. 設定開機自動啟動
sudo systemctl disable httpd        # 7. 取消開機自動啟動
```

### `start` 與 `enable` 完全是兩件事！

| | `start` | `enable` |
|---|---|---|
| 作用 | **現在**立刻啟動 | **下次開機**才會自動啟動 |
| 重開機後 | 不一定還在 | 會自動啟動 |

```bash
sudo systemctl enable --now httpd     # 兩件事一起做（最常用）
sudo systemctl disable --now httpd    # 取消開機啟動 + 現在就停止
systemctl is-active httpd             # active / inactive / failed（腳本用）
systemctl is-enabled httpd            # enabled / disabled
```

### 看懂 `systemctl status`

```text
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since Tue 2023-10-10 09:10:01 UTC; 2h 55min ago
 Main PID: 1234 (httpd)
   Status: "Total requests: 100; ..."
    Tasks: 60 (limit: 512)
   CGroup: /system.slice/httpd.service
           ├─1234 /usr/sbin/httpd -DFOREGROUND
           ├─1235 /usr/sbin/httpd -DFOREGROUND
           └─1236 /usr/sbin/httpd -DFOREGROUND
```

| 欄位 | 解讀 |
|---|---|
| 前面的 `●` | **綠色**=正常運行；**紅色**=failed；白/灰色=停止 |
| `Loaded` | unit 檔位置；`enabled`／`disabled` = 開機是否自動啟動；`vendor preset` 是套件預設值 |
| `Active` | **最重要**：`active (running)` 執行中、`inactive (dead)` 停止、`failed` 失敗、`activating` 啟動中 |
| `Main PID` | 主行程 PID |
| `CGroup` | 這個服務擁有的所有行程（樹狀） |
| 最下方 | **最近幾行 log**，出錯時第一個要看的地方 |

### `restart` vs `reload` 怎麼選？

- **改了設定檔**，服務支援 reload → 用 `reload`（不中斷連線）。
- 不確定或升級了程式 → `restart`。
- 不管哪個，**改完設定先檢查語法**再套用，例如 `apachectl configtest`、`nginx -t`，避免服務因設定錯誤起不來。

### `mask`：徹底封鎖服務

`disable` 只是不開機啟動，但別人（或其他服務）仍可以手動 `start` 或透過相依把它帶起來。`mask` 會把 unit 連結到 `/dev/null`，**任何方式都無法啟動**，直到 `unmask`。

```bash
sudo systemctl mask postfix
sudo systemctl unmask postfix
```

### 列出與篩選

```bash
systemctl list-units --type=service                  # 載入中的服務
systemctl list-units --type=service --state=failed   # 失敗的服務（排查必看）
systemctl list-unit-files --type=service             # 所有 unit 檔與 enabled 狀態
systemctl list-timers                                # 排程器
sudo systemctl daemon-reload                         # 修改 unit 檔後重新載入
```

### 服務故障排查流程

```bash
systemctl status nginx --no-pager             # 1. systemd 認為它是 active、failed 還是 inactive？
journalctl -u nginx -b -n 100 --no-pager      # 2. 本次開機這個服務有什麼錯誤？
ss -lntp | grep ':80'                         # 3. 真的有在聽預期的 Port 嗎？
# 4. 設定檔是否正確？權限／SELinux 是否允許？
# 5. 防火牆有沒有擋？(firewall-cmd --list-all)
```

> [!warning] `restart` 不是萬靈丹
> 重啟只是重新執行一次，**不能修正錯誤的設定**。若重啟後仍失敗，回到 `status`、`journalctl` 與設定檔去找原因。

> [!tip] 裝完 ≠ 跑起來
> `dnf install` 裝了套件，不一定啟動服務，也不一定開放防火牆。完整流程：安裝 → 設定 → 檢查語法 → `enable --now` → `status` → `ss` → 防火牆。

---

## 四、syslog：類別（Facility）與層級（Severity）

應用程式送訊息到系統日誌時，會用兩個標籤分類：

- **Facility（類別）**：這是誰產生的？（kernel、郵件、驗證……）
- **Severity（層級）**：有多嚴重？

### Facility 一覽

| Facility | 說明 |
|---|---|
| `kern` | 核心事件（驅動載入、硬體錯誤） |
| `user` | 使用者層級（登入、登出） |
| `mail` | 郵件系統 |
| `daemon` | 一般服務（啟動、停止、錯誤） |
| `auth` | 驗證與授權（登入失敗） |
| `authpriv` | 安全驗證的**私有**事件，常含敏感資訊（`/var/log/secure`） |
| `syslog` | syslog 守護程式自己的事件 |
| `lpr` | 列印 |
| `news` | 新聞伺服器 |
| `uucp` | UUCP 檔案傳輸（古老） |
| `cron` | 排程（cron） |
| `ftp` | FTP |
| `ntp` | 時間同步 |
| `local0`～`local7` | **自訂**用，不屬於上述類別的服務通常放這裡 |

有些（`ftp`、`news`、`uucp`）已不太流行，常用的就上面那些。

### Severity 層級（數字越小越嚴重）

| 數字 | 名稱 | 關鍵字 | 意義 |
|---|---|---|---|
| 0 | Emergency | `emerg` | 系統無法繼續運行，立即處理 |
| 1 | Alert | `alert` | 需要立刻注意與回應 |
| 2 | Critical | `crit` | 重大問題 |
| 3 | Error | `err` | 發生錯誤，但仍可運行 |
| 4 | Warning | `warning` | 潛在問題 |
| 5 | Notice | `notice` | 正常但值得注意 |
| 6 | Informational | `info` | 一般營運訊息 |
| 7 | Debug | `debug` | 除錯用 |

> [!tip] 記憶口訣（由嚴重到輕微）
> **E**very **A**wesome **C**isco **E**ngineer **W**ill **N**eed **I**ce-cream **D**aily → Emerg, Alert, Crit, Err, Warning, Notice, Info, Debug。
> 管理員要特別重視 **Warning、Error、Alert、Emergency**，評估是應用程式或系統問題並排除。

---

## 五、journald 與 rsyslog

| 特性 | `journalctl`（systemd journal） | `rsyslog`（傳統 syslog 伺服器） |
|---|---|---|
| 儲存格式 | **二進位**，位置 `/var/log/journal/`（或 `/run/log/journal/`） | **純文字**，位置 `/var/log/` |
| 看全部 | `journalctl` | `cat /var/log/messages`（Debian 系是 `/var/log/syslog`） |
| 時間篩選 | `--since`、`--until`（內建） | 需靠 `grep`、`awk` |
| 輪替 | 自動管理（依大小、時間） | 由 `logrotate` 設定 |
| 二進位日誌 | 原生支援 | 不支援 |
| 傳到遠端日誌主機 | 要額外設定或轉給 rsyslog | **原生支援** |
| 即時追蹤 | `journalctl -f` | `tail -f /var/log/messages` |
| 本次開機 | `journalctl -b` | `/var/log/boot.log` |

**怎麼選？**

- 單機或幾台主機：`journalctl` 夠用。
- 主機很多：需要 `rsyslog` 搭配**集中式日誌主機**統一管理（也方便稽核，避免被入侵者從本機刪掉證據）。
- 兩者可以同時存在：rsyslog 也會截取 syslog 訊息，寫到 `/var/log/messages` 等檔案。

常見的 `/var/log/` 檔案：

| 檔案 | 內容 |
|---|---|
| `messages` | 一般系統訊息（沒特別設定的大部分在這） |
| `secure` | 登入、sudo、SSH 驗證（資安必看） |
| `cron` | 排程執行紀錄 |
| `maillog` | 郵件 |
| `dmesg`／`boot.log` | 核心開機訊息／開機服務 |
| `httpd/` | Apache 的 access_log、error_log |

---

## 六、`journalctl` 查日誌

### 基本用法

```bash
journalctl                             # 全部記錄（用 less 分頁；空白鍵翻頁，q 離開，G 到最後）
journalctl -b                          # 本次開機以來
journalctl -b -1                       # 上一次開機
journalctl -u sshd                     # 只看 sshd 服務
journalctl -u nginx -b -n 100          # nginx、本次開機、最近 100 行
journalctl -f                          # 即時追蹤（像 tail -f）
journalctl -u httpd -f                 # 即時追蹤某服務
journalctl -p err                      # 錯誤（err）以上的等級
journalctl -p warning..alert -b        # warning 到 alert 的範圍
journalctl --since "2023-06-11"        # 這天之後
journalctl --since "1 hour ago"        # 最近一小時
journalctl --since "10 minutes ago" --until "5 minutes ago"
journalctl -k                          # 只看核心訊息 (等同 dmesg)
journalctl -t class                    # 依「標籤 (tag)」篩選
journalctl -o json-pretty              # JSON 輸出
journalctl --no-pager                  # 不分頁（搭配 grep 好用）
journalctl --disk-usage                # 日誌佔用多少空間
```

### 重要參數

| 參數 | 說明 |
|---|---|
| `-u 服務` | 指定服務（unit） |
| `-b` | 本次開機（`-b -1` 上次） |
| `-n 50` | 最近 50 行 |
| `-f` | 持續追蹤 |
| `-p 等級` | 依 syslog 層級篩選 |
| `--since` / `--until` | 時間範圍 |
| `-t 標籤` | 依 syslog identifier |
| `-k` | 核心訊息 |
| `-r` | 反向，最新的在最前面 |

### 讓 journal 永久保存

> [!warning] 預設重開機後日誌會消失
> 在 Enterprise Linux 上，journal 預設放在**記憶體**（`/run/log/journal`），重開機就沒了。只要建立目錄，就會改存硬碟：

```bash
sudo mkdir /var/log/journal/
sudo systemctl restart systemd-journald      # 讓設定生效（原文省略，建議做）
journalctl --disk-usage
```

（也可編輯 `/etc/systemd/journald.conf` 設 `Storage=persistent`、`SystemMaxUse=500M` 限制大小。）
排查「上次當機前發生什麼事」就要靠永久保存，這是很重要的設定。

---

## 七、自己寫入日誌：`logger`

把自訂訊息寫進系統日誌（腳本裡很有用，例如備份完成通知）：

```bash
logger -t class -p user.info "Hello"
```

拆解：

| 部分 | 說明 |
|---|---|
| `logger` | 寫入 syslog 的指令 |
| `-t class` | 給這筆記錄貼上**標籤**（tag），之後好找 |
| `-p user.info` | `類別.層級`：類別 `user`、層級 `info` |
| `"Hello"` | 訊息本文 |

用 `journalctl` 找出：

```bash
journalctl -t class
# Oct 10 12:00:01 server class[1234]: Hello
sudo grep class /var/log/messages     # rsyslog 也會記
```

應用：在 Shell script 裡

```bash
logger -t backup -p local0.notice "備份完成，共 $(ls /backup | wc -l) 個檔案"
logger -t backup -p local0.err    "備份失敗！"
```

層級用 `err` 就能用 `journalctl -p err` 一次撈出所有錯誤。

---

## 八、本章小抄

```bash
systemctl status|start|stop|restart|reload 服務
systemctl enable --now 服務                  # 開機啟動 + 立刻啟動
systemctl list-units --type=service --state=failed
journalctl -u 服務 -b -n 100 --no-pager      # 看服務本次開機的 log
journalctl -f ; journalctl -p err -b ; journalctl --since "1 hour ago"
sudo mkdir /var/log/journal                  # 日誌永久保存
logger -t 標籤 -p user.info "訊息"
```
