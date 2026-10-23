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

