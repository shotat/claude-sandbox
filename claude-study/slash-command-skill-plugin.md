# Claude Code 拡張機能ガイド: Slash Command / Skill / Plugin

Claude Codeの拡張機能には3つの概念がある。それぞれの役割と使い分けを整理する。

---

## 概要

| 概念 | 一言で言うと | 主な用途 |
|------|-------------|---------|
| **Slash Command** | CLIの組み込みコマンド | 基本操作（ヘルプ、クリア、設定） |
| **Skill** | カスタム命令セット | 繰り返すタスクの自動化 |
| **Plugin** | 配布可能なパッケージ | チーム・コミュニティへの共有 |

### 関係性

```
┌─────────────────────────────────────────────────────────┐
│  Plugin（配布パッケージ）                                │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│  │   Skills    │ │   Agents    │ │    Hooks    │ ...   │
│  └─────────────┘ └─────────────┘ └─────────────┘       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  Slash Commands                                         │
│  ┌─────────────────────┐ ┌─────────────────────┐       │
│  │  Built-in Commands  │ │  Custom (via Skill) │       │
│  │  /help, /clear ...  │ │  /my-skill ...      │       │
│  └─────────────────────┘ └─────────────────────┘       │
└─────────────────────────────────────────────────────────┘
```

---

## 1. Slash Command（スラッシュコマンド）

### 定義

`/` で始まるコマンド。Claude Codeのinteractive modeで実行する。

### 種類

#### Built-in Commands（組み込み）

Claude Codeに最初から組み込まれているコマンド。

| コマンド | 説明 |
|---------|------|
| `/help` | ヘルプを表示 |
| `/clear` | 会話履歴をクリア |
| `/compact` | コンテキストを圧縮 |
| `/config` | 設定画面を開く |
| `/context` | コンテキスト使用量を表示 |
| `/cost` | トークン使用量を表示 |
| `/doctor` | インストール状態をチェック |
| `/exit` | セッション終了 |
| `/export` | 会話をエクスポート |
| `/init` | CLAUDE.mdでプロジェクト初期化 |
| `/mcp` | MCPサーバー管理 |
| `/memory` | CLAUDE.mdを編集 |
| `/model` | モデルを変更 |
| `/permissions` | パーミッション設定 |
| `/plan` | Plan Modeに入る |
| `/resume` | セッション再開 |
| `/stats` | 使用統計を表示 |

#### Custom Commands（カスタム）

Skillを定義すると、自動的にslash commandとして使えるようになる。

```bash
# Skillを定義すると...
~/.claude/skills/my-tool/SKILL.md

# こう呼び出せる
/my-tool
```

### 特徴

- ユーザーが明示的に呼び出す
- Built-inはカスタマイズ不可
- Customは完全にカスタマイズ可能

---

## 2. Skill（スキル）

### 定義

再利用可能な命令セット。`SKILL.md`ファイルで定義する。

### 配置場所と優先順位

```
Enterprise（全社）          ← 最優先
    ↓
Personal（~/.claude/skills/）
    ↓
Project（.claude/skills/）
    ↓
Plugin内（plugin/skills/）  ← 最後
```

### 基本構造

```
~/.claude/skills/my-skill/
├── SKILL.md           # メイン指示（必須）
├── reference.md       # 参照ドキュメント（オプション）
└── examples/          # 使用例（オプション）
```

### SKILL.md の書き方

```yaml
---
name: code-review
description: コードレビューを実施する
disable-model-invocation: false
user-invocable: true
allowed-tools: Read, Grep
argument-hint: "[file-path]"
---

以下のファイルをレビューしてください: $ARGUMENTS

チェック項目:
1. コード品質
2. セキュリティ
3. パフォーマンス
```

### Frontmatter フィールド一覧

| フィールド | 説明 | デフォルト |
|-----------|------|-----------|
| `name` | スキル名（小文字、ハイフン可） | 必須 |
| `description` | 説明（Claude自動起動の判断に使用） | 必須 |
| `disable-model-invocation` | Claude自動起動を禁止 | `false` |
| `user-invocable` | `/`メニューに表示 | `true` |
| `allowed-tools` | 使用可能なツール | 全ツール |
| `model` | 使用するモデル | 継承 |
| `context` | 実行コンテキスト | - |
| `agent` | subagentの種類 | - |
| `argument-hint` | 引数のヒント | - |

### 引数の受け取り方

```yaml
---
name: migrate
description: コンポーネントを移行する
---

$ARGUMENTS[0] を $ARGUMENTS[1] から $ARGUMENTS[2] に移行してください。
```

```bash
/migrate Button React Vue
# → "Button を React から Vue に移行してください。"
```

### 動的コンテンツの埋め込み

```yaml
---
name: pr-summary
description: PRの変更をサマリする
---

# PR情報
- Diff: !`gh pr diff`
- Files: !`gh pr diff --name-only`

上記の変更をサマリしてください。
```

`!`バッククォートでシェルコマンドの結果を埋め込める。

### Claude自動起動の制御

