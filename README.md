# かえで 授業レビューサイト (Version 2)

<div align="center">
  <img width="430" height="430" alt="image" src="https://github.com/user-attachments/assets/45cec7c4-26d5-4ee5-9c5f-0e282d0f9a93" />
</div>

## プロジェクト概要

> 広大生のための授業レビューサイト
> **「かえで 授業レビューサイト」 Version 2**

- [かえで 授業レビューサイト](https://hirodai-kaede.com/)  
- [スタートアップチャレンジ2023](https://www.hiroshima-u.ac.jp/iagcc/news/80635)
- [元のリポジトリ (かえで Version1)](https://github.com/atsukihat/l10dev)

## インフラ構成

| 層             | サービス   | 用途                               |
| -------------- | ---------- | ---------------------------------- |
| フロントエンド | <img src="https://img.shields.io/badge/Vercel-000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />     | 静的サイトホスティング・デプロイ   |
| バックエンド   | <img src="https://img.shields.io/badge/Render-3A3A3A?style=for-the-badge&logo=render&logoColor=white" alt="Render.com" /> | API サーバーホスティング           |
| データベース   | <img src="https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" /> | PostgreSQL・認証・リアルタイム機能 |

## 技術スタック

<p>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Chakra%20UI-319795?style=for-the-badge&logo=chakraui&logoColor=white" alt="Chakra UI" />
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
</p>

## 開発環境構築

### 前提条件

<p>
  <img src="https://img.shields.io/badge/Node.js-v18%2B-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js v18以上" />
  <img src="https://img.shields.io/badge/Python-v3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python v3.9以上" />
  <img src="https://img.shields.io/badge/Docker--2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Git--F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
</p>

### セットアップ

1. リポジトリをクローン

    ```bash
    git clone <repository-url>
    cd kaede
    ```

1. 環境を立ち上げ

    ```bash
    make setup
    ```

### 毎度の開発時

1. 環境の立ち上げ

    ```bash
    make dev
    ```

1. 開発を終わるとき

    ```bash
    make stop
    ```

## 開発戦略

### API設計

- **Django REST Framework (DRF)** + OpenAPI/Swagger 統合
- **RESTful 設計** + URL path versioning (`/api/v1/`)
- **型安全性**：DRF シリアライザー → OpenAPI → TypeScript 型自動生成（`openapi-typescript`）

### 型生成の自動化

1. Django で API エンドポイントを定義
2. `drf-spectacular`で OpenAPI 仕様を自動生成
3. `openapi-typescript`で TypeScript 型を生成
4. フロントエンドで型安全な API 呼び出し

## ドキュメント

- [データベース設計](docs/DATABASE.md)
- [開発コマンドガイド](docs/COMMAND_GUIDE.md)
- [本番環境デプロイ手順](docs/DEPLOYMENT.md)

## 外部リンク

- [かえで 授業レビューサイト](https://hirodai-kaede.com/)  
- [スタートアップチャレンジ2023](https://www.hiroshima-u.ac.jp/iagcc/news/80635)
- [元のリポジトリ (かえで Version1)](https://github.com/atsukihat/l10dev)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Next.js Documentation](https://nextjs.org/docs)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [openapi-typescript](https://github.com/drwpow/openapi-typescript)
