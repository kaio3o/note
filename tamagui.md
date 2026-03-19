# Tamagui 2.0.0-rc.26 使用說明與規範

本文件針對 Tamagui **2.0.0-rc.26** 版本提供核心指南，包含基礎配置、樣式屬性、組件規範及此版本的重大更新。

---

## 1. 2.0.0-rc.26 版本特性 (What's New)

此版本是邁向 2.0 正式版的關鍵里程碑，重點在於編譯器優化與打包體積縮減。

*   **編譯器增強：** 支援 `tsconfig paths` 自動探索，簡化了路徑別名的配置。
*   **SSR 水合 (Hydration) 修復：** 在 `TamaguiProvider` 中預置了 `PortalProvider`，解決了伺服器渲染時常見的 DOM 不匹配錯誤。
*   **體積優化：** 顯著減少了發佈包的 JS 權重，並優化了 Lucide Icons 的 Source Maps 處理。
*   **樣式特異性 (Specificity)：** 修復了深層巢狀 `$group` 樣式屬性無法正確覆蓋的問題。

---

## 2. 核心配置 (Configuration)

Tamagui 的強大源於 `tamagui.config.ts`。在此定義你的設計系統：

### 2.1 設計代幣 (Tokens)
所有以 `$` 開頭的屬性值都對應到 Token。
- **Size:** `$true`, `$1`, `$2`... (用於 width, height, padding, margin)
- **Color:** `$background`, `$color`, `$blue10`...
- **Radius:** `$2`, `$4`...
- **ZIndex:** `$1`, `$10`...

### 2.2 簡寫屬性 (Shorthands)
為了開發效率，建議在配置中啟用 Shorthands：
- `m`: `margin`
- `p`: `padding`
- `bc`: `backgroundColor`
- `ai`: `alignItems`
- `jc`: `justifyContent`
- `f`: `flex`

---

## 3. 核心組件與佈局 (Core Components)

### 3.1 佈局三大件
- **`YStack`**: 垂直堆疊 (Vertical Flex Column)。
- **`XStack`**: 水平堆疊 (Horizontal Flex Row)。
- **`ZStack`**: 層疊堆疊 (Absolute Positioning Overlay)。

### 3.2 文本組件
- **`Text`**: 基礎文本。
- **`Paragraph`**: 帶有預設行高與邊距的段落文本。
- **`Heading`**: 標題組件 (h1-h6)。

---

## 4. 樣式屬性規範 (Style Props)

### 4.1 互動偽類 (Pseudo Styles)
Tamagui 在原生平台與 Web 之間提供了一致的互動 API：
```tsx
<Button
  backgroundColor="$blue10"
  hoverStyle={{ backgroundColor: '$blue11', scale: 1.05 }}
  pressStyle={{ backgroundColor: '$blue12', scale: 0.95 }}
  focusStyle={{ outlineColor: '$blue8', outlineWidth: 2 }}
/>
```

### 4.2 響應式前綴 (Media Queries)
使用前綴快速實現跨螢幕適配：
- `$gtSm`: 大於 Small 尺寸。
- `$ltMd`: 小於 Medium 尺寸。
- `$gtLg`: 大於 Large 尺寸。

```tsx
<YStack width="100%" $gtMd={{ width: "50%", flexDirection: "row" }} />
```

### 4.3 平台與主題特定
- `$platform-ios` / `$platform-android` / `$platform-web`
- `$theme-light` / `$theme-dark`

---

## 5. 高階開發規範 (Advanced Patterns)

### 5.1 `styled()` 函數
建立可複用的樣式化組件，並定義自定義變體 (Variants)：
```tsx
import { styled, YStack } from 'tamagui'

export const MyCard = styled(YStack, {
  name: 'MyCard', // 用於編譯器調試
  backgroundColor: '$background',
  padding: '$4',
  borderRadius: '$4',

  variants: {
    isError: {
      true: {
        borderColor: '$red10',
        borderWidth: 2,
      }
    }
  } as const
})
```

### 5.2 `asChild` 模式
當需要將樣式傳遞給自定義子組件時使用（常用於整合 Next.js Link 或 React Router）：
```tsx
<Button asChild>
  <NextLink href="/dashboard">進入控制台</NextLink>
</Button>
```

---

## 6. 性能優化建議 (Performance Tips)

1.  **使用靜態編譯器：** 確保在生產環境啟動 `@tamagui/static`，這能將大部分樣式轉換為 CSS，減少 JS 執行負擔。
2.  **避免 inline objects：** 盡量使用 Token 或變體，避免在 render 中直接寫 `style={{ ... }}`，這會繞過編譯器優化。
3.  **Clean Cache：** 在升級到 `rc.26` 後，若遇到樣式不生效，請執行 `tamagui clean` 並重啟開發伺服器。

---

## 7. 參考連結
- [Tamagui 官方文件](https://tamagui.dev)
- [GitHub Release Notes](https://github.com/tamagui/tamagui/releases)
