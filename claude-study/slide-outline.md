# Claude Code 勉強会 スライド構成案（15分版 + ハンズオン）

## 1. オープニング（1分）
- Claude Code とは
- エージェント型 = 自律的にファイル操作・コマンド実行

---

## 2. 最重要ポイント: コンテキスト管理（3分）
- コンテキストウィンドウはすぐいっぱいになる
- いっぱいになると指示を「忘れる」、ミスが増える
- **対策**: `/clear` でリセット、サブエージェントで調査委譲

---

## 3. 効果的な使い方（4分）
- **検証方法を与える**（テスト、スクショ、期待出力）
- **探索 → 計画 → 実装** のフロー（Plan Mode）
- **具体的なコンテキスト**を提供（@でファイル参照）

---

## 4. 環境セットアップのコツ（3分）
- **CLAUDE.md**: 簡潔に、剪定を忘れずに
- 権限設定 / MCP / フック（概要だけ）

---

## 5. Skill / Plugin とは（3分）
- **Skill**: カスタム命令セット（SKILL.md）
- **Plugin**: 配布可能なパッケージ
- → ハンズオンで実際に触ってみる

---

## 6. まとめ（1分）
- コンテキスト管理が命
- 検証方法を与える
- Skill で効率化

---

## ハンズオン（別枠）
- Marketplace から Skill インストール
- skill-creator で自作 Skill 作成

---

## 補足（時間があれば）
- よくある失敗パターン
- その他のツール（Claude Cowork, Claude in Excel）

---

## 参考資料
- claude-code-best-practices-ja.md
- slash-command-skill-plugin.md
- skill-creator.md
- environment.md
- others.md
