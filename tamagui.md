# Tamagui 2.0.0-rc.26 進階使用手冊與限制規範

本文件詳細介紹 Tamagui 的核心功能使用模式、最佳實踐以及在不同平台（Web/Native）下的技術限制。

---

## 1. 設計代幣系統 (Design Tokens)

### 使用方法
在 `createTamagui` 中定義 `size`, `space`, `color`, `radius`, `zIndex` 等。
```tsx
const config = createTamagui({
  tokens: createTokens({
    size: { sm: 10, md: 20, true: 15 }, // true 是預設值
    color: { primary: '#000' },
    space: { 1: 4, 2: 8 },
  })
})
```
*   **調用方式**：`<Stack padding="$2" />`

### 限制與注意
*   **必須前綴 `$`**：在屬性中調用 token 必須加 `$`，否則會被視為原始數值（如 `padding={2}` 代表 2px）。
*   **Token 類型固定**：某些屬性僅能接收特定類型的 Token（例如 `backgroundColor` 只能接 `color` token）。
*   **Runtime 限制**：若不使用編譯器，過多的 Token 映射會在運行時產生輕微的效能開銷。

---

## 2. 響應式設計 (Media Queries)

### 使用方法
透過 `$gt` (greater than) 或 `$lt` (less than) 前綴來應用樣式。
```tsx
<XStack 
  flexDirection="column" 
  $gtMd={{ flexDirection: 'row', padding: '$4' }} 
/>
```

### 限制與注意
*   **Web 優先級**：在 Web 端，Tamagui 使用 CSS Media Queries，這非常高效。
*   **Native 限制**：在 React Native 上，響應式是透過 JS 監聽螢幕尺寸變化實現的。這可能導致**螢幕旋轉時有輕微的樣式延遲**。
*   **編譯器依賴**：強烈建議在 Web 端搭配 `@tamagui/static`，否則所有響應式樣式都會變成 Inline Styles，失去 CSS 的效能優勢。

---

## 3. 主題巢狀 (Theme Nesting)

### 使用方法
你可以局部覆蓋主題，這對於「深色卡片內有淺色按鈕」的場景非常有用。
```tsx
<Theme name="dark">
  <YStack bc="$background">
    <Theme name="light">
      <Button /> {/* 此按鈕將使用 light 主題 */}
    </Theme>
  </YStack>
</Theme>
```

### 限制與注意
*   **效能開銷**：過深的主題巢狀（例如超過 5 層）會增加 Context 查找的負擔，可能導致渲染效能下降。
*   **SSR 水合 (Hydration)**：在 2.0.0-rc.26 之前，複雜的主題巢狀常導致 Web 端初次渲染與伺服器端不一致。**rc.26 雖已優化，但仍建議避免在 `Theme` 組件上動態頻繁切換 `name`。**

---

## 4. `styled()` 組件與變體 (Variants)

### 使用方法
這是擴展組件邏輯的核心工具。
```tsx
const BoldText = styled(Text, {
  color: '$color',
  variants: {
    size: {
      huge: { fontSize: 40, lineHeight: 50 }
    }
  } as const
})
```

### 限制與注意
*   **類型安全**：必須加上 `as const`，否則 TypeScript 可能無法正確推斷 Variant 的名稱。
*   **無法動態生成 Variant**：Variant 的鍵值必須是靜態定義的，你不能根據運行時的 API 數據動態產生新的 Variant 類別。
*   **組合限制**：當一個組件同時有多個 Variant 影響同一個 CSS 屬性時，**最後定義的 Variant 優先級最高**，而非傳入 Props 的順序。

---

## 5. 跨平台樣式一致性 (Cross-Platform)

### 限制與陷阱
*   **Shadows (陰影)**：
    *   Native：主要依賴 `elevation` (Android) 或 `shadowOffset` (iOS)。
    *   Web：轉換為 `box-shadow`。
    *   **限制**：複雜的 CSS 內陰影 (inset shadow) 在 Native 端完全不支援。
*   **Filter/Blur**：
    *   Web：完整支援 `backdrop-filter`。
    *   Native：需要額外安裝 `expo-blur` 或相關庫，Tamagui 預設不處理 Native 端的毛玻璃效果。
*   **佈局差異**：`Text` 組件在 Web 預設是 `display: inline`，但在 Native 始終遵循 Flexbox。建議始終將 Text 放在 `Stack` 內以確保佈局一致。

---

## 6. 編譯器與性能 (The Compiler)

### 限制
*   **動態求值限制**：編譯器只能優化「靜態可分析」的代碼。如果你寫 `<View padding={Math.random()} />`，編譯器會放棄優化該屬性並退回到 Runtime 模式。
*   **Spread Operator**：`<View {...props} />` 會大幅降低編譯器的優化能力，因為它無法預知 `props` 內含有哪些樣式。

---

## 7. 2.0.0-rc.26 專屬升級提醒
*   **Lucide Icons**：此版本優化了圖標權重。若你發現圖標渲染異常，請確保 `@tamagui/lucide-icons` 同步更新至最新。
*   **Z-Index**：rc.26 修復了某些堆疊上下文問題。若你的 `Popover` 或 `Dialog` 層級出錯，請檢查是否在 `TamaguiProvider` 中正確啟用了 `PortalProvider`。

---
*更新日期：2026-03-19*
