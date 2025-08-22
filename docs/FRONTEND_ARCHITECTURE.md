# コンポーネント設計に関する提案書

## 採用する設計手法

- **Atomic Design**
  - UI の基準
  - ボタンからページ全体までを分解して設計する

- **Presentational & Container**  
  - 表示とロジックを分離する基準
  - 例: 表示用の `UserList.tsx` と、データ取得を担う `UserTableContainer.tsx` に分割する

- **Feature-based Design**
  - 機能の基準  
  - ユーザー管理、リスト管理、フィルタなどを機能ごとに分ける
  - データ取得の中でも API 通信と状態管理を分離する

---

## 設計の具体例

1. **大分類**:  
   - `components/` = UI 部分  
   - `features/` = 機能部分  

2. **components/**:  
   - Atomic Design に準拠して分類（atoms / molecules / organisms / layouts）  

3. **features/**:  
   - 機能ごとにフォルダを作成  
   - 各フォルダ内でさらに Container / Presentational に分離  
   - ロジック（API 通信、hooks、store）は `api/`, `hooks/`, `store/` として整理
   - 各機能
        - `auth`: ログイン・ログアウト機能
        - `search`: 検索機能
        - `lecture`: 授業概要表示機能・授業詳細情報表示機能
        - `review`: レビュー表示機能・レビュー投稿機能
        - `profile`: プロフィール閲覧機能・プロフィール編集機能
        - `register`: ユーザー新規登録機能
        - `term`: 利用規約・プライバシーポリシー
        - `contact`: お問い合わせ機能

---

## ディレクトリ構造

```bash
src/
├── app/
│   ├── (public)/
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── register/
│   │   │   └── page.tsx
│   │   ├── forgot-password/
│   │   │   └── page.tsx
│   │   ├── search/
│   │   │   └── page.tsx
│   │   ├── lecture-details/
│   │   │   └── [lectureId]/
│   │   │       └── page.tsx
│   │   ├── terms/
│   │   │   └── page.tsx
│   │   ├── privacy-policy/
│   │   │   └── page.tsx
│   │   └── contact/
│   │       └── page.tsx
│   ├── (protected)/
│   │   ├── dashboard/
│   │   │   └── page.tsx
│   │   ├── edit-profile/
│   │   │   └── page.tsx
│   │   ├── reset-password/
│   │   │   └── page.tsx
│   │   └── create-review/
│   │       └── oage.tsx
│   ├── api/
│   │   └── auth/
│   │       ├── csrf/
│   │       │   └── route.ts
│   │       ├── login/
│   │       │   └── route.ts
│   │       ├── logout/
│   │       │   └── route.ts
│   │       └── me/
│   │           └── route.ts
│   ├── layout.tsx
│   ├── loading.tsx
│   ├── error.tsx
│   └── middleware.ts
├── features/
│   ├── auth/
│   │   ├── components/
│   │   │   ├── LoginForm.tsx
│   │   │   └── AuthGuard.tsx
│   │   ├── containers/
│   │   │   └── LoginContainer.tsx
│   │   ├── hooks/
│   │   │   ├── useLogin.ts
│   │   │   └── useRequireAuth.ts
│   │   ├── services/
│   │   │   └── authApi.ts
│   │   ├── store/
│   │   │   └── authSlice.ts
│   │   └── index.ts
│   ├── search/
│   │   ├── components/
│   │   │   └── FeatureSearchBox.tsx
│   │   ├── containers/
│   │   │   └── SearchBoxContainer.tsx
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   ├── lectures/
│   │   ├── components/
│   │   │   ├── LectureCard.tsx
│   │   │   ├── LectureCardList.tsx
│   │   │   └── LectureSummary.tsx
│   │   ├── containers/
│   │   │   ├── LectureCardListContainer.tsx
│   │   │   └── LectureSummaryContainer.tsx
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   ├── reviews/
│   │   ├── components/
│   │   │   ├── ReviewCard.tsx
│   │   │   └── ReviewCardList.tsx
│   │   ├── containers/
│   │   │   └── ReviewCardListContainer.tsx
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   ├── profiles/
│   │   ├── components/
│   │   │   ├── ProfileCard.tsx
│   │   │   └── EditProfileBoxComponent.tsx
│   │   ├── containers
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   ├── register/
│   │   ├── components/
│   │   │   ├── RegisterBox.tsx
│   │   │   └── ResetPasswordBox.tsx
│   │   ├── containers
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   ├── terms/
│   │   ├── components/
│   │   │   ├── Terms.tsx
│   │   │   └── PrivacyPolicy.tsx
│   │   ├── containers
│   │   ├── hooks
│   │   ├── services
│   │   ├── store
│   │   └── index.ts
│   └── contacts/
│       ├── components/
│       │   └── ContactBox.tsx
│       ├── containers
│       ├── hooks
│       ├── services
│       ├── store
│       └── index.ts
├── shared/
│   ├── ui/
│   │   ├── atoms/
│   │   │   ├── Button.tsx
│   │   │   └── Input.tsx
│   │   ├── molecules/
│   │   │   └── SearchBox.tsx
│   │   ├── organisms/
│   │   │   └── Topbar.tsx
│   │   ├── layouts
│   │   └── index.ts
│   ├── lib/
│   │   ├── http.ts
│   │   ├── env.ts
│   │   ├── constants.ts
│   │   └── auth.server.ts
│   ├── hooks/
│   │   └── useAuth.ts
│   ├── store/
│   │   └── store.ts
│   ├── types/
│   │   ├── index.ts
│   │   └── auth.ts
│   └── styles/
│       └── global.css
├── tests/
│   └── setup.ts
├── assets/
│   └── logo.svg
├── utils/
│   ├── formatDate.ts
│   └── helpers.ts
├── next.config.mjs
└── tsconfig.json
```
