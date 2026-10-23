---
tags: [Linux, systemd, systemctl, journal]
---
# systemd 與日誌

`systemd` 負責開機初始化、服務啟動與相依性；`systemctl` 是主要操作介面。

```bash
systemctl status sshd
systemctl start sshd
systemctl stop sshd
systemctl restart sshd
systemctl enable sshd
systemctl disable sshd
systemctl list-units --type=service
```

`start`／`stop` 影響目前狀態；`enable`／`disable` 影響開機是否啟動。

## journal

```bash
journalctl
journalctl -b
journalctl -u sshd
journalctl -f
journalctl --since "1 hour ago"
journalctl -p err
```

服務異常時，先看 `systemctl status`，再用 `journalctl -u 服務名稱` 對照錯誤。

- [原始章節](https://hackmd.io/@ntub-class/B12EXeiufx/%2FbRIPVHIERvazp-vfsogMoA)

## 從零開始理解

可以把服務想成「長時間在背景執行的程式」，例如 SSH、Web server、資料庫。systemd 是負責開機、啟動服務、停止服務、處理相依關係與收集日誌的系統管理器。

### start 與 enable 的差異

```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

- `start`：現在立刻啟動，但重開機後不一定會自動啟動。
- `enable`：設定開機自動啟動，但不一定現在就啟動。
- `enable --now`：兩件事一起做。

```bash
sudo systemctl enable --now nginx
systemctl is-active nginx
systemctl is-enabled nginx
```

### 服務故障的初學者流程

```bash
systemctl status nginx --no-pager
journalctl -u nginx -b -n 100 --no-pager
ss -lntp | grep ':80'
```

依序回答：

1. systemd 認為服務是 active、failed 還是 inactive？
2. 本次開機的日誌有沒有錯誤？
3. 服務是否真的監聽預期的 Port？
4. 設定檔是否正確、權限是否足夠？
5. 防火牆是否允許外部連線？

### journal 的重要參數

- `-u nginx`：只看 nginx。
- `-b`：只看本次開機。
- `-n 50`：顯示最近 50 行。
- `-f`：持續追蹤新訊息，類似 `tail -f`。
- `-p err`：只看錯誤等級。
- `--since "10 minutes ago"`：限定時間。

> [!warning] restart 不是萬靈丹
> `systemctl restart` 只是重新啟動服務，不能修正錯誤設定。若重啟後仍失敗，應回到 `status`、`journalctl` 與設定檔檢查。
