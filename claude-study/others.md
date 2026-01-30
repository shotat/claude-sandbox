# その他の Claude 関連ツール

## Claude Cowork

- 2026年1月にリリースされた汎用AIエージェント
- **「Claude Code for the rest of your work」** というコンセプト
- macOS 向け、Apple の Virtualization Framework 上で動作

### 仕組み

- 指定したフォルダへのアクセス権を与えると、Claude がファイルの読み書き・作成を自律的に実行
- 並列実行可能なタスクは複数の Claude インスタンスを spawn して処理

### ユースケース

- ダウンロードフォルダの整理
- レシートのスクショから経費スプレッドシート作成
- デスクトップのメモから下書き作成
- etc.

### 利用条件

- 当初は Max プラン ($100-200/月) 限定
- 現在は Pro ($20/月)、Team、Enterprise でも利用可能（research preview）

### 参考

- [Introducing Cowork | Claude](https://claude.com/blog/cowork-research-preview)
- [TechCrunch の記事](https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/)

---

## Claude in Excel

- Microsoft Excel に Claude を統合するアドイン
- 2025年10月に research preview としてローンチ、2026年1月から Pro ユーザーにも開放

### 機能

- 複数タブのワークブックを読み込んで内容を理解
- セルレベルの引用付きで計算式を説明
- `#REF!`、`#VALUE!`、循環参照などのエラーを特定・修正提案
- ピボットテーブル、グラフ、ファイルアップロード対応
- `.xlsx` / `.xlsm` 形式をサポート

### モデル

- Sonnet 4.5 または Opus 4.5 を使用
- 財務モデリングや予測タスクに強い

### 注意点

- ⚠️ 外部からの信頼できないスプレッドシートは使わないこと（プロンプトインジェクション攻撃のリスク）

### 参考

- [Claude in Excel | Claude Help Center](https://support.claude.com/en/articles/12650343-claude-in-excel)
- [DataCamp のチュートリアル](https://www.datacamp.com/tutorial/claude-in-excel)
