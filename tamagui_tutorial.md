# Tamagui 教學：屬性與規範

本文件旨在提供 Tamagui 的基本介紹，並詳細說明其樣式屬性 (Style Props) 的使用方式與核心規範。

## 1. 什麼是 Tamagui？

Tamagui 是一個全端、跨平台的 UI 工具組，專為 React Native 和 Web 設計。它不僅提供了一套豐富的 UI 組件，更透過其獨特的編譯器優化，實現了前所未有的性能。

其核心亮點包括：

*   **跨平台一致性**：一套程式碼，同時在 Web 和原生應用 (iOS/Android) 上運行，並保持外觀與行為的一致性。
*   **高性能**：透過靜態編譯器 (`@tamagui/static`)，在建置階段就將樣式和邏輯進行優化，大幅減少客戶端的運算負擔，達到近乎「零執行成本」的性能。
*   **樣式超集**：支援完整的 React Native 樣式，並擴展了大量 CSS 功能，如媒體查詢、偽類、主題等。
*   **豐富的組件庫**：提供 `tamagui` (有樣式組件) 和 `@tamagui/core` (無樣式基礎) 兩種選擇，靈活性高。

---

## 2. 核心屬性與規範 (Style Props)

Tamagui 的強大之處在於其靈活且直觀的樣式屬性系統。它允許你用類似 CSS 的語法快速為組件添加樣式。

### 2.1 基礎樣式

你可以直接在 Tamagui 組件上使用類似 CSS 的屬性，它們是 React Native 樣式的超集。

```jsx
import { View, Text } from 'tamagui'

export const MyComponent = () => (
  <View 
    padding="$4" 
    backgroundColor="$background"
    borderRadius={10}
    elevation="$2"
  >
    <Text color="$color" fontSize={16}>Hello Tamagui</Text>
  </View>
)
```

*   **設計代幣 (Design Tokens)**：以 `$` 符號開頭的屬性值 (如 `$4`, `$background`) 是指在主題中預先定義的設計代幣。這有助於保持設計系統的一致性。
*   **常規值**：你也可以使用常規的數字 (for `px`) 或字串值。

### 2.2 偽狀態 (Pseudo States)

Tamagui 支援多種偽狀態，用於處理用戶互動時的樣式變化，這在 Web 和原生應用中都非常有用。

*   `hoverStyle`: 滑鼠懸停時的樣式 (僅限 Web)。
*   `pressStyle`: 元件被按下時的樣式。
*   `focusStyle`: 元件獲得焦點時的樣式。
*   `focusVisibleStyle`: 使用鍵盤導航獲得焦點時的樣式。

```jsx
<View 
  backgroundColor="$blue10"
  hoverStyle={{ backgroundColor: '$blue11' }}
  pressStyle={{ backgroundColor: '$blue12' }}
/>
```

### 2.3 響應式設計 (Responsive Design)

Tamagui 的媒體查詢功能使其能輕鬆實現響應式佈局。預設情況下，你可以使用 `$sm`, `$md`, `$lg`, `$xl` 等前綴來指定在不同螢幕尺寸下應用的樣式。

```jsx
<View 
  width="100%"
  $gtSm={{ width: "50%" }}
  $gtLg={{ width: "25%" }}
/>
```
*   `$gtSm`: "大於 small" 尺寸時生效。
*   `$ltMd`: "小於 medium" 尺寸時生效。

### 2.4 平台與主題特定樣式

你可以根據不同的平台 (Web, iOS, Android) 或主題 (Light, Dark) 來應用不同的樣式。

*   `$platform-ios`: 僅在 iOS 上生效。
*   `$platform-android`: 僅在 Android 上生效。
*   `$platform-web`: 僅在 Web 上生效。
*   `$theme-light`: 在 `light` 主題下生效。
*   `$theme-dark`: 在 `dark` 主題下生效。

```jsx
<View 
  padding="$4"
  $platform-ios={{ paddingVertical: "$6" }}
  $theme-dark={{ backgroundColor: "#333" }}
/>
```

### 2.5 其他重要屬性

*   `asChild`: 當設定為 `true` 時，該組件不會渲染自己的 DOM 元素，而是將其屬性（包括樣式和事件）傳遞給其唯一的子元素。這對於組合組件和保持語意化的 HTML 結構非常有用。

    ```jsx
    <Button asChild>
      <a href="/home">Go Home</a>
    </Button>
    ```

*   `tag`: (僅限 Web) 強制將組件渲染為指定的 HTML 標籤。

    ```jsx
    <Text tag="h1" fontSize={32}>
      This is a title
    </Text>
    ```

---

## 3. 總結

Tamagui 透過其強大的編譯器和富有表現力的樣式屬性系統，為 React 開發者提供了一個高效、一致且愉快的跨平台 UI 開發體驗。掌握其 Style Props 的使用方式是發揮 Tamagui 全部潛力的關鍵。建議深入閱讀官方文件，探索更多高級功能如 `styled()`, `createTamagui()` 等。
