# 搜尋與動態規劃 DP

## 學習目標

理解「搜尋狀態空間」與「記錄重複子問題」的差別，能從暴力搜尋推導出 Memoization 或 Bottom-up DP。

---

## 需要知道的觀念

### 1. 搜尋 Search

- **DFS**：一路走到底再回頭，適合枚舉、回溯、樹與圖遍歷。
- **BFS**：一層一層擴展，常用於最少步數、無權圖最短路。
- **Backtracking**：嘗試 → 遞迴 → 撤銷，常見於排列組合與棋盤題。
- **State Space**：把每個狀態視為節點，把操作視為邊。
- **Pruning 剪枝**：提早排除不可能答案，避免無效搜尋。

### 2. Dynamic Programming

DP 適合具備以下特徵的問題：

- **Overlapping Subproblems**：子問題會重複出現。
- **Optimal Substructure**：大問題答案可由小問題答案組成。

DP 三要素：

1. **狀態定義**：`dp[i]` 或 `dp[i][j]` 代表什麼？
2. **轉移方程**：目前狀態從哪些狀態轉移而來？
3. **初始條件**：最小問題的答案是什麼？

### 3. Top-down vs Bottom-up

- **Top-down**：遞迴 + Memoization，較接近暴力搜尋。
- **Bottom-up**：由小到大填表，通常較好控制空間與順序。

### 4. 常見 DP 類型

- 一維 DP：爬樓梯、House Robber。
- 二維 DP：Grid、LCS、Edit Distance。
- 背包 DP：0/1 背包、完全背包、Subset Sum。
- 區間 DP：合併石頭、矩陣鏈乘法。
- 樹 DP：樹上最大獨立集、樹上路徑。
- Bitmask DP：狀態集合、TSP 類型。
- Digit DP：數位限制計數問題。

---

## 練習方向

### 搜尋練習

- 從排列、組合、子集合開始。
- 練習畫出遞迴樹。
- 練習設計 visited，避免重複走。
- 練習何時用 DFS、何時用 BFS。

### DP 練習

每題照這個順序想：

1. 暴力遞迴怎麼寫？
2. 哪些參數決定一個子問題？
3. 這些參數就是 DP 狀態嗎？
4. 子問題是否重複？
5. 是否能加 memo？
6. 是否能改成 bottom-up？
7. 是否能壓縮空間？

---

## 常見題型

### 搜尋

- Subsets
- Permutations
- Combination Sum
- N-Queens
- Word Search
- Maze Search

### DP

- Climbing Stairs
- House Robber
- Maximum Subarray
- Coin Change
- 0/1 Knapsack
- Longest Increasing Subsequence
- Longest Common Subsequence
- Edit Distance
- Unique Paths
- Minimum Path Sum
- Palindrome Partitioning

---

## 建議練習順序

1. Recursion 基礎
2. Backtracking：子集合、排列、組合
3. BFS 最短步數
4. Top-down Memoization
5. 一維 DP
6. 二維 Grid DP
7. Knapsack
8. LIS / LCS
9. 區間 DP
10. Tree DP / Bitmask DP

---

## 推薦資源

- LeetCode DP 題單
- NeetCode DP Roadmap
- VisuAlgo Recursion / DP 視覺化
- GeeksforGeeks Dynamic Programming
