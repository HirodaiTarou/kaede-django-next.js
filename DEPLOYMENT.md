# 本番環境デプロイ手順

## 0. 環境管理の基本

### 環境変数ファイルの構成

#### フロントエンド（Next.js）
```
frontend/
├── .env.local          # 開発環境（gitignore）
├── .env.example        # テンプレート
└── .env.production     # 本番環境（gitignore）
```

#### バックエンド（Django）
```
backend/
├── .env                # 開発環境（gitignore）
├── .env.example        # テンプレート
└── settings_production.py  # 本番環境設定
```

### 開発環境セットアップ手順

#### 1. 環境変数ファイルの作成
```bash
# フロントエンド
cp frontend/.env.example frontend/.env.local

# バックエンド
cp backend/.env.example backend/.env
```

#### 2. 環境変数の設定内容

**フロントエンド（.env.local）**:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000/api
NEXT_PUBLIC_ENVIRONMENT=development
NEXT_PUBLIC_APP_NAME=Kaede Dev
```

**バックエンド（.env）**:
```bash
# データベース設定
POSTGRES_DB=kaede
POSTGRES_USER=kaede
POSTGRES_PASSWORD=kaede
DB_HOST=localhost
DB_PORT=5432

# Django設定
SECRET_KEY=your-secret-key-here
DEBUG=True

# CORS設定
FRONTEND_URL=http://localhost:3000
```

#### 3. Docker環境での開発
```bash
# 開発サーバーの起動
docker-compose up -d

# アクセス先
# フロントエンド: http://localhost:3000
# バックエンド: http://localhost:8000
# データベース: localhost:5432
```

#### 4. 開発時の注意点
- `.env`ファイルは`.gitignore`に追加済み
- 機密情報は環境変数で管理
- 本番環境の設定は変更しない

### 本番環境での環境変数管理

#### Vercel（フロントエンド）
Vercelダッシュボード → プロジェクト設定 → Environment Variables:
```bash
NEXT_PUBLIC_API_URL=https://your-app.onrender.com/api
NEXT_PUBLIC_ENVIRONMENT=production
NEXT_PUBLIC_APP_NAME=Kaede
```

#### Render.com（バックエンド）
Render.comダッシュボード → サービス設定 → Environment:
```bash
SECRET_KEY=<自動生成>
DJANGO_SETTINGS_MODULE=core.settings_production
DATABASE_URL=<Supabaseから取得>
FRONTEND_URL=<VercelのURL>
DEBUG=False
```

## 1. Supabase セットアップ

### GUI操作:
1. https://supabase.com にログイン
2. 「New Project」→ プロジェクト名: `kaede-production`
3. Region: `Northeast Asia (Tokyo)`
4. Database Password: 強力なパスワード設定
5. 「Create new project」

### 取得する情報:
- Database URL: `Settings` → `Database` → `Connection string` → `URL`
- API URL: `Settings` → `API` → `URL`
- anon key (匿名キー): `Settings` → `API` → `anon public`
  - フロントエンドからSupabaseにアクセスする際に使用する公開キー
  - 認証が必要なAPIでも安全に使用可能（Row Level Security設定により制御）

## 2. Render.com バックエンドデプロイ

### GUI操作:
1. https://render.com にログイン
2. 「New」→「Web Service」
3. GitHubリポジトリを連携
4. 設定:
   - Name: `kaede-backend`
   - Runtime: `Python 3`
   - Build Command: `pip install -r backend/requirements.txt && python backend/manage.py collectstatic --noinput`
   - Start Command: `cd backend && gunicorn --bind 0.0.0.0:$PORT core.wsgi:application`

### 環境変数設定:
```
SECRET_KEY=<自動生成>
DJANGO_SETTINGS_MODULE=core.settings_production
DATABASE_URL=<Supabaseから取得>
FRONTEND_URL=<後でVercelから取得>
DEBUG=False
```

## 3. Vercel フロントエンドデプロイ

### GUI操作:
1. https://vercel.com にログイン
2. 「New Project」→ GitHubリポジトリインポート
3. Framework Preset: `Next.js`
4. Root Directory: `frontend`

### 環境変数設定:
```
NEXT_PUBLIC_API_URL=<Render.comから取得したURL>/api
```

## 4. 相互URL設定

### Render.com環境変数更新:
```
FRONTEND_URL=<VercelのURL>
```

### Vercel環境変数更新:
```
NEXT_PUBLIC_API_URL=<RenderのURL>/api
```

## 5. データベースマイグレーション

Render.comのWebサービスが起動後、自動でマイグレーションが実行されます。

## 6. テスト

1. フロントエンド: `<vercel-url>`
2. バックエンドAPI: `<render-url>/api/hello/`
3. ユーザー一覧: `<render-url>/api/users/`

## トラブルシューティング

### よくある問題:
1. **CORS エラー**: `FRONTEND_URL` が正しく設定されているか確認
2. **データベース接続エラー**: `DATABASE_URL` が正しいか確認
3. **静的ファイル**: `collectstatic` が実行されているか確認
4. **環境変数エラー**: 環境変数が正しく設定されているか確認

### 環境変数関連の問題

#### 開発環境
- **フロントエンドがAPIに接続できない**: `NEXT_PUBLIC_API_URL` が正しいか確認
- **バックエンドがデータベースに接続できない**: `.env` ファイルのデータベース設定を確認
- **CORSエラー**: `FRONTEND_URL` が正しく設定されているか確認

#### 本番環境
- **Vercelで環境変数が読み込まれない**: Vercelダッシュボードで環境変数が設定されているか確認
- **Render.comで環境変数が読み込まれない**: Render.comダッシュボードで環境変数が設定されているか確認
- **API接続エラー**: `NEXT_PUBLIC_API_URL` が正しい本番URLになっているか確認

### 環境変数の確認方法

#### フロントエンド（Next.js）
```javascript
// ブラウザのコンソールで確認
console.log(process.env.NEXT_PUBLIC_API_URL);
```

#### バックエンド（Django）
```python
# Djangoシェルで確認
python manage.py shell
>>> import os
>>> print(os.environ.get('DATABASE_URL'))
```

### ログ確認:
- Render.com: Dashboardの「Logs」タブ
- Vercel: Dashboardの「Functions」タブ
