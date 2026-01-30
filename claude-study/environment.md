# Claude Code の実行環境

## 1. Terminal (CLI)

- `claude` コマンドで起動するシンプルな形
- **Ghostty** とか軽量ターミナルと組み合わせると快適
- 余計なもの入れたくない人に最近人気

## 2. IDE 連携

- **Zed** - 軽量で速い、最近流行り
- **VS Code** - 拡張機能あるけどメモリ食いすぎ問題
- **JetBrains 系** - プラグイン対応
- 軽さ重視なら Zed とか新しめのエディタがいいかも

## 3. Claude Desktop App

- macOS / Windows 向けのGUIアプリ
- MCP サーバー連携が強み
- ⚠️ 内部で **git worktree** 使うので、worktree 嫌いな人は注意（環境構築が遅くなりがち）

## 4. Claude Code on the Web

- ブラウザから Claude Code セッションを起動できる
- ⚠️ **Docker** と **git submodule** が使えない制約あり
- コードリーディングとか軽い調査用途向け
