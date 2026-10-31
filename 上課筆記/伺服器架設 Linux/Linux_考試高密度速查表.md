---
tags: [Linux, 伺服器架設, 考試, 速查表]
---

# Linux 伺服器架設｜考試高密度速查表

> 適用：Rocky / RHEL 9。列印建議：A4 橫式、雙欄、邊界窄、9–10 pt；內容設計為約兩面 A4。`<...>` 必須替換成實際值；先確認目標再執行會修改資料的指令。

## 0. 考試 SOP（每題完成即驗證）

`whoami; pwd; ip -br a; lsblk -f; systemctl status <服務>`  
需重開機仍有效：IP→`nmcli`＋`autoconnect`；服務→`systemctl enable --now`；掛載/Swap→`/etc/fstab`＋`mount -a`；防火牆→`--permanent`＋`--reload`。  
排錯順序：設定檔→服務 `status`→日誌 `journalctl -u <svc> -b`→監聽 `ss -tulpen`→防火牆→SELinux。

## 1. 核心觀念／檔案

- 系統：`uname -r`、`cat /etc/os-release`、`hostnamectl`；主機名檔：`/etc/hostname`，改：`hostnamectl set-hostname <name>`。
- 路徑：`/` 根、`~` 家目錄、`.` 目前、`..` 上層、`-` 前一目錄；絕對路徑以 `/` 起始。
- 檔案：`ls -lah`、`stat <檔>`（inode/大小/時間/SELinux）、`file <檔>`、`touch <檔>`（建空檔／更新時間）；`cp -a` 保留屬性；`mv -i`；`rm -ri`；`mkdir -p a/b/c`。
- 檢視／搜尋：`cat -n`、`less`（`/字` 搜尋，`q` 離開）、`head -n N`、`tail -f`；`grep -rinE 'pat' <路徑>`；`find <路徑> -type f -name '*.log'`；`awk -F: '{print $1}' /etc/passwd`；`sed -i 's/a/b/g' f`；`cut -d: -f1 f | sort | uniq -c`。
- `find` 時間：`-mtime -1` 一天內、`n` 約 n 天前、`+n` 超過 n 天；指令位置：`which`、`type`、`echo $PATH`、`export PATH=$PATH:/opt`。
- vim：`i` 插入、`Esc` 指令；`:w`、`:q`、`:wq`、`:q!`；`dd/yy/p/u`；`/字`；`gg/G`。歷史：`!!`、`!18`、`!mkdir`。

## 2. 帳號、群組、權限

- 資料庫：`/etc/passwd`（7欄帳號資料）、`/etc/shadow`（密碼/期限）、`/etc/group`（群組）。`id <user>` 查 UID/GID/群組。
- 帳號：`useradd -m -s /bin/bash -g <主要群組> -G <附加群組> u`；`passwd u`；`usermod -aG wheel u`（不可漏 `-a`）；`userdel -r u`；`chage -l u`；`groupadd g`；`gpasswd -a u g`；`su - u`／`sudo <cmd>`。
- 批次：`newusers users.txt`（passwd 同格式 7 欄）；`chpasswd < pw.txt`（`帳號:密碼`）。名單含明碼，考後刪除。
- 權限：`r=4,w=2,x=1`；`ls -l`：類型／u／g／o。檔案：r讀、w改、x執行；目錄：r列出、w建刪、x進入/穿越。常用：644、600、755、700、777、770、775。
- `chmod 640 f`／`chmod u+x f`；`chown u:g f`；`chgrp g f`；`umask 027`。ACL：`getfacl f`；`setfacl -m u:alice:rwx dir`；預設繼承：`setfacl -d -m u:alice:rwx dir`。多人目錄先限縮為 `700`，再以 ACL 精準授權；子目錄使用者也需父目錄 `x`。

## 3. 重導、行程、時間

