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

