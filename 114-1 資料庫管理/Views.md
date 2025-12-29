> **將經常需要執行的查詢寫成一個views**
---
### 基本規則
- 同一資料庫中名稱不能重複，也不能與Table 名稱相同
- 不能使用於Triggers
- 只能使用已存在的Table 或View
- 查詢語句中的From 不能使用子查詢
- 不能使用TEMPORARY 表格
- 不能使用變數
---
### 建立Views 元件
```SQL
CREATE [OR REPLACE] VIEW *View名稱 AS *查詢語句
```
---
### 查詢View 資訊
```SQL
DESC *View名稱
```
---
### 修改與刪除View 元件
```SQL
ALTER VIEW *View名稱 AS *查詢語句
-- 沒有這個View 會建立新的
CREATE OR REPLACE VIEW *View名稱 AS *查詢語句
```


```SQL
-- IF EXISTS 如果沒有這個View 不會報錯
DROP VIEW [IF EXISTS] *View名稱
```
---
