# Claude Code Skills 入門

Claude Code で Skills を使う方法と、自作スキルを作成する手順をまとめた資料。

## Skills とは

Skills は、Claude が特定のタスクを効率よくこなすための「指示書・スクリプト・リソース」をまとめたフォルダ。
動的に読み込まれて、Claude の能力を拡張する。

**ユースケース例:**
- 会社のブランドガイドラインに沿ったドキュメント作成
- 組織固有のワークフローでデータ分析
- 個人タスクの自動化

## セットアップ手順

### 1. Marketplace の追加

Claude Code で以下のコマンドを実行:

```
/plugin marketplace add anthropics/skills
```

これで `anthropics/skills` リポジトリが Plugin Marketplace として登録される。

### 2. Plugin のインストール

**方法A: 対話的にインストール**

1. `Browse and install plugins` を選択
2. `anthropic-agent-skills` を選択
3. `document-skills` または `example-skills` を選択
4. `Install now` を選択

**方法B: コマンドで直接インストール**

```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

### 3. インストールできる Plugin 一覧

| Plugin名 | 内容 |
|----------|------|
| `document-skills` | Excel, Word, PowerPoint, PDF の操作 |
| `example-skills` | skill-creator, mcp-builder, frontend-design, webapp-testing など |

`skill-creator` は `example-skills` に含まれてる。

## Skills の使い方

インストール後は、普通に話しかけるだけでOK。

```
Use the PDF skill to extract the form fields from path/to/some-file.pdf
```

## 自作 Skill の作成

### 基本構造

Skill は `SKILL.md` ファイルを含むフォルダ。最低限これだけあればいい。

```
my-skill/
└── SKILL.md
```

### SKILL.md のテンプレート

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

### Frontmatter の必須フィールド

| フィールド | 説明 |
|-----------|------|
| `name` | スキルのユニーク識別子（小文字、スペースはハイフン） |
| `description` | スキルが何をするか、いつ使うかの説明 |

### skill-creator を使ってスキルを作る

`example-skills` をインストールしていれば、skill-creator が使える。

```
skill-creator を使って、○○するスキルを作って
```

Claude が対話的にスキル作成をサポートしてくれる。

## 参考リンク

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Agent Skills 仕様](https://agentskills.io)
- [anthropics/skills リポジトリ](https://github.com/anthropics/skills)
