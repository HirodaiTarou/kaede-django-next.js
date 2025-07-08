# Kaede

## 概要

Kaede は、Next.js + Django + Supabase を使用したモダンな Web アプリケーションです。元プロジェクトリポジトリ（https://github.com/atsukihat/l10dev） をベースに開発されています。

## アーキテクチャ

### リポジトリ構成

- **ポリレポ構成**：フロントエンドとバックエンドを分離したリポジトリ構成

### インフラ構成

| 層             | サービス   | 用途                               |
| -------------- | ---------- | ---------------------------------- |
| フロントエンド | Vercel     | 静的サイトホスティング・デプロイ   |
| バックエンド   | Render.com | API サーバーホスティング           |
| データベース   | Supabase   | PostgreSQL・認証・リアルタイム機能 |

## 技術スタック

### フロントエンド

- **Next.js**
  - サーバーサイドレンダリング対応
  - 最適化されたパフォーマンス
- **React**
  - 引き継ぎが容易
  - 豊富な参考資料とコミュニティ
- **TypeScript**
  - 型安全性の確保
  - 開発効率の向上

### バックエンド

- **Django**
  - 標準管理画面の提供
  - チームメンバー（服部、高原）の習熟度が高い
  - 豊富なライブラリとエコシステム
- **Docker**
  - 開発環境の標準化
  - デプロイメントの一貫性

## API 設計・開発戦略

### Django REST Framework (DRF)

- **Django との親和性が高い**
- **シリアライザーによる型安全な API 開発**
- **自動的な OpenAPI 仕様書生成**

### OpenAPI/Swagger 統合

- `drf-spectacular`を使用して Django から OpenAPI 仕様を自動生成
- フロントエンドとの型共有を実現
- API 仕様の自動文書化

### API 設計原則

- **RESTful 設計に準拠**
- **バージョニング戦略**：URL path versioning (`/api/v1/`)
- **一貫したレスポンス形式とエラーハンドリング**

### 型安全性の確保

- **バックエンド**：DRF シリアライザーによる型定義
- **フロントエンド**：OpenAPI 仕様から TypeScript 型を自動生成
- **型生成の自動化**：`openapi-typescript`を使用

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

## チーム構成

- **服部**：Django 開発担当
- **高原**：Django 開発担当
- その他メンバー：フロントエンド・インフラ担当

## 参考資料

- [元プロジェクトリポジトリ](https://github.com/atsukihat/l10dev)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Next.js Documentation](https://nextjs.org/docs)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [openapi-typescript](https://github.com/drwpow/openapi-typescript)
