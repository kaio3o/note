## Views

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
 ### 資料維護(CREATE、UPDATE)
 > **保證資料安全**
 
 - 不可以包含計算或函式
	 - 聚合函數 (`SUM`, `COUNT`, `AVG`...)
	- `DISTINCT`
	- `GROUP BY`
	- `HAVING`
	- `UNION`
	- 某些複雜的 `JOIN`
 - ALGORITHM不可以為TEMPTABLE(暫存表)

```SQL
-- 建立名稱為EmpDept30View 的View 表，查詢emp 表內符合depno = 30 的資料
CREATE VIEW cmdev.EmpDept30View AS
SELECT empno, ename, job, manager, hiredate, salary, comm
FROM cmdev.emp
WHERE deptno = 30;

UPDATE EmpDept30View
SET comm = 600
WHERE empno = 7844;
-- 也可以使用INSERT
INSERT INTO EmpDept30View
VALUES (9001, 'SIMON', 'SALESMAN', 7698, '2000-04-01', 1000, 250)
```
#### WITH CHECK OPTION
> View 中有WHERE 條件，限定要符合條件才執行
#####  CASCADED | LOCAL
如果View 中使用其他View
- CASCADED 是確認所有View 的WHERE
- LOCAL 只確認目前View 中的WHERE

```SQL

CREATE VIEW cmdev.EmpDept30View AS
SELECT empno, ename, job, manager, hiredate, salary, comm, deptno
FROM cmdev.emp
WHERE deptno = 30
WITH [CASCADED | LOCAL] CHECK OPTION;

INSERT INTO EmpDept30View
VALUES (9001, 'SIMON', 'SALESMAN', 7698, '2000-04-01', 1000, 250, 40);
-- 因為不符合deptno = 30 所以會報錯
```
