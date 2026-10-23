---
tags: [Linux, RPM, dnf, 套件管理]
---
# RPM 與 dnf 套件管理

- RPM 是套件格式與底層管理工具。
- `dnf` 會處理 repository、相依套件、更新與移除，日常管理通常優先使用 `dnf`。

```bash
rpm -qa
rpm -q package
rpm -qi package
rpm -ql package
rpm -ivh package.rpm

dnf repolist
dnf search keyword
dnf info package
dnf install package
dnf update
dnf remove package
dnf history
```

安裝或更新前先確認來源、版本、相依性、服務影響與回復方式。

- [原始章節](https://hackmd.io/@ntub-class/B12EXeiufx/%2FE4bWmADQTxqRbUb2orKniw)

## 從零開始理解

套件不是單一執行檔，通常還包含設定檔、函式庫、服務檔與文件。套件管理器可以記錄版本、檔案歸屬與相依性，避免手動複製檔案造成系統不一致。

### RPM 與 dnf 的角色

- RPM：處理單一 `.rpm` 套件，適合查詢「這個檔案屬於哪個套件」。
- dnf：連線到 repository，搜尋、下載並解決相依套件，日常安裝更新優先使用它。

### 初學者的安全流程

```bash
dnf search nginx
dnf info nginx
sudo dnf install nginx
rpm -q nginx
systemctl status nginx
```

每一步的問題是：

1. 有沒有這個套件？
2. 它是哪個版本、從哪裡來？
3. 安裝會帶入哪些相依套件？
4. 安裝後套件是否真的存在？
5. 服務是否啟動、是否需要另外設定？

### 查詢檔案由哪個套件提供

已安裝檔案：

```bash
rpm -qf /usr/bin/某個命令
rpm -ql 套件名稱
```

尚未安裝但想查來源：

```bash
dnf provides '*/命令名稱'
```

### 更新與移除

```bash
sudo dnf check-update
sudo dnf update
dnf history
dnf history info <ID>
```

移除前先看 dnf 提出的清單；有些套件可能是其他服務的相依項。正式環境應先確認維護窗口、備份與回復方式。

> [!warning] 不要混淆套件與服務
> 安裝套件不一定會啟動服務；服務也可能需要設定檔、防火牆與 SELinux 設定才能正常提供功能。