| 設定 | 動作 |
|------|------|
| `disable-model-invocation: false` | Claudeが関連タスクで自動起動 |
| `disable-model-invocation: true` | ユーザーが明示的に呼び出したときのみ |

**自動起動を禁止すべきケース:**
- デプロイ処理
- 外部サービスへの送信
- 破壊的な操作

---

## 3. Plugin（プラグイン）

### 定義

Skills、Agents、Hooks、MCPサーバーをまとめて配布するためのパッケージ。

### ディレクトリ構造

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # マニフェスト（必須）
├── skills/              # Skillを含める場合
│   └── my-skill/
│       └── SKILL.md
├── agents/              # Agentを含める場合
│   └── researcher.md
├── hooks/               # Hooksを含める場合
│   └── hooks.json
├── .mcp.json           # MCPサーバー設定
├── README.md
└── LICENSE
```

### plugin.json の書き方

```json
{
  "name": "my-plugin",
  "description": "プラグインの説明",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "homepage": "https://github.com/user/my-plugin",
  "repository": "https://github.com/user/my-plugin",
  "license": "MIT"
}
```

### インストール方法

```bash
# GitHubからインストール
/plugin install https://github.com/user/my-plugin

# ローカルでテスト（開発時）
claude --plugin-dir ./my-plugin
```

### 呼び出し方

Plugin内のSkillは名前空間付きで呼び出す。

```bash
/plugin-name:skill-name
```

例:
```bash
/code-reviewer:security-check src/auth.ts
```

### マーケットプレイス

公式マーケットプレイスで公開・配布が可能。

```bash
# マーケットプレイスを管理
/plugin

# プラグインを検索
/plugin search <keyword>
```

---

## 比較表

### Slash Command vs Skill vs Plugin

| 項目 | Slash Command (Built-in) | Skill | Plugin |
|------|-------------------------|-------|--------|
| **目的** | 基本操作 | カスタムタスク | 配布・共有 |
| **定義方法** | 組み込み | `SKILL.md` | `plugin.json` + 複数ファイル |
| **カスタマイズ** | 不可 | 可能 | 可能 |
| **スコープ** | グローバル | Personal/Project | インストール先 |
| **共有方法** | - | 手動コピー | `/plugin install` |
| **バージョン管理** | - | なし | Semantic Versioning |
| **含められるもの** | - | Skillのみ | Skills, Agents, Hooks, MCP |
| **Claude自動起動** | しない | 設定可能 | Skill設定に依存 |

### いつ何を使う？

| シナリオ | 推奨 |
|---------|------|
| 基本操作（ヘルプ、設定変更） | Built-in Slash Command |
| 個人用の便利コマンド | Skill（Personal） |
| プロジェクト固有のタスク | Skill（Project） |
| チームで共有したい | Plugin |
| 外部に公開したい | Plugin（マーケットプレイス） |
| 複数の機能をセットで提供 | Plugin |

---

## 実践例

### 例1: シンプルなSkill

```yaml
# ~/.claude/skills/explain/SKILL.md
---
name: explain
description: コードをわかりやすく説明する
allowed-tools: Read
---

$ARGUMENTS のコードを以下の形式で説明してください:

1. 概要（1-2文）
2. 処理フロー
3. 重要なポイント
```

```bash
/explain src/auth.ts
```

### 例2: 自動起動禁止のSkill

```yaml
# .claude/skills/deploy/SKILL.md
---
name: deploy
description: 本番環境にデプロイする
disable-model-invocation: true
allowed-tools: Bash
---

以下の手順でデプロイを実行:

1. テスト実行: `npm test`
2. ビルド: `npm run build`
3. デプロイ: `npm run deploy`
```

### 例3: 完全なPlugin

```
review-tools/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── code-review/
│   │   └── SKILL.md
│   └── security-review/
│       └── SKILL.md
└── README.md
```

```json
// .claude-plugin/plugin.json
{
  "name": "review-tools",
  "description": "コードレビュー用ツール集",
  "version": "1.0.0",
  "author": { "name": "Team" }
}
```

```bash
# インストール
/plugin install https://github.com/team/review-tools

# 使用
/review-tools:code-review src/
/review-tools:security-review src/auth/
```

---

## ベストプラクティス

### Skill作成時

1. **descriptionを明確に書く** - Claude自動起動の判断基準になる
2. **危険な操作は`disable-model-invocation: true`** - 意図しない実行を防ぐ
3. **toolsを制限する** - 必要最小限の権限で動作させる
4. **サポートファイルで分割** - SKILL.mdは簡潔に保つ

### Plugin作成時

1. **READMEを充実させる** - 使い方を明記
2. **バージョニングを適切に** - Semantic Versioningに従う
3. **依存関係を明示** - 必要なMCPサーバーなど
4. **LICENSEを含める** - 配布時に必須

---

## 参考リンク

- [Claude Code Skills Documentation](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Claude Code Plugins Documentation](https://docs.anthropic.com/en/docs/claude-code/plugins)
- [CLI Reference](https://docs.anthropic.com/en/docs/claude-code/cli-reference)