- FD：stdin=0、stdout=1、stderr=2。`>f` 覆寫、`>>f` 追加、`2>err`、`>out 2>err`、`>all 2>&1`／`&>all`、`<in`、`cmd1 | cmd2`、`cmd | tee log | cmd2`。**`2>&1` 必須在 `>檔案` 後面**；`cat f > f` 會先截斷，檔案清空。
- 資源：`top`（`P` CPU、`M` MEM）、`free -h`、`uptime`（load average）、`df -hT`、`du -sh /var/*`、`df -i`、`lsblk -f`。行程：`ps auxf`／`ps -ef --forest`／`pstree -p`；`pgrep <名>`、`pidof <名>`；先 `kill -TERM PID`，無效才 `kill -KILL PID`。
- 時間：`timedatectl`；`timedatectl set-timezone Asia/Taipei`；`timedatectl set-ntp true/false`；`hwclock -w`（系統→RTC）、`-s`（RTC→系統）；chrony：編 `/etc/chrony.conf`，`server <host> iburst`，`systemctl restart chronyd`，`chronyc sources -v`。
- cron：`分 時 日 月 週 命令`；`crontab -e/-l`；`/etc/crontab` 多「執行者」欄。例：`0 2 * * * /usr/local/sbin/backup.sh >>/var/log/backup.log 2>&1`；看 log：`tail -f /var/log/cron`。`systemctl list-timers` 查 systemd timer。

## 4. 磁碟、網路、套件、服務

- 磁碟：`lsblk -f`→確認目標→（必要才）`mkfs.xfs /dev/sdb`→`mkdir -p /data`→`mount /dev/sdb /data`→`blkid /dev/sdb`→fstab：`UUID=<uuid> /data xfs defaults 0 0`→`mount -a`→`findmnt /data`。`umount /data`；XFS 線上擴：`xfs_growfs /掛載點`（只能擴，參數是掛載點）。
- 網路：`ip -br a`、`ip route`、`ping -c 4 <gateway>`、`ss -tulpen`、`host <name> <dns>`／`dig +short <name>`、`curl -I <url>`、`traceroute <host>`。診斷：介面→路由/閘道→DNS→HTTP→Port。
- IP：`nmtui`，或 `nmcli con modify <連線> ipv4.method manual ipv4.addresses <IP/遮罩> ipv4.gateway <GW> ipv4.dns <DNS> connection.autoconnect yes`；`nmcli con up <連線>`。NAT 以 VMnet8 的**網段/MAC**判斷，勿只看 ens 編號。
- 套件：`rpm -q/-qi/-ql/-qf <檔>`；`dnf search/info/install/remove/update <套件>`；`dnf provides '*/命令'`；`dnf repolist --all`；repo：`/etc/yum.repos.d/*.repo`，`dnf config-manager --set-enabled <repo>`。rpm 不解相依，安裝優先 dnf。
- systemd：`systemctl status/start/stop/restart/reload <svc>`；`enable --now`=開機啟動＋立即啟動；`disable --now`；`is-active/is-enabled`；`list-units --type=service --state=failed`。日誌：`journalctl -u <svc> -b -n 100 -f`；`logger -t tag -p user.info 'msg'`。
- 防火牆：`firewall-cmd --list-all`；`firewall-cmd --permanent --add-service={http,dns,nfs,mountd,rpc-bind}`；`firewall-cmd --reload`。SELinux 常見：`restorecon -Rv /var/www/html`、`setsebool -P httpd_can_network_connect_db 1`、`setsebool -P httpd_use_nfs 1`。

## 5. 題庫練習 30 題｜極短答案（必背）

