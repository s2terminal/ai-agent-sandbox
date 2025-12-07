# AI Agent Sandbox - Copilot Instructions

## Project Overview

AI エージェント開発のサンドボックス環境。

## Development Environment

### Package Manager: uv

すべてのサブプロジェクトは **uv** を使用。`pip` や `poetry` は使用しない。

```bash
# 依存関係インストール（各サブディレクトリで実行）
cd google-adk-python && uv sync
cd litellm-proxy && uv sync
```

### Dev Container (Podman)

- コンテナランタイム: **Podman**（Docker ではない）
- Containerfile ベース: `.devcontainer/Containerfile`
- docker-composeは非推奨（Podmanとの互換性に問題があるらしい）
- 開発環境はコンテナで再現できるようにすること。シェルコマンドでの環境操作は禁止。
