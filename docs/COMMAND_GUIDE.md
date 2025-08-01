# 開発コマンドガイド

## Docker関連

Dockerの日常的な操作についてはMakefileにショートカットが記述されているのでそちらを利用して欲しいですが、込み入った処理を実行するのであれば以下のようなコマンドが役に立つと思います

### バックエンドコンテナ

- コンテナに入る

    ```bash
    docker exec -it kaede-backend-1 bash
    ```

### DBコンテナ

- コンテナに入る

    ```bash
    docker exec -it kaede-db-1 bash
    ```

- DBに入る

    ```bash
    psql -U kaede
    ```

- DBの一覧を表示

    ```bash
    \dt
    ```
