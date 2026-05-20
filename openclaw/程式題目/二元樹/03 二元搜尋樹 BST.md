---
tags:
  - 二元樹
  - BST
  - BinarySearchTree
  - Medium
---

# 03 二元搜尋樹 BST

BST（Binary Search Tree，二元搜尋樹）的特性：

- 左子樹所有值 `< root.val`
- 右子樹所有值 `> root.val`
- 每個子樹也都必須符合 BST

## 必練題目

### 1. Search in a Binary Search Tree（搜尋 BST）
> 說明：利用 BST 左小右大的特性，從根節點一路往左或往右縮小搜尋範圍。

- 難度：Easy
- 核心：利用 BST 大小關係往左或往右找

```python
def search_bst(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)
```

---

### 2. Insert into a Binary Search Tree（插入 BST）
> 說明：依照 BST 規則找到新值應該放入的空位，並接上新的節點。

- 難度：Medium
- 核心：找到空位後插入新節點

```python
def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root
```

---

### 3. Validate Binary Search Tree（驗證 BST）
> 說明：確認每個節點都符合整個祖先範圍限制，而不只是比直接左右孩子大或小。

- 難度：Medium
- 核心：不能只比較左右 child，要限制整個子樹範圍

```python
def is_valid_bst(root):
    def dfs(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float('-inf'), float('inf'))
```

---

### 4. Kth Smallest Element in a BST（BST 第 K 小元素）
> 說明：利用 BST 中序遍歷會遞增的特性，找到排序後第 K 個最小值。

- 難度：Medium
- 核心：BST 中序遍歷是遞增序列

```python
def kth_smallest(root, k):
    stack = []
    cur = root

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
```

---

### 5. Lowest Common Ancestor of a BST（BST 最近共同祖先）
> 說明：在 BST 中找到同時位於兩個節點路徑上的最低節點，也就是它們最近的共同祖先。

- 難度：Medium
- 核心：如果 p、q 都比 root 小，往左；都比 root 大，往右；否則 root 就是答案

```python
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

---

### 6. Delete Node in a BST（刪除 BST 節點）
> 說明：刪除指定節點後仍要維持 BST 性質，需分別處理無子節點、一個子節點與兩個子節點。

- 難度：Medium
- 核心：刪除節點有三種情況：無子節點、一個子節點、兩個子節點

```python
def delete_node(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        successor = root.right
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)

    return root
```

## 小結

BST 題目的兩大武器：

1. **中序遍歷會得到排序結果**。
2. **每個節點都有上下界限制**。
