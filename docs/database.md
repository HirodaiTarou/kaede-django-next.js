# データベース設計

## 概要

Kaedeプロジェクトのデータベース設計です。講義レビューシステムのためのテーブル構成とリレーションを定義しています。

## ER図

```mermaid
erDiagram

lectures ||--o{ lecture_details : "含む"
lecture_details ||--o{ lecture_detail_times : "含む"
users ||--o{ reviews : "投稿する"
users ||--o{ review_logs : "投稿する(ログ)"
users ||--o{ likes : "いいねする"
reviews ||--o{ likes : "受け取る"
users ||--o{ delete_review_requests : "報告する"
reviews ||--o{ delete_review_requests : "受け取る"
lectures ||--o{ reviews : "対象"
lectures ||--o{ review_logs : "対象"
lectures ||--o{ lecture_labels : "含む"
labels ||--o{ lecture_labels : "含む"

lectures {
    id lectureId pk "講義ID"
    string lectureName "授業名"
    string teacherName "主担当教員名"
}

lecture_details {
    id lectureDetailId pk "講義詳細ID"
    id lectureId fk "講義ID"
    string lectureCode "講義コード"
    string syllabusUrl "シラバスURL"
    string location "開講場所"
    string faculty "開講部局"
    string category "科目区分"
    string grade "履修年次"
}

lecture_detail_times {
    id lectureDetailTimeId pk "時間割ID"
    id lectureDetailId fk "講義詳細ID"
    int year "年度"
    string term "ターム"
    string dayOfWeek "曜日"
    string timePeriod "時限"
}

users {
    id id pk "ID（主キー）"
    string userName "ユーザー名"
    string userEmail "メールアドレス"
    string password "パスワード"
    string universityName "大学名"
    string category "所属"
    string faculty "学部"
    string department "学科"
    int admissionYear "入学年度"
    timestamp created_at "作成時間"
    timestamp updated_at "更新時間"
}

reviews {
    id reviewId pk "ID（主キー）"
    id lectureId fk "講義ID"
    id userId fk "ユーザーID"
    integer attendanceYear "受講年度"
    string attendanceConfirm "出欠の有無"
    string weeklyAssignments "毎回のレポート・テスト"
    string midtermAssignments "中間のレポート・テスト"
    string finalAssignments "期末のレポート・テスト"
    string pastExamPossession "過去問の所持"
    string grades "成績"
    int creditLevel "単位取得"
    int interestLevel "面白さ"
    int skillLevel "スキル"
    text comments "コメント"
    timestamp created_at "投稿時間"
    timestamp updated_at "更新時間"
}

review_logs {
    id reviewLogId pk "ID（主キー）"
    id lectureId fk "講義ID"
    id userId fk "ユーザーID"
    integer attendanceYear "受講年度"
    string attendanceConfirm "出欠の有無"
    string weeklyAssignments "毎回のレポート・テスト"
    string midtermAssignments "中間のレポート・テスト"
    string finalAssignments "期末のレポート・テスト"
    string pastExamPossession "過去問の所持"
    string grades "成績"
    int creditLevel "単位取得"
    int interestLevel "面白さ"
    int skillLevel "スキル"
    text comments "コメント"
    string status "状況"
    timestamp created_at "投稿時間"
}

labels {
    id labelId pk "ラベルID"
    string labelName "ラベル名"
}

lecture_labels {
    id lectureId fk "講義ID"
    id labelId fk "ラベルID"
}

likes {
    id reviewId fk "レビューID"
    id userId fk "ユーザーID"
    timestamp created_at "いいね時間"
}

delete_review_requests {
    id reviewId fk "レビューID"
    id userId fk "ユーザーID"
    timestamp created_at "報告時間"
}

contacts {
    id contactId pk "コンタクトID"
    string name "氏名"
    string email "メールアドレス"
    string category "種類"
    text message "メッセージ"
    timestamp created_at "問い合わせ時間"
}
```

## テーブル定義

### 1. lectures（講義テーブル）

講義の基本情報を管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | 講義ID |
| `lectureName` | `string` | `NOT NULL` | 授業名 |
| `teacherName` | `string` | `NOT NULL` | 主担当教員名 |
| `created_at` | `timestamp` | `NOT NULL` | 作成時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 2. lecture_details（講義詳細テーブル）

