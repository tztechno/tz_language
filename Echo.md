###
# Echo
###

---
3.5

Echoを使用してGo言語でSQLiteを使ったブログを作成する手順を以下に示します。Echoは人気のある軽量なWebフレームワークであり、HTTPルーティングやミドルウェアの処理を簡単に行うことができます。

### 手順

1. **Echoのインストール**

   Echoをインストールするには、まずGoモジュールを使用して以下のコマンドを実行します。

   ```bash
   go get -u github.com/labstack/echo/v4
   ```

   このコマンドは、Echo v4をダウンロードしてインストールします。

2. **SQLiteのインストール**

   SQLiteはGo言語の標準ライブラリには含まれていないため、外部パッケージを使用します。一般的には以下のパッケージを使用します。

   ```bash
   go get -u github.com/mattn/go-sqlite3
   ```

   このコマンドにより、SQLite3用のGo言語のパッケージである`go-sqlite3`がインストールされます。

3. **プロジェクトのディレクトリ構造**

   プロジェクトを構成するために基本的なディレクトリ構造を設定します。

   ```
   myblog/
   ├── main.go
   ├── go.mod
   ├── go.sum
   ├── handlers/
   │   ├── post.go
   ├── models/
   │   ├── post.go
   ├── database/
   │   ├── database.go
   └── .env
   ```

   - `main.go`: エントリーポイントとなるメインのGoプログラム。
   - `handlers/`: リクエストを処理するためのハンドラー関数を定義します。
   - `models/`: データモデルを定義します。
   - `database/`: データベースの接続と初期化を行うファイルを配置します。
   - `.env`: 環境変数の設定ファイル（任意）。

4. **データベースの初期化**

   `database/database.go`ファイルを作成して、SQLiteのデータベース接続とテーブルの作成を行います。

   ```go
   package database

   import (
       "database/sql"
       "log"

       _ "github.com/mattn/go-sqlite3"
   )

   var DB *sql.DB

   func InitDB() {
       var err error
       DB, err = sql.Open("sqlite3", "./blog.db")
       if err != nil {
           log.Fatal(err)
       }

       createTable := `
       CREATE TABLE IF NOT EXISTS posts (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT NOT NULL,
           content TEXT NOT NULL
       );
       `
       _, err = DB.Exec(createTable)
       if err != nil {
           log.Fatal(err)
       }
   }
   ```

5. **モデルの定義**

   `models/post.go`ファイルに投稿のデータモデルを定義します。

   ```go
   package models

   type Post struct {
       ID      int    `json:"id"`
       Title   string `json:"title"`
       Content string `json:"content"`
   }
   ```

6. **ハンドラーの定義**

   `handlers/post.go`ファイルに、HTTPリクエストを処理するためのハンドラー関数を実装します。

   ```go
   package handlers

   import (
       "database/sql"
       "github.com/labstack/echo/v4"
       "myblog/database"
       "myblog/models"
       "net/http"
   )

   // 全ての投稿を取得
   func GetPosts(c echo.Context) error {
       rows, err := database.DB.Query("SELECT id, title, content FROM posts")
       if err != nil {
           return err
       }
       defer rows.Close()

       var posts []models.Post
       for rows.Next() {
           var post models.Post
           if err := rows.Scan(&post.ID, &post.Title, &post.Content); err != nil {
               return err
           }
           posts = append(posts, post)
       }

       return c.JSON(http.StatusOK, posts)
   }

   // 新しい投稿を作成
   func CreatePost(c echo.Context) error {
       post := new(models.Post)
       if err := c.Bind(post); err != nil {
           return err
       }

       stmt, err := database.DB.Prepare("INSERT INTO posts (title, content) VALUES (?, ?)")
       if err != nil {
           return err
       }
       defer stmt.Close()

       _, err = stmt.Exec(post.Title, post.Content)
       if err != nil {
           return err
       }

       return c.JSON(http.StatusCreated, post)
   }

   // 特定の投稿を取得
   func GetPost(c echo.Context) error {
       id := c.Param("id")
       var post models.Post

       row := database.DB.QueryRow("SELECT id, title, content FROM posts WHERE id = ?", id)
       if err := row.Scan(&post.ID, &post.Title, &post.Content); err != nil {
           if err == sql.ErrNoRows {
               return echo.NewHTTPError(http.StatusNotFound, "Post not found")
           }
           return err
       }

       return c.JSON(http.StatusOK, post)
   }

   // 特定の投稿を削除
   func DeletePost(c echo.Context) error {
       id := c.Param("id")

       stmt, err := database.DB.Prepare("DELETE FROM posts WHERE id = ?")
       if err != nil {
           return err
       }
       defer stmt.Close()

       _, err = stmt.Exec(id)
       if err != nil {
           return err
       }

       return c.NoContent(http.StatusNoContent)
   }
   ```

7. **メインのエントリーポイント**

   `main.go`ファイルにEchoアプリケーションのエントリーポイントを実装します。

   ```go
   package main

   import (
       "github.com/labstack/echo/v4"
       "log"
       "myblog/database"
       "myblog/handlers"
       "net/http"
   )

   func main() {
       // データベース接続の初期化
       database.InitDB()

       // Echoのインスタンスを作成
       e := echo.New()

       // ルーティングの設定
       e.GET("/", handlers.GetPosts)
       e.POST("/post", handlers.CreatePost)
       e.GET("/post/:id", handlers.GetPost)
       e.DELETE("/post/:id", handlers.DeletePost)

       // サーバーの起動
       log.Fatal(e.Start(":3000"))
   }
   ```

8. **サーバーの起動**

   最後に、ターミナルで以下のコマンドを実行してEchoサーバーを起動します。

   ```bash
   go run main.go
   ```

   これにより、`http://localhost:3000/`でアプリケーションにアクセスできるようになります。

### まとめ

以上がEchoを使用してGo言語でSQLiteを使ったブログを作成する手順です。これにより、HTTPリクエストの処理、データベースの操作、APIのエンドポイントの作成などがカバーされます。必要に応じてエンドポイントを追加したり、フロントエンドを統合したりして、より実用的なWebアプリケーションに進化させることができます。

---
