// 把 Obsidian「網站公開管理」外掛的隱藏清單併入 Quartz 的 ignorePatterns。
// 用法（在 Quartz 根目錄執行）：node apply-hidden.mjs <外掛 data.json> <quartz.config.yaml>
import fs from "fs"
import YAML from "yaml"

const [dataPath, configPath] = process.argv.slice(2)
const hidden = fs.existsSync(dataPath)
  ? (JSON.parse(fs.readFileSync(dataPath, "utf8")).hidden ?? [])
  : []

const doc = YAML.parseDocument(fs.readFileSync(configPath, "utf8"))
const patterns = doc.getIn(["configuration", "ignorePatterns"])
for (const raw of hidden) {
  // 跳脫 glob 特殊字元，避免檔名中的括號等被當成規則；同一路徑同時當成檔案與資料夾處理
  const p = raw.replace(/[()[\]{}*?!+@]/g, "\\$&")
  patterns.add(p)
  patterns.add(`${p}/**`)
}
fs.writeFileSync(configPath, doc.toString())
console.log(`已排除 ${hidden.length} 個不公開項目${hidden.length ? "：\n  " + hidden.join("\n  ") : ""}`)
