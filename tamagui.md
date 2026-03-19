# Tamagui 2.0.0-rc.26 完整使用指南與規範

本文件整合了 Tamagui 的核心屬性使用方法、進階規範及 2.0.0-rc.26 的技術限制。

---

## 1. 2.0.0-rc.26 版本特性

*   **自動路徑探索**：編譯器現在能自動識別 `tsconfig.json` 的路徑別名。
*   **SSR 水合優化**：預置了 `PortalProvider`，大幅減少 Web 端 SSR 的水合不匹配錯誤。
*   **效能增強**：移除了 Lucide 圖標的多餘 Source Maps，打包體積更小。

---

## 2. 核心屬性使用方法 (Style Props)

### 2.1 基礎樣式屬性
Tamagui 是 React Native 樣式的超集，支援簡寫 (Shorthands)。
*   `p`, `px`, `py`: Padding。
*   `m`, `mx`, `my`: Margin。
*   `bc`: `backgroundColor`。
*   `zi`: `zIndex`。
*   **調用 Token**：`<View p="$4" bc="$background" />` (必須加 `$` 符號)。

### 2.2 偽狀態 (Pseudo States)
用於處理 Web 和 Native 的互動：
*   `hoverStyle`: 僅 Web 支援。
*   `pressStyle`: 按下時的縮放或變色。
*   `focusStyle`: 獲取焦點時的樣式。

### 2.3 特殊功能屬性
*   **`asChild`**: 將樣式傳遞給唯一的子組件（不渲染多餘 DOM）。常用於整合路由 Link。
    ```tsx
    <Button asChild>
      <Link href="/home">首頁</Link>
    </Button>
    ```
*   **`tag`**: (僅限 Web) 強制渲染為特定 HTML 標籤。
    ```tsx
    <Text tag="h1">標題</Text>
    ```

---

## 3. 進階功能與技術限制

### 3.1 設計代幣 (Tokens)
*   **用法**：在 `createTamagui` 中定義 `size`, `color`, `space` 等。
*   **限制**：Token 映射在運行時有輕微開銷，建議搭配編譯器。

### 3.2 響應式設計 (Media Queries)
*   **用法**：`$gtSm`, `$ltMd`, `$gtLg`。
*   **限制**：在 Native 端是透過 JS 監聽螢幕旋轉實現的，極端情況下可能有微小延遲。

### 3.3 主題巢狀 (Theme Nesting)
*   **用法**：`<Theme name="dark">...</Theme>`。
*   **限制**：過深的主題巢狀（>5層）會影響 Context 查找效能。

### 3.4 `styled()` 組件與變體 (Variants)
*   **用法**：
    ```tsx
    export const MyButton = styled(Button, {
      variants: {
        urgent: { true: { bc: '$red10' } }
      } as const
    })
    ```
*   **限制**：Variant 名稱必須是靜態的，且必須加 `as const` 以保證類型安全。

---

## 4. 跨平台一致性陷阱

1.  **陰影 (Shadows)**：Native 的 `elevation` 與 Web 的 `box-shadow` 在視覺上很難完全一致，建議使用 Tamagui 的 Shadow Tokens。
2.  **模糊 (Blur)**：Native 需安裝額外庫（如 `expo-blur`），Tamagui 不會自動轉換 `backdrop-filter`。
3.  **佈局差異**：`Text` 組件在 Web 是 `inline`，Native 是 `flex`。建議始終在外層包裹 `Stack` 以穩定佈局。

---

## 5. 性能優化建議

1.  **避免 Spread Props**：`<View {...props} />` 會讓編譯器無法預先優化。
2.  **靜態化**：盡量使用 Token 而非 inline 數值（如 `padding={10}`），這能讓編譯器將其轉換為靜態 CSS。
3.  **清理快取**：升級 rc.26 後若樣式錯誤，請執行 `tamagui clean`。

---
*更新日期：2026-03-19*
