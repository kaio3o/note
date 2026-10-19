// 產生網站首頁（index.md）：最近編輯條目、分類分頁、隨機漫遊與統計。
// 只列出會公開的筆記：套用 quartz.config.yaml 的 ignorePatterns，並略過 draft: true。
// 用法（在 Quartz 根目錄執行）：node build-home.mjs <筆記資料夾> <quartz.config.yaml> <home.md> <輸出 index.md>
import fs from "fs"
import path from "path"
import { execFileSync } from "child_process"
import { globby } from "globby"
import YAML from "yaml"

const [notesDir, configPath, homePath, outPath] = process.argv.slice(2)

const config = YAML.parse(fs.readFileSync(configPath, "utf8"))
const ignore = config.configuration.ignorePatterns ?? []
const home = parseFrontmatter(fs.readFileSync(homePath, "utf8")).data

function parseFrontmatter(raw) {
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/)
  if (!m) return { data: {}, body: raw }
  let data = {}
  try {
    data = YAML.parse(m[1]) ?? {}
  } catch {}
  return { data, body: raw.slice(m[0].length) }
}

// 與 Quartz 相同的網址規則（空白變 -，去掉 ? #，& 變 -and-，% 變 -percent）
function slugify(fp) {
  return fp
    .replace(/\.md$/, "")
    .split("/")
    .map((seg) =>
      seg
        .replace(/\s/g, "-")
        .replace(/&/g, "-and-")
        .replace(/%/g, "-percent")
        .replace(/\?/g, "")
        .replace(/#/g, ""),
    )
    .join("/")
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
}

// 取第一段像內文的文字當摘要
function summarize(body) {
  for (const line of body.split(/\r?\n/)) {
    const t = line.trim()
    if (!t || /^(#|```|---|\||>|!\[|<)/.test(t)) continue
    const plain = t
      .replace(/!?\[\[([^\]|]*)\|?([^\]]*)\]\]/g, (_, a, b) => b || a)
      .replace(/!?\[([^\]]*)\]\([^)]*\)/g, "$1")
      .replace(/[*_`~=]/g, "")
      .replace(/^[-+*]\s+|^\d+\.\s+/, "")
      .trim()
    if (plain.length >= 4) return plain.length > 60 ? plain.slice(0, 60) + "…" : plain
  }
  return ""
}

function gitDate(file) {
  try {
    const out = execFileSync("git", ["log", "-1", "--format=%cs", "--", file], {
      cwd: notesDir,
      encoding: "utf8",
    }).trim()
    if (out) return out
  } catch {}
  return fs.statSync(path.join(notesDir, file)).mtime.toISOString().slice(0, 10)
}

const files = await globby("**/*.md", { cwd: notesDir, ignore, gitignore: true })
const notes = []
let linkCount = 0
for (const file of files) {
  if (file === "index.md") continue
  const { data, body } = parseFrontmatter(fs.readFileSync(path.join(notesDir, file), "utf8"))
  if (data.draft === true || data.draft === "true") continue
  const links = body.match(/\[\[[^\]]+\]\]/g) ?? []
  linkCount += links.length
  const top = file.includes("/") ? file.split("/")[0] : null
  notes.push({
    slug: slugify(file),
    title: data.title ?? path.basename(file, ".md"),
    desc: data.description ?? summarize(body),
    date: data.modified ?? data.updated ?? gitDate(file),
    category: top ?? home.rootCategory ?? "其他筆記",
  })
}
notes.sort((a, b) => String(b.date).localeCompare(String(a.date)) || a.title.localeCompare(b.title))

// 資料夾分類依名稱排序，根目錄筆記的分類放最後
const rootCat = home.rootCategory ?? "其他筆記"
const categories = [...new Set(notes.map((n) => n.category))].sort(
  (a, b) => (a === rootCat) - (b === rootCat) || a.localeCompare(b, "zh-Hant"),
)
const catId = (c) => "c" + categories.indexOf(c)
const showTabs = categories.length > 1
const limit = home.limit ?? 30
const latest = notes[0]?.date ?? ""

const lines = []
lines.push("---")
lines.push(`title: ${JSON.stringify(home.title ?? "索引目錄")}`)
// 首頁連到每篇筆記；設成 unlisted，避免它出現在每篇筆記的反向連結與關係圖中
lines.push("unlisted: true")
// 分享時顯示的說明文字（首頁的筆記屬性面板已在設定中隱藏）
lines.push(`description: ${JSON.stringify(home.subtitle ?? "")}`)
lines.push("---")
lines.push("")
// HTML 區塊之間不留空行、不縮排，避免被 Markdown 當成段落或程式碼
const html = []
html.push(`<div class="home-index">`)
html.push(`<header class="home-head">`)
html.push(`<p class="home-crumb">Garden <span>/</span> <b>index</b></p>`)
html.push(`<h1 class="home-title">${escapeHtml(home.title ?? "索引目錄")}</h1>`)
html.push(
  `<p class="home-sub">${escapeHtml(home.subtitle ?? "")} · 涵蓋 ${notes.length} 篇條目與 ${linkCount} 條雙向連結</p>`,
)
html.push(`</header>`)
if (showTabs) {
  html.push(`<div class="home-tabs" role="tablist">`)
  html.push(`<input type="radio" name="home-tab" id="home-tab-all" checked />`)
  html.push(`<label for="home-tab-all">全部條目 <small>(${notes.length})</small></label>`)
  for (const c of categories) {
    const count = notes.filter((n) => n.category === c).length
    html.push(`<input type="radio" name="home-tab" id="home-tab-${catId(c)}" />`)
    html.push(`<label for="home-tab-${catId(c)}">${escapeHtml(c)} <small>(${count})</small></label>`)
  }
  html.push(`</div>`)
  // 選到某分類時只顯示該分類，且不受「全部條目」的筆數上限限制
  const rules = categories
    .map((c) => {
      const id = catId(c)
      return (
        `.home-index:has(#home-tab-${id}:checked) .home-entry:not([data-cat="${id}"]){display:none}` +
        `.home-index:has(#home-tab-${id}:checked) .home-entry.is-extra[data-cat="${id}"]{display:grid}`
      )
    })
    .join("")
  html.push(`<style>${rules}</style>`)
}
html.push(`<section class="home-log">`)
html.push(`<div class="home-section-head"><h2>最近編輯條目</h2><span>LOG</span></div>`)
html.push(`<ol class="home-entries">`)
notes.forEach((n, i) => {
  const extra = i >= limit ? " is-extra" : ""
  html.push(
    `<li class="home-entry${extra}" data-cat="${catId(n.category)}"><a href="./${encodeURI(n.slug)}" class="home-entry-title">${escapeHtml(n.title)}</a><time datetime="${escapeHtml(n.date)}">${escapeHtml(n.date)}</time>${n.desc ? `<p class="home-entry-desc">${escapeHtml(n.desc)}</p>` : ""}</li>`,
  )
})
if (notes.length === 0) html.push(`<li class="home-empty">目前沒有公開的筆記。</li>`)
html.push(`</ol>`)
html.push(`</section>`)
const slugs = escapeHtml(JSON.stringify(notes.map((n) => "./" + encodeURI(n.slug))))
html.push(`<footer class="home-foot">`)
html.push(
  `<button type="button" class="home-random" data-slugs="${slugs}" onclick="var s=JSON.parse(this.dataset.slugs);if(s.length)location.href=s[Math.floor(Math.random()*s.length)]">隨機漫遊一篇筆記 <span>(Random Note)</span></button>`,
)
html.push(`<a class="home-rss" href="./index.xml">RSS 訂閱</a>`)
html.push(
  `<span class="home-stats">${notes.length} 篇筆記 · ${linkCount} 條雙向連結${latest ? ` · 最後更新 ${escapeHtml(latest)}` : ""}</span>`,
)
html.push(`</footer>`)
html.push(`</div>`)

fs.writeFileSync(outPath, lines.join("\n") + html.join("\n") + "\n")
console.log(`首頁已產生：${notes.length} 篇筆記、${categories.length} 個分類、${linkCount} 條連結`)