|題|答案|
|---|---|
|Q1 安裝 httpd|`sudo dnf install httpd`；確認：`rpm -q httpd`；啟用：`systemctl enable --now httpd`|
|Q2 移除 httpd|`sudo dnf remove httpd`|
|Q3 設 IP|`sudo nmtui`；或 `nmcli con modify ...` 後 `nmcli con up <連線>`|
|Q4 Windows 網路連線|Win+R：`ncpa.cpl`|
|Q5 找 NAT 網卡|比對 `ip a` IP 網段/MAC 與 VMware VMnet8；不可只猜 ens160/ens192|
|Q6 主機名檔／改名|`/etc/hostname`；`hostnamectl set-hostname Server1`（重登入看提示字元）|
|Q7 `touch` 另一功能|檔案不存在時建立 0 byte 空檔；`touch -d '2026-01-01 08:00' f` 指定時間|
|Q8 詳細檔案屬性|`stat /etc/passwd`|
|Q9 遞迴列目錄|`ls -R a/`；保留 X 排序：`ls -XR a/`|
|Q10 重跑 history 第 18 條|`!18`|
|Q11 `:` 改 `,` 且寫回|`sed -i 's/:/,/g' sample1`|
|Q12 刪含 sync 的行|`sed -i '/sync/d' sample1`|
|Q13 腳本可執行|`chmod +x /opt/hello` 或 `chmod 755 /opt/hello`；首行 `#!/bin/bash`|
|Q14 顯示 PATH|`echo $PATH` 或 `printenv PATH`|
|Q15 批次帳號／密碼|`newusers users.txt`；或 `for...useradd...; chpasswd < pw.txt`|
|Q16 多層建 `/class`|`sudo mkdir -p /class/{public,grp1,grp2}`|
|Q17 public/grp1/grp2 權限|`chmod 777 public; chmod 770 grp1; chmod 775 grp2`|
|Q18 stdout+stderr 存檔|`ls sample2 >log.txt 2>&1` 或 `ls sample2 &>log.txt`|
|Q19 `cat log.txt >log.txt`|檔案先被重導截斷，內容變空|
|Q20 top 前 3 支程式|`top -b -n 1 | head -n 10 | tail -n 3`|
|Q21 樹狀行程|`ps auxf`／`ps -ef --forest`／`pstree -p`|
|Q22 依名稱找 PID|`pgrep httpd`／`pidof sshd`|
|Q23 讓 NTP inactive|`systemctl stop chronyd` 或 `timedatectl set-ntp false`|
|Q24 台北時區|`timedatectl set-timezone Asia/Taipei`|
|Q25 CPU 53.5% 篩 PID|`ps aux | awk '$3 >= 53 {print $2}'`（第3欄 CPU、第2欄 PID）|
|Q26 結束 Q25 篩出的 PID|`kill $(ps aux | awk '$3 >= 53 {print $2}')`；先確認篩選結果|
|Q27 系統時間寫入 RTC|`hwclock -w`|
|Q28 即時看 cron log|`tail -f /var/log/cron` 或 `journalctl -u crond -f`|
|Q29 測試 fstab|`umount /mydata; mount -a; df -h /mydata`|
|Q30 擴充 XFS|`xfs_growfs /mydata`（掛載點，非 `/dev/sdb`）|

## 6. 期末實作題型（濃縮清單）

- UUID 檔：`find /etc -type f -regextype posix-extended -regex '.*/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\.exam'`；找到後 `cp <結果> /tmp/exam_file.txt`（`.txt` 題型僅改副檔名）。
- 多人目錄：所有帳號同一主要群組時不可直接授權該群組；用 ACL。先 `chmod -R 700 /目錄`，`setfacl -m u:<user>:rwx <目錄>`；使用者需上層 `--x`；未來新增內容需 `setfacl -d -m ...`。
- 可疑行程：`journalctl -f`→記 PID→`ps -p PID -o pid,ppid,user,cmd`＋`ls -l /proc/PID/exe`→`cp -p <程式> /exam_resource/; chmod -x ...`→`grep -r '<程式名>' /etc/cron* /var/spool/cron`／`systemctl list-timers`→停觸發、`kill PID`、刪原程式。
- Swap：`swapon --show`→`swapoff <file>`→註解 `/etc/fstab` swap 行→`swapon --show; free -h`。
- Web/DB：`dnf install -y mariadb-server httpd php php-mysqlnd php-pdo`；`systemctl enable --now mariadb httpd`；`mysql -uroot -p -e 'CREATE DATABASE exam;'`；`mysql -uroot -p exam < backup.sql`；部署 PHP 至 `/var/www/html/`；開 http 防火牆；`curl http://localhost/file.php`。
- NFS：Server2 `/etc/exports`：`/web-roots 10.6.X.0/24(ro,sync)`；`dnf install nfs-utils`；`systemctl enable --now nfs-server`；`exportfs -rav`；Server1 fstab：`10.6.X.12:/web-roots /var/www/html nfs defaults,_netdev 0 0`；`mount -a`。
- DNS：A=名稱→IPv4、AAAA=IPv6、CNAME=別名、MX=郵件、NS=名稱伺服器、PTR=反解、TXT=文字。改 zone 後 SOA serial +1，`named-checkconf`、`named-checkzone <zone> <file>`、`rndc reload`；查：`host -t a/txt/cname <名稱> <DNS-IP>`。

## 7. 最後 60 秒

`mount -a` 無錯；`systemctl is-enabled <svc>`；`firewall-cmd --list-all`；`ip -br a`；`ping -c 4 <對端>`；`ss -tulpen`；`curl`／`host` 實測；`reboot` 後再驗證。**勿改 root 密碼；題目 X 代入本人代號。**
