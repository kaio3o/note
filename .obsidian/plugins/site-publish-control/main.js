// 網站公開管理：隱藏清單存在本外掛的 data.json，
// GitHub Actions 建置網站時會讀取它，把清單中的筆記與資料夾排除在網站之外。
const { Plugin, PluginSettingTab, Setting, Notice, TFolder } = require("obsidian")

const DEFAULT_DATA = { hidden: [] }

module.exports = class SitePublishControl extends Plugin {
  async onload() {
    this.data = Object.assign({}, DEFAULT_DATA, await this.loadData())
    this.styleEl = document.head.createEl("style", { attr: { id: "site-publish-control-dynamic" } })
    this.refreshStyles()

    this.registerEvent(
      this.app.workspace.on("file-menu", (menu, file) => this.addMenuItem(menu, [file])),
    )
    this.registerEvent(
      this.app.workspace.on("files-menu", (menu, files) => this.addMenuItem(menu, files)),
    )

    // 改名或搬移時同步更新清單，刪除時移除
    this.registerEvent(
      this.app.vault.on("rename", async (file, oldPath) => {
        let changed = false
        this.data.hidden = this.data.hidden.map((p) => {
          if (p === oldPath) {
            changed = true
            return file.path
          }
          if (p.startsWith(oldPath + "/")) {
            changed = true
            return file.path + p.slice(oldPath.length)
          }
          return p
        })
        if (changed) await this.persist()
      }),
    )
    this.registerEvent(
      this.app.vault.on("delete", async (file) => {
        const before = this.data.hidden.length
        this.data.hidden = this.data.hidden.filter(
          (p) => p !== file.path && !p.startsWith(file.path + "/"),
        )
        if (this.data.hidden.length !== before) await this.persist()
      }),
    )

    this.addCommand({
      id: "toggle-current-note",
      name: "切換目前筆記是否公開到網站",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile()
        if (!file) return false
        if (!checking) this.setHidden([file], !this.isDirectlyHidden(file.path))
        return true
      },
    })

    this.addSettingTab(new HiddenListTab(this.app, this))
  }

  onunload() {
    this.styleEl?.remove()
  }

  isDirectlyHidden(path) {
    return this.data.hidden.includes(path)
  }

  hiddenByParent(path) {
    return this.data.hidden.find((p) => path.startsWith(p + "/"))
  }

  addMenuItem(menu, files) {
    if (files.length === 0) return
    const allHidden = files.every((f) => this.isDirectlyHidden(f.path))
    const inherited = files.length === 1 && this.hiddenByParent(files[0].path)

    menu.addItem((item) => {
      if (inherited && !allHidden) {
        item
          .setTitle(`網站：已隨資料夾「${inherited}」隱藏`)
          .setIcon("eye-off")
          .setDisabled(true)
        return
      }
      item
        .setTitle(allHidden ? "在網站上公開" : "在網站上隱藏")
        .setIcon(allHidden ? "eye" : "eye-off")
        .onClick(() => this.setHidden(files, !allHidden))
    })
  }

  async setHidden(files, hide) {
    const paths = files.map((f) => f.path)
    if (hide) {
      for (const p of paths) if (!this.data.hidden.includes(p)) this.data.hidden.push(p)
    } else {
      this.data.hidden = this.data.hidden.filter((p) => !paths.includes(p))
    }
    await this.persist()
    const label = paths.length === 1 ? `「${files[0].name}」` : `${paths.length} 個項目`
    new Notice(hide ? `${label}已設為不公開` : `${label}已設為公開`)
  }

  async persist() {
    this.data.hidden.sort((a, b) => a.localeCompare(b))
    await this.saveData(this.data)
    this.refreshStyles()
    this.settingTab?.display()
  }

  // 在檔案總管把隱藏的項目淡化並加上標記
  refreshStyles() {
    const selectors = this.data.hidden.flatMap((p) => {
      const v = CSS.escape(p)
      return [
        `.nav-file-title[data-path="${v}"]`,
        `.nav-folder-title[data-path="${v}"]`,
        `.nav-file-title[data-path^="${v}/"]`,
        `.nav-folder-title[data-path^="${v}/"]`,
      ]
    })
    const own = this.data.hidden.flatMap((p) => {
      const v = CSS.escape(p)
      return [
        `.nav-file-title[data-path="${v}"] .nav-file-title-content::after`,
        `.nav-folder-title[data-path="${v}"] .nav-folder-title-content::after`,
      ]
    })
    this.styleEl.textContent =
      selectors.length === 0
        ? ""
        : `${selectors.join(",\n")} { opacity: 0.45; }\n` +
          `${own.join(",\n")} { content: "不公開"; margin-left: 6px; padding: 0 5px; font-size: 0.7em; border-radius: 4px; background: var(--background-modifier-border); color: var(--text-muted); vertical-align: middle; }`
  }
}

class HiddenListTab extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin)
    this.plugin = plugin
    plugin.settingTab = this
  }

  display() {
    const { containerEl } = this
    containerEl.empty()
    containerEl.createEl("p", {
      text: "以下筆記與資料夾不會發布到網站。在檔案總管按右鍵選「在網站上隱藏／公開」即可切換；推送到 GitHub 後網站會自動更新。",
    })

    const hidden = this.plugin.data.hidden
    if (hidden.length === 0) {
      containerEl.createEl("p", { text: "目前所有筆記都會公開。", cls: "setting-item-description" })
      return
    }
    for (const p of hidden) {
      const isFolder = this.app.vault.getAbstractFileByPath(p) instanceof TFolder
      new Setting(containerEl)
        .setName(p)
        .setDesc(isFolder ? "資料夾（含底下所有檔案）" : "筆記")
        .addButton((btn) =>
          btn.setButtonText("改為公開").onClick(async () => {
            this.plugin.data.hidden = this.plugin.data.hidden.filter((x) => x !== p)
            await this.plugin.persist()
          }),
        )
    }
  }
}
