---
tags: [Linux, 期末考, 練習, DNS, bind, 伺服器架設]
source: https://hackmd.io/@ntub-class/B12EXeiufx
---
# 期末練習與 DNS 補充

> [!abstract] 這份是什麼
> 課程目錄最後面放的「**114 學年度期末練習 1、2**」與「**DNS**（記錄種類、DNS Server）」。期末考是**上機實作、電腦評分**，題目會用到前面學過的幾乎所有技能，所以拿來當總複習最好。
>
> 每題我都整理了「**要做什麼 → 用到哪一章 → 解題思路與指令**」。指令是依照前面章節與常見做法寫的**參考解法**，不是官方答案，請在自己的練習 VM 上驗證。
>
> 總目錄：[[伺服器架設與規劃]]

原始頁面：[114 期末練習1](https://hackmd.io/@ntub-class/B12EXeiufx/%2FH5iKE2tkQm6V2jvg-4QtLg)、[練習1 評分](https://hackmd.io/@ntub-class/B12EXeiufx/%2FfHafsB7QSp2ymCoBTaxKEA)、[114 期末練習2](https://hackmd.io/@ntub-class/B12EXeiufx/%2FhjkhR_GzR0OQn2mD-LNOhw)、[練習2 評分](https://hackmd.io/@ntub-class/B12EXeiufx/%2FALHUyGGbQWG4flsoqf77eg)、[各種 DNS 記錄](https://hackmd.io/@ntub-class/B12EXeiufx/%2FmeYw6jxwRIShQRt5DdZ_Sw)、[DNS Server](https://hackmd.io/@ntub-class/B12EXeiufx/%2FvFzX8F1WR7SCQcZ1IKB7hQ)

> [!warning] 考試規則（練習1原文）
> - **不要修改 root 密碼**（會影響評分）。
> - 可以參考上課筆記或自己整理的筆記，**不可以使用任何 AI 工具**（ChatGPT、Claude、Gemini 等）。
> - 題目中的大寫 **X** 代表「你自己的考試代號」，不要照抄字母。
> - 考完要把 `server-1`、`server-2` **重新開機**後才評分（檢查的就是「重開機後還在不在」）。

---

## 一、考試通用心法

**重開機後仍有效 = 一定要寫進設定檔／啟用開機啟動。** 考題常見的陷阱：

| 要求 | 你要做 | 對應章節 |
|---|---|---|
| 「開機自動掛載」 | 寫 `/etc/fstab`，用 `mount -a` 測 | [[08 磁碟與檔案系統]] |
| 「開機自動啟動服務」 | `systemctl enable --now` | [[11 systemd 與日誌]] |
| 「IP 重開機仍在」 | `nmcli` 設 `connection.autoconnect yes` | [[09 網路工具與組態]] |
| 「防火牆允許」 | `firewall-cmd --permanent` + `--reload` | 見下 |
| 「時區」 | `timedatectl set-timezone` | [[07 時間與系統排程]] |

**防火牆小抄**（練習 DNS、Web 時都會用到）：

```bash
sudo firewall-cmd --list-all
sudo firewall-cmd --permanent --add-service=http      # 或 --add-port=80/tcp
sudo firewall-cmd --permanent --add-service=dns
sudo firewall-cmd --reload
```

`--permanent` 才會重開機後保留；沒加只有當下有效。

**邊做邊檢查**：每題做完就驗證一次，不要全做完才發現第一題就錯。

---

## 二、114 期末練習 1（試題編號 251201）

環境：兩台 EL9 VM（`EL9-Basic_ExamServer-1/2`），帳號 `student`。開始前要先執行**課程提供的部署腳本**（用你的代號），做完後重新開機再評分。

### 0. 部署考試機

由老師提供的腳本，把你的代號 X 傳進去，建立題目環境（原文用 `curl ... | exam_id=X bash` 的形式）。

> [!warning] 只在老師指定的考試 VM 上執行
> 「下載腳本直接丟給 bash 執行」本身有風險，請確認網址是老師公布的，且只在考試 VM 執行。

### 1. 設定 IP（對應第九章）

兩台各有一個**沒設 IP 的網路埠**，設為：

| 主機 | IP |
|---|---|
| server-1 | `192.168.X.11/24` |
| server-2 | `192.168.X.12/24` |

並用 `ping` 驗證互通，且「封包正確取得回應」（0% packet loss）。

```bash
ip -br link                           # 找出哪張網卡沒有 IP
nmcli connection show
sudo nmcli connection modify <連線名稱> ipv4.addresses 192.168.X.11/24 ipv4.method manual connection.autoconnect yes
sudo nmcli connection up <連線名稱>
ping -c 4 192.168.X.12
```

> 若該網卡還沒有對應的連線，用 `nmcli connection add type ethernet ifname <網卡> con-name <名稱> ...` 建一個。

### 2. 找出指定檔案（對應第二章）

在 server-2 的 `/etc/` 找出：**檔名是 UUID 格式、副檔名 `.exam`，且位於「名稱也是 UUID 格式」的目錄中**，複製成 `/tmp/exam_file.txt`。

```bash
sudo find /etc -type f -regextype posix-extended \
  -regex '.*/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\.exam'
# 找到後：
sudo cp <找到的路徑> /tmp/exam_file.txt
```

重點：UUID 格式是 `8-4-4-4-12` 個十六進位字元（第二章的練習）。

### 3. 套件安裝與 Repo（對應第十章）

server-2 上 `mail` 指令不能用，需補裝；套件必須來自 `appstream`，而且 `baseos` 這個 repo 被停用了，要先啟用。

```bash
dnf repolist --all                         # 看哪個 repo 是 disabled
sudo dnf config-manager --set-enabled baseos
# 或編輯 /etc/yum.repos.d/*.repo 把 baseos 的 enabled=0 改成 1
dnf provides '*/mail'                      # 找出 mail 指令由哪個套件提供（常是 s-nail / mailx）
sudo dnf install --repo appstream <套件>   # 指定從 appstream 安裝（或 --enablerepo / --disablerepo）
which mail
```

### 4. NTP 校時與時區（對應第七章）

server-2 用 chrony，來源只留：`watch.stdtime.gov.tw`、`clock.stdtime.gov.tw`，**取消其他來源**；時區 `Asia/Taipei`。

```bash
sudo vi /etc/chrony.conf
#   註解掉 pool ... iburst
#   新增：
#     server watch.stdtime.gov.tw iburst
#     server clock.stdtime.gov.tw iburst
sudo systemctl restart chronyd
chronyc sources -v
sudo timedatectl set-timezone Asia/Taipei
timedatectl
```

### 5. 帳號管理與目錄權限（對應第三、四章）— 這題最容易失分

**(a) 帳號**：建立群組 `avengers`，**所有新帳號主要群組都是 avengers**，帳號：`nick bruce tony odin thor loki`，密碼都是 `exam`。

```bash
groupadd avengers
for u in nick bruce tony odin thor loki; do
  useradd -g avengers $u
  echo "$u:exam" | chpasswd
done
```

**(b) 目錄**（server-2，**除指示外所有人無任何權限**）：

| 目錄 | 誰可以讀寫 |
|---|---|
| `/avenger/` 與全部子目錄 | `nick` |
| `/avenger/legal/` | `tony`（+ nick） |
| `/avenger/hr/` | `tony`、`bruce`（+ nick） |
| `/avenger/secret/` | `bruce`（+ nick） |
| `/avenger/bifrost/` | `bruce`、`odin`、`thor`、`loki`（+ nick） |
| `/avenger/temp/` | 上述所有帳號都可讀取與寫入 |

**思路**：因為所有人主要群組都是 `avengers`，**不能用「avengers 群組」授權**（那樣全部人都有權限）。需要用 **ACL**（`setfacl`）針對特定使用者，或為每個目錄建專用群組。ACL 最直接：

```bash
mkdir -p /avenger/{legal,hr,secret,bifrost,temp}
chmod -R 700 /avenger            # 先全關（擁有者 root 外，其他人 none）
chown -R root:root /avenger

# 讓 nick 可以進入並讀寫所有（含日後新增的）：
setfacl -R -m u:nick:rwx /avenger
setfacl -R -d -m u:nick:rwx /avenger        # -d 預設 ACL，之後新增的子項目也繼承

setfacl -m  u:tony:rwx  /avenger/legal /avenger/hr
setfacl -m  u:bruce:rwx /avenger/secret /avenger/bifrost /avenger/hr
setfacl -m  u:odin:rwx,u:thor:rwx,u:loki:rwx /avenger/bifrost
for u in nick bruce tony odin thor loki; do setfacl -m u:$u:rwx /avenger/temp; done

# 要進到子目錄，上層 /avenger 必須讓這些人有 x（進入權限）：
for u in tony bruce odin thor loki; do setfacl -m u:$u:--x /avenger; done
getfacl -R /avenger | less                  # 檢查
```

> 「讀寫」要同時給 `r` 和 `w`；**目錄還需要 `x` 才能進入**。這是第四章的核心觀念。
> 替代做法（不用 ACL）：為每個目錄建一個專用群組（如 `g_hr`），把需要的人用 `usermod -aG` 加進去，目錄設 `chgrp g_hr` + `chmod 770`。

### 6. 磁碟掛載（對應第八章）

server-2 把 `/dev/sdb` 掛到 `/exam_resource/`，重開機後自動掛載。

```bash
lsblk -f                                      # 先看 sdb 有沒有已經格式化
# 如果題目已提供檔案系統就不要再 mkfs；沒有才 sudo mkfs.xfs /dev/sdb
sudo mkdir -p /exam_resource
sudo blkid /dev/sdb                           # 取 UUID
sudo vi /etc/fstab                            # 加：UUID=... /exam_resource xfs defaults 0 0
sudo systemctl daemon-reload
sudo mount -a
df -h /exam_resource
```

> ⚠️ 這題後面的第 8、10 題會用到 `/exam_resource/` 裡的檔案（`db_backup`、`ap_backup`），**表示 sdb 上可能已有資料**，不要隨便 `mkfs`！

### 7. 程式位置與 PATH（對應第二章）

`/opt/exam_check_disk` 是 Shell Script，每次都要打完整路徑。把它移到「在 `$PATH` 裡的目錄」，讓使用者直接輸入 `exam_check_disk`。

```bash
echo $PATH
sudo mv /opt/exam_check_disk /usr/local/bin/
ls -l /usr/local/bin/exam_check_disk          # 確認有執行權限
exam_check_disk
```

`/usr/local/bin/` 是放「管理員自行安裝的指令」的標準位置，也在 PATH 內。

### 8. 問題行程偵查（對應第六、十一章）

SYSLOG 一直出現沒看過的記錄（有顯示 PID），找出寫 log 的行程：

1. 把目標程式**複製**到 `/exam_resource/`（保留原檔名，**取消執行權限**）。
2. 找出**觸發它執行的設定檔案**，把**觸發的那一行**取消（註解／刪除）。
3. 把目標程式**刪除**。

思路：

```bash
sudo journalctl -f                              # 或 tail -f /var/log/messages，看反覆出現的記錄與 PID
ps -p <PID> -o pid,ppid,user,cmd                # 該行程是什麼指令
ls -l /proc/<PID>/exe                           # 實際執行檔位置
sudo cp -p <程式路徑> /exam_resource/ ; sudo chmod -x /exam_resource/<檔名>
# 誰觸發的？最常見是 cron：
sudo cat /etc/crontab ; ls /etc/cron.d/ ; sudo crontab -l ; sudo grep -r '<程式名>' /etc/cron* /var/spool/cron
# 也可能是 systemd timer / service：systemctl list-timers
sudo vi <設定檔>                                # 把那一行註解掉
sudo kill <PID>                                 # 若還在跑，先停掉
sudo rm <程式路徑>
```

這題整合了第六章（看 PID、PPID）、第七章（cron）、第十一章（journal）。

### 9. 停用檔案型 Swap（對應第八章）

有一個 Swap 是以「檔案」提供，要停用，且重開機後不能再自動啟用。

```bash
swapon --show                  # 找出哪個是 file 型（TYPE=file）
sudo swapoff /swapfile         # 立即停用（路徑依 swapon --show 為準）
sudo vi /etc/fstab             # 把該 swap 那一行刪除或註解
sudo systemctl daemon-reload
swapon --show ; free -h        # 確認
# 可選：sudo rm /swapfile
```

**重點**：重開機會不會再啟用，取決於 `/etc/fstab`；只 `swapoff` 沒改 fstab，重開又回來。

### 10. Web + PHP + MariaDB 整合（總合題）

在 server-2：

**(a) 資料庫**：`/exam_resource/db_backup/` 有 `.sql`，用它還原。`root` 密碼 `P@ssw0rd`，建立資料庫 `exam` 並還原。

```bash
sudo dnf install -y mariadb-server
sudo systemctl enable --now mariadb
sudo mysql_secure_installation              # 設定 root 密碼為 P@ssw0rd
mysql -uroot -p -e "CREATE DATABASE exam;"
mysql -uroot -p exam < /exam_resource/db_backup/<檔名>.sql
mysql -uroot -p -e "SHOW TABLES;" exam
```

**(b) Web 與 PHP**

```bash
sudo dnf install -y httpd php php-mysqlnd php-pdo
sudo systemctl enable --now httpd
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

`php-mysqlnd` 同時提供 PDO MySQL 與 mysqli 驅動。

**(c) PHP 程式**：`/exam_resource/ap_backup/myid.php`，第 11 行要設成 `$pass = 'P@ssw0rd';`，再部署到 Apache 可讀取的目錄（預設 `/var/www/html/`）。

```bash
sudo vi /exam_resource/ap_backup/myid.php          # 第 11 行改密碼（vi 中輸入 :11 跳行）
sudo cp /exam_resource/ap_backup/myid.php /var/www/html/
```

**(d) 驗證**：在 server-2 執行 `curl http://serverX/myid.php`，必須輸出自己的 X 編號。

> [!tip] 如果 curl 收到 PHP 原始碼或 403/500
> - 是原始碼：PHP 模組沒裝或 httpd 沒重啟 → `systemctl restart httpd`。
> - 403：檔案權限／SELinux（`ls -Z`，`restorecon -Rv /var/www/html`）。
> - 500：看 `/var/log/httpd/error_log`，多半是連不上資料庫（密碼、資料庫名）。
> - SELinux 擋 httpd 連 DB：`setsebool -P httpd_can_network_connect_db 1`。

### 評分

重開機後，用 root 在 server-2 執行老師提供的評分腳本（`curl -s <老師的網址>/rs.sh | bash`），看每題是否通過。

---

## 三、114 期末練習 2

環境：VMware Workstation Player 開 `exam-server1`、`exam-server2`。用 root（密碼 `exam`，**不要改**）登入後，執行 `set-exam-id X` 初始化題目。兩台互連使用 **`10.6.X.0/24`**。

### 網路架構與 VMware 設定

- Server1、Server2 **各新增 2 張網卡**：Network Adapter = **NAT**，Network Adapter2 = **Bridge**。
- 作業系統設定：

| 主機 | 網卡 1 | 網卡 2 |
|---|---|---|
| Server1 | DHCP | `10.6.X.11` / `255.255.255.0` |
| Server2 | DHCP | `10.6.X.12` / `255.255.255.0` |

- 兩台要能以 10.6.X.0/24 互通。（`nmcli connection modify ... ipv4.method manual` + `connection up`）

### 題目一覽與解法方向

| # | 題目 | 重點與指令 |
|---|---|---|
| 2 | Server2 `/etc/` 找出 **UUID 命名、副檔名 `.txt`、位於 UUID 目錄中**的檔案，複製為 `/tmp/file` | `find` + 正規表示式（同練習 1 第 2 題，副檔名改 `.txt`） |
| 3 | Server1、Server2 用 chrony 校時為 `time.stdtime.gov.tw`；時區 `Asia/Taipei` | SOP：編輯 `/etc/chrony.conf` → 刪/註解 `pool ... iburst` → 新增 `server time.stdtime.gov.tw iburst` → `systemctl restart chronyd` → `chronyc sources` 檢查 |
| 4 | Server1：建群組 `staff`，所有新帳號主要群組 staff；帳號 `rowling potter ron hermione dumbledore voldemort`，密碼 `exam` | `groupadd`、`useradd -g staff`、`chpasswd` |
| 5 | Server1 目錄 `/folder`：rowling 可讀寫全部；voldemort 讀寫 `legal` 與 `hr`；dumbledore 讀寫 `secret`、`it`、`hr`；potter／ron／hermione 讀寫 `it`；**其他人無權限** | 同練習 1 第 5 題，用 ACL 或專用群組 |
| 6 | Server2：`/dev/sdb` 掛到 `/web-roots`，開機自動掛載 | `mkfs.xfs`（若需要）+ fstab UUID + `mount -a` |
| 7 | Server2 **NFS 服務**：只讓 `10.6.X.0/24` **唯讀**存取 `/web-roots`，重開機自動啟用；實體目錄**不可**是 `rwxrwxrwx` | 見下 |
| 8 | Server1：MariaDB 開機啟動；root 密碼 `exam`；建立 `exam` 資料庫並用 `/db-backup/db.sql` 還原 | 同練習 1 第 10 題(a) |
| 9 | Server1：httpd + PHP（需 `pdo` 與 `mysqli`）；把 server2 的 NFS 分享掛到 `/var/www/html`（開機自動）；設定三個虛擬主機 `web1.exam.class`、`web2.exam.class`、`hello.exam.class`，對應 `/var/www/html/<網域名>` | 見下 |
| 9' | Server2 驗證：`http://web1.exam.class` 首頁顯示 `web1`；`http://web2.exam.class` 顯示 `web2`；`http://hello.exam.class/myid.php` 顯示 `MYIDX` | 內容放在 NFS 目錄（server2 的 `/web-roots`）裡 |

> 注意事項：驗收前把 Server1 與 Server2 **重新開機後不要再登入**，直接評分。

### NFS 參考做法（Server2）

NFS（網路檔案系統）讓一台主機把目錄「分享」給其他主機掛載使用。

```bash
sudo dnf install -y nfs-utils
sudo mkdir -p /web-roots/{web1.exam.class,web2.exam.class,hello.exam.class}
sudo chmod 755 /web-roots           # 別用 777（題目禁止）
sudo vi /etc/exports
#   /web-roots  10.6.X.0/24(ro,sync)        ← ro = 唯讀
sudo systemctl enable --now nfs-server
sudo exportfs -rav
sudo firewall-cmd --permanent --add-service={nfs,mountd,rpc-bind}
sudo firewall-cmd --reload
showmount -e localhost
```

### Web（Server1）參考做法

```bash
sudo dnf install -y httpd php php-mysqlnd nfs-utils mariadb-server
# 掛載 server2 的 NFS，開機自動（fstab）：
#   10.6.X.12:/web-roots  /var/www/html  nfs  defaults,_netdev  0 0
sudo mount -a

# 三個 Virtual Host：/etc/httpd/conf.d/vhosts.conf
#   <VirtualHost *:80>
#       ServerName web1.exam.class
#       DocumentRoot /var/www/html/web1.exam.class
#   </VirtualHost>
#   （web2、hello 同理）
sudo apachectl configtest
sudo systemctl enable --now httpd
```

驗證端要讓 `web1.exam.class` 等名稱能解析：在 `/etc/hosts` 加 `10.6.X.11 web1.exam.class web2.exam.class hello.exam.class`，再 `curl http://web1.exam.class`。

> [!note] NFS 與 SELinux
> httpd 要讀 NFS 上的內容需開 SELinux 布林值：`setsebool -P httpd_use_nfs 1`（和 `httpd_can_network_connect_db`）。SELinux 在 12/14 的課程會講。

### 評分

重開機後，在 Server1 以 root 執行老師提供的評分腳本。頁面還附有一支講解影片（YouTube）可以參考。

---

## 四、DNS（網域名稱系統）

> 後半學期（11/16 起）會學 DNS 用戶端與 Apache，這裡先整理老師放在目錄最後的兩頁。

### DNS 是什麼？

人類記名稱（`www.example.com`），電腦用 IP 通訊。DNS 就是**把名稱翻譯成 IP** 的系統。老師的說法：「DNS 是所有資訊服務應用之母。」

| | 方向 | 說明 |
|---|---|---|
| **正解**（Forward） | 名稱 → IP | 最常用 |
| **反解**（Reverse） | IP → 名稱 | 依需求設定，記錄是 PTR |

重點觀念：

- DNS 是**授權式、分散式**結構。上層網域可以把子網域「**委派**」出去，之後子網域底下的記錄由子網域自己管，上層只告訴查詢者「子網域的負責主機在哪」。
- 協定規範在 **RFC 1035**；記錄種類可參考維基百科「List of DNS record types」。
- 使用 **UDP 53**；回應超過 512 bytes 時改用 **TCP 53**。所以防火牆要**同時**放行 TCP/53 與 UDP/53。
- EL8/EL9 使用 **`bind-chroot`** 套件：BIND 加上 chroot 隔離，增加安全性。主要設定檔 `/etc/named.conf`，記錄檔放 `/var/named/`。

### 常見 DNS 記錄類型

| 類型 | 用途 | 範例 |
|---|---|---|
| **SOA** | 區域授權起始，記載序號、更新週期等 | `@ IN SOA ...` |
| **NS** | 這個網域由哪台名稱伺服器負責 | `@ NS ns` |
| **A** | 名稱 → IPv4 | `www IN A 192.168.20.1` |
| **AAAA** | 名稱 → IPv6 | |
| **CNAME** | 別名，指向另一個名稱 | `web IN CNAME www` |
| **MX** | 郵件伺服器 | |
| **TXT** | 文字註記（SPF、網域驗證等） | `www IN TXT "WEB HOSTING to here"` |
| **PTR** | IP → 名稱（反解） | |

### 練習：架設 DNS Server（Server2 實作，Server1 驗證）

**目標**：了解 DNS 設定、運作機制，用 `bind` 完成需求。以下 `X` 是你的代號，`domainX.linux.class` 是自訂的練習網域。

**1. 安裝套件**

```bash
dnf list bind-chroot
sudo dnf install -y bind-chroot
ls -lh /etc/named.conf        # 主要設定檔
ls -lh /var/named/            # 記錄檔位置
```

**2. 修改主要設定檔**

```bash
sudo cp -a /etc/named.conf /etc/named.conf_backup     # 先備份！
sudo vi /etc/named.conf
```

需要修改的位置：

```text
listen-on port 53 { 127.0.0.1; 172.16.2.X; };       # 大約第 11 行：監聽本機和自己的 IP
recursion no;                                        # 大約第 31 行：不提供遞迴查詢（只回答自己負責的網域）
dnssec-enable no;                                    # 大約第 33 行（舊版 BIND）
dnssec-validation no;

# 在 zone "." 區塊後新增我們自己的區域：
zone "domainX.linux.class" IN {
    type master;                                     # 這台是主要（master）伺服器
    file "db.domainX.linux.class";                   # 區域資料檔（放在 /var/named/）
    allow-query { any; };                            # 允許任何人查詢
};
```

> [!note] `dnssec-enable` 在新版會報錯
> `dnssec-enable` 選項在 BIND 9.16 以後已被移除；如果你的 Rocky 版本啟動 named 時出現 `unknown option 'dnssec-enable'`，把那行刪掉就好（`dnssec-validation no;` 保留）。這份教材是以 EL8 示範的。

**3. 建立區域資料檔**

```bash
cd /var/named
sudo cp -a named.empty db.domainX.linux.class        # 以範本複製，保留權限
sudo vi db.domainX.linux.class
```

```text
$TTL 3H
@   IN SOA  @ nsadmin.domainX.linux.class. (
                1       ; serial   序號（每次修改都要+1，否則從屬伺服器不會更新）
                1D      ; refresh  從屬多久檢查一次
                1H      ; retry    失敗後多久重試
                1W      ; expire   多久沒聯絡就失效
                3H )    ; minimum  負面快取時間
@       NS      ns
ns  0   IN  A   172.16.2.X
```

- `@` 代表網域本身（domainX.linux.class）。
- 網域名稱結尾的 `.`（點）很重要：寫了 `.` 代表是完整名稱；沒寫會自動接上網域名。
- `nsadmin.domainX.linux.class.` 是管理者信箱（`@` 以 `.` 表示）。

**4. 啟動服務**

```bash
sudo systemctl enable named-chroot
sudo systemctl start  named-chroot
```

服務名稱是 **`named-chroot`**（因為裝的是 bind-chroot）。要用 `enable --now` 一次完成也行。

**5. 防火牆**

```bash
sudo firewall-cmd --permanent --add-service=dns
sudo firewall-cmd --reload
sudo firewall-cmd --list-all | grep dns
#   services: cockpit dhcpv6-client dns ssh
```

**6. 確認 Port 有開**

```bash
sudo ss -ntulp | grep :53
# udp UNCONN ... 172.16.2.11:53 ... users:(("named",pid=2444,fd=513))
# tcp LISTEN ... 172.16.2.11:53 ... users:(("named",pid=2444,fd=22))
```

應該同時看到 **UDP 53 與 TCP 53**，且分別在 `127.0.0.1`、你的 IP 與 `::1` 上。

**7. 本機驗證**

```bash
sudo dnf install -y bind-utils
host -t ns domainX.linux.class 127.0.0.1
# domainX.linux.class name server ns.domainX.linux.class.
host ns.domainX.linux.class 127.0.0.1
# ns.domainX.linux.class has address 172.16.2.X
```

**8. 從其他主機（Server1）驗證**

```bash
host -t ns domainX.linux.class 172.16.2.X        # 注意：要指定 Server2 的 IP，或把 Server1 的 DNS 指向 Server2
host ns.domainX.linux.class 172.16.2.X
```

> 原文在 Server1 上沒指定 DNS 伺服器，前提是 Server1 的 DNS 已經設成 Server2（可用 `nmcli connection modify <名稱> ipv4.dns 172.16.2.X` 設定）。最保險是在 `host` 指令最後面加上 DNS 伺服器 IP。

### 練習：新增各種 DNS 記錄（Server2）

編輯區域檔，在 NS 記錄之後加入：

```bash
sudo vi /var/named/db.domainX.linux.class
```

```text
myweb  0  IN  A      192.168.1.20

; 設定 TXT 註記
www    0  IN  TXT    "WEB HOSTING to here"

; 設定 IPv4 Round-Robin（同一個名稱對應兩個 IP，輪流回應，簡易負載分散）
www    0  IN  A      192.168.20.1
www    0  IN  A      192.168.20.2

; 設定別名記錄
web    0  IN  CNAME  www
web1   0  IN  CNAME  www
web2   0  IN  CNAME  www
```

重新載入：

```bash
sudo rndc reload
```

> 修改後別忘了把 SOA 的 `serial` 加 1，習慣上會用日期格式如 `2026112001`。

**在 Server1 驗證**

```bash
host -t a   myweb.domainX.linux.class        # A 記錄
host -t a   www.domainX.linux.class          # 會看到兩個 IP（Round-Robin）
host -t txt www.domainX.linux.class          # 文字註記
host        web.domainX.linux.class          # 別名 → www → 兩個 IP
host -t cname web1.domainX.linux.class
host -t cname web2.domainX.linux.class
```

| 記錄 | 預期結果 |
|---|---|
| `host -t a www...` | 回兩個 IP：192.168.20.1、192.168.20.2 |
| `host -t txt www...` | `descriptive text "WEB HOSTING to here"` |
| `host web...` | `web... is an alias for www...` 然後列出 www 的位址 |
| `host -t cname web1...` | `web1... is an alias for www...` |

排錯：`systemctl status named-chroot`、`journalctl -u named-chroot -b`、`named-checkconf`、`named-checkzone domainX.linux.class /var/named/db.domainX.linux.class`（檢查語法超好用）。

---

## 五、考前檢查表

- [ ] 能不看筆記設定 IP（`nmcli`）、時區、chrony 來源
- [ ] 能建立帳號／群組並設定 `chpasswd`
- [ ] 能用 ACL 或群組設計多人目錄權限，並用 `su -` 切換帳號驗證
- [ ] 能掛載磁碟並寫入 `/etc/fstab`，`mount -a` 無錯誤
- [ ] 能用 `find` + 正規表示式找 UUID 檔案
- [ ] 能找出可疑行程與觸發它的 cron
- [ ] 能安裝 httpd / php / mariadb 並 `enable --now`，開防火牆
- [ ] 每題做完都**重開機驗證**
