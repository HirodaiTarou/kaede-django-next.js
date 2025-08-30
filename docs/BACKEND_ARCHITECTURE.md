# バックエンドアーキテクチャ設計書

## プロジェクト概要

- **主要機能**: ユーザー管理、授業管理、レビュー管理、お問い合わせ管理
- **アーキテクチャ**: Django REST Framework + JWT 認証 + OpenAPI 仕様

---

## 採用する設計手法

- **Django REST Framework (DRF)**

  - RESTful API の構築
  - シリアライゼーションとバリデーション
  - 認証・認可の実装

- **JWT 認証**

  - セッションレスな認証システム
  - フロントエンドとの連携

- **OpenAPI 仕様**

  - API 仕様の自動生成
  - フロントエンドでの型安全性の確保

---

## 技術スタック

### フレームワーク

- **Django**: [公式サイト](https://www.djangoproject.com/) - 高レベル Python Web フレームワーク
- **Django REST Framework**: [公式サイト](https://www.django-rest-framework.org/) - Web API 構築のためのツールキット
- **Simple JWT**: [公式ドキュメント](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - JWT 認証の実装

### データベース

- **Supabase**: PostgreSQL ベースの BaaS
- **Django ORM**: オブジェクトリレーショナルマッピング

---

## ディレクトリ構造

```bash
backend/
├── core/                    # プロジェクト設定（settings, urls, asgi, wsgi）
├── users/                   # ユーザー管理アプリ
├── lectures/                # 授業管理アプリ
├── reviews/                 # レビュー管理アプリ
├── contacts/                # お問い合わせ管理アプリ
├── static/                  # 静的ファイル
├── staticfiles/             # 静的ファイル（本番用）
├── requirements.txt         # Python 依存関係
├── Dockerfile               # Docker 設定
├── Dockerfile.dev           # 開発用Docker設定
├── entrypoint.sh            # Docker起動スクリプト
├── manage.py                # Django 管理コマンド
└── openapi-schema.yml       # OpenAPI 仕様（自動生成）
```

---

## 主要機能

### 1. ユーザー管理 (`users/`)

- **機能**: ユーザー登録、ログイン、プロフィール管理
- **認証**: JWT 認証（Simple JWT）
- **API**: `/api/v1/users/`, `/api/v1/auth/`

### 2. 授業管理 (`lectures/`)

- **機能**: 授業一覧、詳細表示、検索
- **API**: `/api/v1/lectures/`, `/api/v1/lectures/{id}/`

### 3. レビュー管理 (`reviews/`)

- **機能**: レビュー投稿、一覧表示、評価
- **API**: `/api/v1/reviews/`, `/api/v1/reviews/{id}/`

### 4. お問い合わせ管理 (`contacts/`)

- **機能**: お問い合わせフォーム、管理
- **API**: `/api/v1/contacts/`

---

## 認証・認可システム

### JWT 認証

- **アクセストークン**: 短期間（15 分）
- **リフレッシュトークン**: 長期間（7 日）

### 権限設定

- **IsAuthenticated**: 認証済みユーザーのみ
- **IsOwnerOrReadOnly**: 所有者のみ編集可能

---

## 開発・デプロイ

### 開発環境

- **Docker**: コンテナ化された開発環境
- **PostgreSQL (Docker)**: 開発用データベース

### 本番環境

- **Render.com**: Django アプリケーション
- **Supabase**: 本番データベース

---

## テスト・品質管理

### テスト戦略

- **Unit Tests**: モデル、ビュー、シリアライザーの個別テスト
- **Integration Tests**: API エンドポイントの統合テスト

### コード品質

- **Black**: コードフォーマット
- **isort**: インポート整理
- **flake8**: リントチェック

---

## OpenAPI 統合

### 自動生成

- **drf-spectacular**: OpenAPI 仕様の自動生成
- **Swagger UI**: API ドキュメントの表示

### フロントエンド連携

- **openapi-typescript**: TypeScript 型の自動生成

---

## セキュリティ対策

### 認証・認可

- JWT トークンの適切な管理
- 権限の細かい制御

### データ保護

- 入力値の検証
- SQL インジェクション対策

---
