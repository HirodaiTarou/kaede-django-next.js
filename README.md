# Kaede

## 概要

Kaede は、Next.js + Django + Supabase を使用したモダンな Web アプリケーションです。
元プロジェクトリポジトリ（https://github.com/atsukihat/l10dev） をベースに開発されています。

## アーキテクチャ

### リポジトリ構成

- **レポ構成**：フロントエンドとバックエンドを分離したリポジトリ構成

### インフラ構成

| 層             | サービス   | 用途                               |
| -------------- | ---------- | ---------------------------------- |
| フロントエンド | Vercel     | 静的サイトホスティング・デプロイ   |
| バックエンド   | Render.com | API サーバーホスティング           |
| データベース   | Supabase   | PostgreSQL・認証・リアルタイム機能 |

## 技術スタック

### フロントエンド

- Next.js
- React
- TypeScript

### バックエンド

- Django
- Docker

## API 設計・開発戦略

- **Django REST Framework (DRF)** + OpenAPI/Swagger 統合
- **RESTful 設計** + URL path versioning (`/api/v1/`)
- **型安全性**：DRF シリアライザー → OpenAPI → TypeScript 型自動生成（`openapi-typescript`）

## 開発環境構築

### 前提条件

- Node.js (v18 以上)
- Python (v3.9 以上)
- Docker
- Git

### セットアップ

1. リポジトリをクローン

```bash
git clone <repository-url>
cd kaede
```

2. フロントエンド環境構築

```bash
# フロントエンドディレクトリに移動
cd frontend
npm install
```

3. バックエンド環境構築

```bash
# バックエンドディレクトリに移動
cd backend
pip install -r requirements.txt
```

4. Docker コンテナの起動

```bash
docker-compose up -d
```

## 開発ワークフロー

### 型生成の自動化

1. Django で API エンドポイントを定義
2. `drf-spectacular`で OpenAPI 仕様を自動生成
3. `openapi-typescript`で TypeScript 型を生成
4. フロントエンドで型安全な API 呼び出し

### デプロイメント

- **フロントエンド**：Vercel への自動デプロイ
- **バックエンド**：Render.com への自動デプロイ
- **データベース**：Supabase でのマネージド運用



## 参考資料

- [元プロジェクトリポジトリ](https://github.com/atsukihat/l10dev)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Next.js Documentation](https://nextjs.org/docs)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [openapi-typescript](https://github.com/drwpow/openapi-typescript)