講義の詳細情報を管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | 講義詳細ID |
| `lectureId` | `id` | `FOREIGN KEY` | 講義ID |
| `lectureCode` | `string` | `NOT NULL` | 講義コード |
| `syllabusUrl` | `string` | - | シラバスURL |
| `location` | `string` | - | 開講場所 |
| `faculty` | `string` | - | 開講部局 |
| `category` | `string` | - | 科目区分 |
| `grade` | `string` | - | 履修年次 |
| `created_at` | `timestamp` | `NOT NULL` | 作成時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 3. lecture_detail_times（講義時間割テーブル）

講義の時間割情報を管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | 時間割ID |
| `lectureDetailId` | `id` | `FOREIGN KEY` | 講義詳細ID |
| `year` | `int` | `NOT NULL` | 年度 |
| `term` | `string` | `NOT NULL` | ターム |
| `dayOfWeek` | `string` | `NOT NULL` | 曜日 |
| `timePeriod` | `string` | `NOT NULL` | 時限 |
| `created_at` | `timestamp` | `NOT NULL` | 作成時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 4. users（ユーザーテーブル）

ユーザー情報を管理するテーブルです。Laravelのシーダーファイルに基づいて定義。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | ID（主キー） |
| `userName` | `string` | `NOT NULL` | ユーザー名 |
| `userEmail` | `string` | `UNIQUE, NOT NULL` | メールアドレス |
| `password` | `string` | `NOT NULL` | パスワード（ハッシュ化） |
| `universityName` | `string` | `NOT NULL` | 大学名 |
| `category` | `string` | `NOT NULL` | 所属 |
| `faculty` | `string` | `NOT NULL` | 学部 |
| `department` | `string` | `NOT NULL` | 学科 |
| `admissionYear` | `int` | `NOT NULL` | 入学年度 |
| `created_at` | `timestamp` | `NOT NULL` | 作成時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 5. reviews（レビューテーブル）

講義レビューを管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | ID（主キー） |
| `lectureId` | `id` | `FOREIGN KEY` | 講義ID |
| `userId` | `id` | `FOREIGN KEY` | ユーザーID |
| `attendanceYear` | `integer` | - | 受講年度 |
| `attendanceConfirm` | `string` | - | 出欠の有無 |
| `weeklyAssignments` | `string` | - | 毎回のレポート・テスト |
| `midtermAssignments` | `string` | - | 中間のレポート・テスト |
| `finalAssignments` | `string` | - | 期末のレポート・テスト |
| `pastExamPossession` | `string` | - | 過去問の所持 |
| `grades` | `string` | - | 成績 |
| `creditLevel` | `int` | - | 単位取得 |
| `interestLevel` | `int` | - | 面白さ |
| `skillLevel` | `int` | - | スキル |
| `comments` | `text` | - | コメント |
| `created_at` | `timestamp` | `NOT NULL` | 投稿時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 6. review_logs（レビューログテーブル）

レビューの変更履歴を管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | ID（主キー） |
| `lectureId` | `id` | `FOREIGN KEY` | 講義ID |
| `userId` | `id` | `FOREIGN KEY` | ユーザーID |
| `attendanceYear` | `integer` | - | 受講年度 |
| `attendanceConfirm` | `string` | - | 出欠の有無 |
| `weeklyAssignments` | `string` | - | 毎回のレポート・テスト |
| `midtermAssignments` | `string` | - | 中間のレポート・テスト |
| `finalAssignments` | `string` | - | 期末のレポート・テスト |
| `pastExamPossession` | `string` | - | 過去問の所持 |
| `grades` | `string` | - | 成績 |
| `creditLevel` | `int` | - | 単位取得 |
| `interestLevel` | `int` | - | 面白さ |
| `skillLevel` | `int` | - | スキル |
| `comments` | `text` | - | コメント |
| `status` | `string` | - | 状況 |
| `created_at` | `timestamp` | `NOT NULL` | 投稿時間 |

### 7. labels（ラベルテーブル）

講義のラベルを管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | ラベルID |
| `labelName` | `string` | `UNIQUE, NOT NULL` | ラベル名 |
| `created_at` | `timestamp` | `NOT NULL` | 作成時間 |
| `updated_at` | `timestamp` | `NOT NULL` | 更新時間 |

### 8. lecture_labels（講義ラベル関連テーブル）

講義とラベルの多対多関係を管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `lectureId` | `id` | `FOREIGN KEY` | 講義ID |
| `labelId` | `id` | `FOREIGN KEY` | ラベルID |

### 9. likes（いいねテーブル）

