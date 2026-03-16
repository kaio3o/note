# Git 常用指令統整與解釋

Git 是一個強大的版本控制系統，以下整理了日常開發中常用的 Git 指令及其解釋。

## 1. 設定 (Configuration)

### `git config`
設定 Git 的使用者名稱和電子郵件，這些資訊會記錄在你的提交中。

- **設定使用者名稱：**
  ```bash
  git config --global user.name "你的名字"
  ```
- **設定使用者電子郵件：**
  ```bash
  git config --global user.email "你的電子郵件"
  ```
- **查看所有設定：**
  ```bash
  git config --list
  ```

## 2. 取得專案 (Getting a Project)

### `git init`
在當前目錄初始化一個新的 Git 儲存庫。

```bash
git init
```

### `git clone`
複製一個遠端儲存庫到本地。

```bash
git clone <遠端儲存庫URL> [本地目錄名稱]
# 範例：
git clone https://github.com/user/repo.git my_project
```

## 3. 儲存變更 (Saving Changes)

### `git status`
查看工作目錄和暫存區的狀態，顯示哪些檔案已修改、已暫存或未被追蹤。

```bash
git status
```

### `git add`
將檔案從工作目錄添加到暫存區，準備提交。

- **添加單個檔案：**
  ```bash
  git add <檔案名稱>
  # 範例：
  git add index.html
  ```
- **添加所有修改過的檔案：**
  ```bash
  git add .
  ```

### `git commit`
將暫存區的變更提交到本地儲存庫。

- **提交並附帶訊息：**
  ```bash
  git commit -m "你的提交訊息"
  # 範例：
  git commit -m "新增首頁內容"
  ```
- **提交並自動打開編輯器輸入訊息：**
  ```bash
  git commit
  ```
- **修改上次提交：**
  ```bash
  git commit --amend
  ```

## 4. 查看歷史 (Viewing History)

### `git log`
查看提交歷史。

- **查看所有提交：**
  ```bash
  git log
  ```
- **查看簡潔的提交歷史：**
  ```bash
  git log --oneline
  ```
- **查看圖形化的提交歷史：**
  ```bash
  git log --graph --oneline --all
  ```

### `git diff`
比較檔案的差異。

- **比較工作目錄和暫存區的差異：**
  ```bash
  git diff
  ```
- **比較暫存區和上次提交的差異：**
  ```bash
  git diff --staged
  ```
- **比較兩個提交之間的差異：**
  ```bash
  git diff <commit1> <commit2>
  ```

## 5. 分支管理 (Branching)

### `git branch`
管理分支。

- **列出所有分支：**
  ```bash
  git branch
  ```
- **建立新分支：**
  ```bash
  git branch <新分支名稱>
  # 範例：
  git branch feature/new-feature
  ```
- **刪除分支：**
  ```bash
  git branch -d <分支名稱> # 只能刪除已合併的分支
  git branch -D <分支名稱> # 強制刪除分支
  ```

### `git checkout`
切換分支或恢復檔案。

- **切換到指定分支：**
  ```bash
  git checkout <分支名稱>
  # 範例：
  git checkout develop
  ```
- **建立並切換到新分支：**
  ```bash
  git checkout -b <新分支名稱>
  ```
- **恢復檔案到上次提交的狀態：**
  ```bash
  git checkout -- <檔案名稱>
  ```

### `git merge`
將一個分支的變更合併到當前分支。

```bash
git merge <要合併的分支名稱>
# 範例：
git merge feature/new-feature
```

### `git rebase`
將一個分支的提交應用到另一個分支的頂部，以保持提交歷史的線性。

```bash
git rebase <目標分支名稱>
# 範例：
git rebase main
```

## 6. 遠端操作 (Remote Operations)

### `git remote`
管理遠端儲存庫。

- **列出所有遠端儲存庫：**
  ```bash
  git remote -v
  ```
- **添加遠端儲存庫：**
  ```bash
  git remote add <名稱> <URL>
  # 範例：
  git remote add origin https://github.com/user/repo.git
  ```

### `git fetch`
從遠端儲存庫下載最新的變更，但不會自動合併到本地分支。

```bash
git fetch <遠端名稱>
# 範例：
git fetch origin
```

### `git pull`
從遠端儲存庫下載最新的變更並自動合併到當前分支。

```bash
git pull <遠端名稱> <分支名稱>
# 範例：
git pull origin main
```

### `git push`
將本地提交推送到遠端儲存庫。

```bash
git push <遠端名稱> <分支名稱>
# 範例：
git push origin main
```
- **設定上游分支並推送：**
  ```bash
  git push -u origin <分支名稱>
  ```

## 7. 撤銷操作 (Undoing Changes)

### `git reset`
重置 HEAD 到指定狀態，可以撤銷提交或取消暫存。

- **取消暫存區的檔案：**
  ```bash
  git reset HEAD <檔案名稱>
  ```
- **撤銷上次提交 (保留工作目錄變更)：**
  ```bash
  git reset HEAD~1
  ```
- **撤銷上次提交 (丟棄工作目錄變更)：**
  ```bash
  git reset --hard HEAD~1
  ```

### `git revert`
建立一個新的提交來撤銷之前的提交，保留歷史記錄。

```bash
git revert <提交ID>
```

### `git restore` (Git 2.23+ 推薦)
恢復工作目錄或暫存區的檔案。

- **恢復工作目錄中的檔案到上次提交的狀態：**
  ```bash
  git restore <檔案名稱>
  ```
- **將檔案從暫存區恢復到工作目錄 (取消暫存)：**
  ```bash
  git restore --staged <檔案名稱>
  ```

## 8. 儲藏 (Stashing)

### `git stash`
暫時儲存工作目錄中未提交的變更，以便切換到其他任務。

- **儲藏變更：**
  ```bash
  git stash save "你的儲藏訊息"
  ```
- **查看儲藏列表：**
  ```bash
  git stash list
  ```
- **應用最近的儲藏並保留在列表中：**
  ```bash
  git stash apply
  ```
- **應用最近的儲藏並從列表中刪除：**
  ```bash
  git stash pop
  ```
- **刪除所有儲藏：**
  ```bash
  git stash clear
  ```

## 9. 標籤 (Tagging)

### `git tag`
為特定的提交打上標籤，通常用於標記發布版本。

- **列出所有標籤：**
  ```bash
  git tag
  ```
- **建立輕量標籤：**
  ```bash
  git tag <標籤名稱>
  # 範例：
  git tag v1.0.0
  ```
- **建立附註標籤 (推薦，包含更多資訊)：**
  ```bash
  git tag -a <標籤名稱> -m "標籤訊息"
  # 範例：
  git tag -a v1.0.0 -m "Release version 1.0.0"
  ```
- **將標籤推送到遠端：**
  ```bash
  git push origin <標籤名稱>
  git push origin --tags # 推送所有標籤
  ```
- **刪除本地標籤：**
  ```bash
  git tag -d <標籤名稱>
  ```
- **刪除遠端標籤：**
  ```bash
  git push origin --delete <標籤名稱>
  ```
