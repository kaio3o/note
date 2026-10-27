---
tags: [Linux, RPM, dnf, yum, 套件管理, repository]
source: https://hackmd.io/@ntub-class/B12EXeiufx
---
# RPM 與 dnf 套件管理

> [!abstract] 這章要學會什麼
> 1. 知道 Linux 裡「裝軟體」叫**裝套件**，以及 `rpm` → `yum` → `dnf` 的演進
> 2. 會用 `rpm` **查詢**（`-qa`、`-qf`、`-ql`、`-qi`）
> 3. 看懂 **repository（套件來源）** 設定檔 `/etc/yum.repos.d/*.repo`
> 4. 會用 `dnf` 搜尋、安裝、移除、更新、查歷史、反查套件
>
> 總目錄：[[伺服器架設與規劃]]；裝完服務後的啟動與管理見 [[11 systemd 與日誌]]。

原始章節：[套件管理需求](https://hackmd.io/@ntub-class/B12EXeiufx/%2FcLJDMB9JQuC-x1-nx9mdug)、[RPM 管理](https://hackmd.io/@ntub-class/B12EXeiufx/%2F0DWDepIZSDuk2p3PC5gA9Q)、[使用 dnf 管理套件](https://hackmd.io/@ntub-class/B12EXeiufx/%2FE4bWmADQTxqRbUb2orKniw)

---

## 一、為什麼需要「套件管理」？

在 Linux 我們比較少說「軟體」，而說「**套件（package）**」。套件不是單一執行檔，通常還包含：

- 執行檔
- 設定檔
- 函式庫
- 服務檔（systemd unit）
- 說明文件
- **版本資訊與相依性**（需要哪些其他套件）

套件管理器會**記錄**這些東西，所以能做到：

| 能力 | 手動複製檔案做不到的事 |
|---|---|
| 知道每個檔案屬於哪個套件 | 清理時不會漏、也不會誤刪 |
| 安全升級／移除 | 不會留下一堆殘檔 |
| 自動處理相依性 | 不用自己找缺什麼 |
| 驗證完整性 | 用 GPG 簽名確認套件沒被竄改 |

相比「下載原始碼自己編譯」（`./configure && make && make install`），用套件管理系統**方便又有效率**，也不會讓系統處於「不知道誰裝了什麼」的狀態。

## 二、演進史：rpm → yum → dnf

| 階段 | 工具 | 特色／問題 |
|---|---|---|
| 1 | **RPM**（格式）／`rpm`（指令） | Enterprise Linux 的**最小套件格式**。能裝、升級、移除、查詢，但**不會自動解決相依性** |
| 2 | **yum**（Yellowdog Updater, Modified） | 自動解決相依性；可從 **repository** 下載安裝 |
| 3 | **dnf**（Dandified YUM） | yum 的下一代：更快、更有效率、**支援模組化（多版本）**、可自動移除用不到的相依套件；**RHEL 8 起正式採用**；命令列與 yum 大致相容（`yum` 在 EL8/9 其實是連到 `dnf` 的別名） |

### 什麼是「相依性地獄」？

```bash
sudo rpm -ivh foo.rpm
# error: Failed dependencies:  bar is needed by foo
```

foo 需要 bar → 你先去找 bar.rpm → bar 又需要 baz → …… 這種連鎖的相依，用 `rpm` 手動處理會非常痛苦。`yum`／`dnf` 會**自動把整串相依套件一次找齊裝好**，這就是它們存在的原因。

> [!tip] 用一句話分清楚
> **`rpm` = 處理單一 `.rpm` 檔案的底層工具（擅長查詢）；`dnf` = 連到 repository 的高階工具（日常安裝更新用）。**

---

## 三、`rpm`：底層工具（主要用來查詢）

雖然有 dnf，管理員仍要懂 rpm，用在**除錯、離線管理、查詢**。

### 常用參數

| 參數 | 意思 |
|---|---|
| `-q` | query 查詢 |
| `-a` | all 全部已安裝套件 |
| `-i` | info 套件詳細資訊（安裝時是 install） |
| `-l` | list 套件包含的檔案清單 |
| `-f 檔案` | file 反查這個檔案屬於哪個套件 |
| `-p` | 對象是 `.rpm` 檔案（尚未安裝的） |
| `-c` | 只列出設定檔 |
| `-v` `-h` | 詳細輸出、顯示進度條（`-ivh` 組合） |
| `--changelog` | 套件修改紀錄 |
| `-V` | verify，驗證套件檔案有沒有被改過 |

### 範例

**安裝**（需要自己處理相依性，不推薦日常使用）

```bash
sudo rpm -ivh foo.rpm
```

**列出已安裝套件**

```bash
rpm -qa | head
# libgcc-11.2.1-9.4.el9.x86_64
# tzdata-2022a-1.el9_0.noarch
# ...
```

套件名稱格式：`名稱-版本-發行號.發行版.架構`，例如 `libgcc-11.2.1-9.4.el9.x86_64`：

- `libgcc`：名稱
- `11.2.1`：上游軟體版本
- `9.4`：打包發行號
- `el9`：Enterprise Linux 9
- `x86_64`：CPU 架構（`noarch` = 不分架構）

**查某個套件有沒有裝：** `rpm -q nginx`

**反查：這個檔案屬於哪個套件？**

```bash
rpm -qf /usr/lib64/libxml2.so.2
# libxml2-2.9.13-1.el9.x86_64
```

**安裝前先看 .rpm 會裝哪些檔案**（`-p` 對象是檔案）

```bash
rpm -qlp apr-1.7.0-11.el9.x86_64.rpm
# /usr/lib64/libapr-1.so.0
# /usr/share/doc/apr/README ...
```

> [!note] 原文寫法的小補充
> 原教材寫 `rpm -ql apr-...rpm`，但 `-ql` 後面接的是「已安裝套件名稱」，若對象是尚未安裝的 `.rpm` 檔案，要加 `-p`（`-qlp`）。已安裝的則 `rpm -ql apr`。

**看套件的修改紀錄（含 CVE 安全修補）**

```bash
rpm -q --changelog kernel | head
```

**其他實用：**

```bash
rpm -qi httpd              # 套件詳細資訊
rpm -qc httpd              # 這個套件的設定檔有哪些（超實用）
rpm -qd httpd              # 說明文件
rpm -V httpd               # 驗證檔案有沒有被改過（資安稽核常用）
rpm --import <gpgkey>      # 匯入 GPG 公鑰
```

---

## 四、Repository（套件來源）設定

### dnf 去哪裡抓套件？

dnf 預設從**網路上的 repository** 下載，所以主機必須能連網（或指向內部的鏡像站）。它先讀取設定檔，再到設定檔指定的位置找套件。設定檔放在：

```text
/etc/yum.repos.d/*.repo
```

Rocky Linux 預設會有：

```text
Rocky-BaseOS.repo         ← 基本系統
Rocky-AppStream.repo      ← 應用程式與模組
Rocky-Extras.repo         ← 額外套件
Rocky-Devel.repo  Rocky-PowerTools.repo(CRB)  Rocky-HighAvailability.repo
Rocky-Plus.repo  Rocky-NFV.repo  Rocky-RT.repo  Rocky-Media.repo  Rocky-Sources.repo  ...
```

（Rocky 9 的檔名略有不同，如 `rocky.repo`、`rocky-addons.repo`、`rocky-extras.repo`。）

### 一個 repo 的結構

```ini
[baseos]
name=Rocky Linux $releasever - BaseOS
mirrorlist=https://mirrors.rockylinux.org/mirrorlist?arch=$basearch&repo=BaseOS-$releasever
#baseurl=http://dl.rockylinux.org/$contentdir/$releasever/BaseOS/$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rockyofficial
```

| 參數 | 意義 |
|---|---|
| `[baseos]` | repo 的**唯一識別名稱**（dnf 指令裡用這個名字，例如 `--enablerepo=baseos`） |
| `name` | 給人看的說明 |
| `mirrorlist` | 鏡像站**清單**，dnf 會從中自動挑最合適的 |
| `baseurl` | **明確指定**的來源網址。前面加 `#` = 註解 = 不使用 |
| `gpgcheck` | 是否檢查套件的 GPG 簽名（確認封裝者正確、沒被竄改） |
| `enabled` | `1` 啟用、`0` 停用 |
| `gpgkey` | 驗證用的公鑰位置，與 `gpgcheck` 搭配 |

**重點**：`mirrorlist` 與 `baseurl` 通常**只用一個**（另一個註解掉）；`gpgcheck` 與 `gpgkey` 通常一起用，確保套件完整安全。`$releasever`、`$basearch` 是變數，會自動被換成版本（如 9）與架構（x86_64）。

> [!tip] 想用學校／公司內部的鏡像站（或離線環境）
> 把 `mirrorlist` 註解掉，`baseurl` 改成內部網址，例如 `baseurl=http://mirror.local/rocky/$releasever/BaseOS/$basearch/os/`，就能讓內網主機不用連外網也能安裝更新。

### 第三方來源與 EPEL

預設來源裡沒有的套件（例如 `htop`、`fail2ban`），可以安裝 **EPEL**（Extra Packages for Enterprise Linux，Fedora 社群維護）：

```bash
sudo dnf install -y epel-release
```

⚠️ 第三方來源要確認可信任，並檢查 `gpgcheck=1`。

---

## 五、`dnf` 常用指令

### 指令總表

| 指令 | 說明 |
|---|---|
| `dnf search <關鍵字>` | 搜尋套件（名稱或描述） |
| `dnf info <套件>` | 套件詳細資訊（版本、來源 repo、摘要） |
| `dnf list <套件>` | 列出可用與已安裝的版本 |
| `dnf list installed` | 已安裝清單 |
| `dnf install <套件>` | 安裝（自動處理相依） |
| `dnf update [套件]` | 更新指定套件；**不指定就更新全部** |
| `dnf check-update` | 只檢查有哪些可更新，不實際更新 |
| `dnf remove <套件>` | 移除，**預設連不再使用的相依套件一併移除** |
| `dnf history` | 套件操作歷史 |
| `dnf provides <路徑>` | 查詢某檔案／指令屬於哪個套件 |
| `dnf repolist` | 目前啟用的 repo 清單（`--all` 看全部） |
| `dnf clean all` | 清除快取（下載的 rpm 與 metadata） |
| `dnf makecache` | 重新建立快取 |
| `dnf autoremove` | 清掉孤兒相依套件 |

常用選項：`-y` 全部自動回答 yes（腳本用；**手動操作時建議不要加，先看清單**）。

### 範例 1：查詢與安裝 httpd

```bash
sudo dnf list httpd
sudo dnf install httpd
```

安裝時 dnf 會先列出要安裝的清單，讓你確認：

```text
Dependencies resolved.
 Package            Arch    Version               Repository   Size
Installing:
 httpd              x86_64  2.4.53-11.el9_2.5     appstream    47 k
Installing dependencies:
 apr                x86_64  1.7.0-11.el9          appstream   123 k
 apr-util           ...
 httpd-core         ...
 mailcap            noarch  2.1.49-5.el9          baseos       32 k
Installing weak dependencies:
 mod_http2          ...
Transaction Summary
Install  12 Packages
Total download size: 2.0 M
Installed size: 6.0 M
Is this ok [y/N]: y
```

怎麼看：

- **Installing**：你要裝的套件。
- **Installing dependencies**：**必要相依**，沒有它們跑不起來，自動一起裝。
- **Installing weak dependencies**：**弱相依**（建議但非必要，例如 `mod_http2`）。
- `Repository`：這個套件來自哪個 repo（`baseos`、`appstream`…）。
- `Is this ok [y/N]`：預設是 N（要自己輸入 `y`）。
- 下載完會做 **transaction check／test**（先測試能不能裝），再執行安裝，最後 `Verifying` 驗證，`Complete!` 即完成。

> [!tip] 裝完不等於跑起來
> 安裝套件**不一定會啟動服務**，也不會自動開機啟動，更不會設好防火牆。要再做：
> ```bash
> sudo systemctl enable --now httpd
> systemctl status httpd
> ```
> 詳見 [[11 systemd 與日誌]]。

### 範例 2：移除

```bash
sudo dnf remove httpd
```

```text
Removing:
 httpd
Removing unused dependencies:
 apr  apr-util  httpd-core  mailcap  ...
Remove  12 Packages
Is this ok [y/N]:
```

**dnf 在移除時，會把「不再被其他套件使用」的相依套件一併清掉**（這是它比舊 yum 進步之處）。但要小心：**移除前看清楚清單**，有些套件可能是別的服務也要用的。

### 範例 3：套件操作歷史

```bash
sudo dnf history
```

```text
ID | Command line          | Date and time    | Action(s) | Altered
 4 | remove httpd          | 2023-09-12 22:09 | Removed   |   12
 3 | install httpd         | 2023-09-12 22:08 | Install   |   12
 2 | install -y mariadb-s… | 2023-05-12 00:43 | I, U      |   89
 1 |                       | 2023-02-16 16:28 | Install   |  336
```

（原文打成 `sudo history`，正確是 `dnf history`。）

進階：

```bash
sudo dnf history info 3        # 看第 3 次到底裝了什麼
sudo dnf history undo 3        # 還原第 3 次操作（反向操作）
sudo dnf history rollback 2    # 回到第 2 次之後的狀態
```

**稽核與還原利器**：出事了可以查「誰在什麼時候裝了什麼」。

### 範例 4：這個指令屬於哪個套件？

```bash
sudo dnf provides '*bin/awk'
# gawk-5.1.0-6.el9.x86_64 : The GNU version of the AWK text processing utility
# Repo        : @System
# Provide    : /bin/awk
```

- 路徑用單引號包起來，避免 Shell 提前展開 `*`。
- `Repo: @System` 代表目前已經安裝。
- **最常用的情境**：執行某指令出現 `command not found`，用 `dnf provides '*/指令名'` 找該裝哪個套件（例如 `dnf provides '*/named'`、`dnf provides '*/dig'` → `bind-utils`）。

### 範例 5：升級系統

```bash
sudo dnf check-update            # 先看有哪些更新
sudo dnf update                  # 全部更新
sudo dnf update nginx            # 只更新 nginx
sudo dnf upgrade --security      # 只套用安全性更新
sudo needs-restarting -r         # 需要重開機嗎？（dnf-utils）
```

> [!warning] 正式環境更新前
> 確認：維護時間窗、備份或 VM 快照、回復方式（`dnf history undo`）、這次更新會不會讓服務重啟。

---

## 六、一個標準的安裝流程

以 nginx 為例，每一步都在回答一個問題：

```bash
dnf search nginx                      # 1. 有這個套件嗎？
dnf info nginx                        # 2. 哪個版本、哪個 repo、做什麼的？
sudo dnf install nginx                # 3. 安裝，看清楚相依清單再輸入 y
rpm -q nginx                          # 4. 真的裝好了嗎？版本是？
rpm -qc nginx                         # 5. 設定檔在哪？
sudo systemctl enable --now nginx     # 6. 啟動並設為開機啟動
systemctl status nginx                # 7. 服務真的在跑嗎？
ss -lntp | grep ':80'                 # 8. 有在監聽 Port 嗎？
```

## 七、常見問題

| 問題 | 原因／解法 |
|---|---|
| `Failed to download metadata for repo` | 網路不通／DNS 不通／鏡像站失效。先確認 [[09 網路工具與組態]]：`ping`、`host`、`curl -I` |
| `No match for argument: xxx` | 套件名稱錯誤或來源沒啟用：`dnf search xxx`、`dnf repolist --all` |
| `GPG check FAILED` | 沒匯入公鑰，或套件被改過。確認來源可信再 `rpm --import` |
| `command not found` | `dnf provides '*/指令'` 找套件 |
| `Error: Unable to find a match` | 同上，或 minimal 安裝沒有 EPEL |
| 想看某個檔案是哪個套件裝的 | `rpm -qf 路徑` |
| 磁碟被 dnf 快取吃掉 | `sudo dnf clean all` |

> [!warning] 不要拿 `rpm -i` 取代 dnf
> `rpm -i` 不會解決相依性，也不會管 repository。日常安裝一律 `dnf install`，也可以直接 `dnf install ./foo.rpm`（本機 rpm 也能自動補相依）。