レビューへのいいねを管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `reviewId` | `id` | `FOREIGN KEY` | レビューID |
| `userId` | `id` | `FOREIGN KEY` | ユーザーID |
| `created_at` | `timestamp` | `NOT NULL` | いいね時間 |

### 10. delete_review_requests（レビュー削除リクエストテーブル）

レビューの削除リクエストを管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `reviewId` | `id` | `FOREIGN KEY` | レビューID |
| `userId` | `id` | `FOREIGN KEY` | ユーザーID |
| `created_at` | `timestamp` | `NOT NULL` | 報告時間 |

### 11. contacts（お問い合わせテーブル）

お問い合わせを管理するテーブルです。

| カラム名 | データ型 | 制約 | 説明 |
|---------|---------|------|------|
| `id` | `increments` | `PRIMARY KEY` | コンタクトID |
| `name` | `string` | `NOT NULL` | 氏名 |
| `email` | `string` | `NOT NULL` | メールアドレス |
| `category` | `string` | - | 種類 |
| `message` | `text` | `NOT NULL` | メッセージ |
| `created_at` | `timestamp` | `NOT NULL` | 問い合わせ時間 |

## リレーション

### 主要なリレーション

1. **lectures → lecture_details**: 1対多
   - 1つの講義に対して複数の詳細情報

2. **lecture_details → lecture_detail_times**: 1対多
   - 1つの講義詳細に対して複数の時間割

3. **users → reviews**: 1対多
   - 1人のユーザーが複数のレビューを投稿

4. **lectures → reviews**: 1対多
   - 1つの講義に対して複数のレビュー

5. **reviews → likes**: 1対多
   - 1つのレビューに対して複数のいいね

6. **lectures ↔ labels**: 多対多（lecture_labels経由）
   - 1つの講義に複数のラベル、1つのラベルが複数の講義に付与

### 制約

- **外部キー制約**: 参照整合性を保証
- **ユニーク制約**: メールアドレス、ラベル名の重複防止
- **NOT NULL制約**: 必須項目の保証

## インデックス戦略

### 推奨インデックス

```sql
-- 検索性能向上のためのインデックス
CREATE INDEX idx_reviews_lecture_id ON reviews(lectureId);
CREATE INDEX idx_reviews_user_id ON reviews(userId);
CREATE INDEX idx_reviews_created_at ON reviews(created_at);

CREATE INDEX idx_likes_review_id ON likes(reviewId);
CREATE INDEX idx_likes_user_id ON likes(userId);

CREATE INDEX idx_lecture_labels_lecture_id ON lecture_labels(lectureId);
CREATE INDEX idx_lecture_labels_label_id ON lecture_labels(labelId);

-- ユーザー検索用
CREATE INDEX idx_users_email ON users(userEmail);
CREATE INDEX idx_users_university ON users(universityName);
```

## データ型の詳細

### 数値型
- `int`: 整数値（年度、レベル評価など）
- `integer`: 大きな整数値
- `increments`: 自動増分ID

### 文字列型
- `string`: 短い文字列（VARCHAR相当）
- `text`: 長い文字列（TEXT相当）

### 日時型
- `timestamp`: 日時情報

### その他
- `boolean`: 真偽値

## Laravel命名規則との対応

### テーブル名
- Laravel: `snake_case` (例: `lecture_details`)
- Django: `snake_case` (例: `lecture_details`)

### カラム名
- Laravel: `camelCase` (例: `lectureName`)
- Django: `snake_case` (例: `lecture_name`)

### 主キー
- Laravel: `id` (increments)
- Django: `id` (AutoField)

### タイムスタンプ
- Laravel: `created_at`, `updated_at`
- Django: `created_at`, `updated_at`

## セキュリティ考慮事項

1. **パスワード**: ハッシュ化して保存
2. **個人情報**: 適切な暗号化・アクセス制御
3. **ログ管理**: レビュー変更履歴の保持
4. **削除リクエスト**: 不適切なコンテンツの報告機能

## マイグレーション戦略

### Laravel → Django 変換

1. **テーブル名**: そのまま使用（snake_case）
2. **カラム名**: camelCase → snake_case
3. **データ型**: Laravel → Django対応
4. **リレーション**: 外部キー制約の維持

### 推奨マイグレーション手順

```bash
# 1. マイグレーションファイル作成
python manage.py makemigrations

# 2. マイグレーション適用
python manage.py migrate

# 3. データ移行（必要に応じて）
python manage.py loaddata initial_data.json
```
