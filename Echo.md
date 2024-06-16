###
# Echo
###

---
3.5

`ajax.html`でJavaScriptを使ってバックエンド（GoのEchoアプリケーション）と通信するための方法を説明します。以下の手順に従って実装していきます。

### バックエンド（GoのEchoアプリケーション）の設定

1. **Echoのルーティングを追加**:

   GoのEchoアプリケーションで、`/calculate`エンドポイントにPOSTリクエストを処理するハンドラーを追加します。このハンドラーは、受け取った数値に基づいてLucas数を計算し、結果をJSON形式で返します。

   ```go
   package main

   import (
       "fmt"
       "log"
       "myblog/database"
       "myblog/handlers"
       "strconv"
       "time"

       "github.com/labstack/echo/v4"
       "github.com/labstack/echo/v4/middleware"
   )

   func main() {
       // データベース接続の初期化
       database.InitDB()

       // Echoのインスタンスを作成
       e := echo.New()

       // 静的ファイルをホストする設定
       e.Static("/", "public") // "public"は静的ファイルが格納されているディレクトリ名に置き換える

       // ミドルウェアの設定
       e.Use(middleware.Logger())
       e.Use(middleware.Recover())

       // ルーティングの設定
       e.GET("/", handlers.GetPosts)
       e.POST("/post", handlers.CreatePost)
       e.GET("/post/:id", handlers.GetPost)
       e.DELETE("/post/:id", handlers.DeletePost)

       // /calculate エンドポイントのハンドラーを追加
       e.POST("/calculate", calculateLucasNumber)

       // サーバーの起動
       log.Fatal(e.Start(":3000"))
   }

   // calculateLucasNumber は /calculate エンドポイントのハンドラー関数
   func calculateLucasNumber(c echo.Context) error {
       // リクエストから数値 n を取得
       var request struct {
           N int `json:"n"`
       }
       if err := c.Bind(&request); err != nil {
           return echo.NewHTTPError(http.StatusBadRequest, "Invalid request")
       }
       n := request.N

       // Lucas数の計算
       startTime := time.Now()
       lucasNumber := getLucasNumber(n)
       endTime := time.Now()
       processTime := endTime.Sub(startTime).Milliseconds()

       // 結果をJSONで返す
       response := map[string]interface{}{
           "result":      lucasNumber,
           "process_time": processTime,
       }
       return c.JSON(http.StatusOK, response)
   }

   // getLucasNumber は n 番目のLucas数を計算する関数（例として単純な実装）
   func getLucasNumber(n int) int {
       if n == 0 {
           return 2
       }
       if n == 1 {
           return 1
       }
       return getLucasNumber(n-1) + getLucasNumber(n-2)
   }
   ```

2. **Lucas数の計算処理**:

   `getLucasNumber`関数は、単純な再帰による方法でn番目のLucas数を計算しています。実際のアプリケーションでは、より効率的な方法で計算する必要がありますが、ここでは例としてこの実装を使用しています。

### ajax.htmlの設定

`ajax.html`のJavaScript部分を、GoのEchoアプリケーションと通信するように変更します。

```html
<!DOCTYPE html>
<html>

<head>
    <title>Lucas Number Calculator</title>
</head>

<body>
    <p>AJAX Lucas Number</p>
    <input type="number" id="inputN" placeholder="Enter a number">
    <button onclick="sendRequest()">Calculate</button>
    <div id="result"></div>
    <div id="time"></div>

    <script>
        function sendRequest() {
            const n = document.getElementById('inputN').value;
            fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ n: parseInt(n) }) // 数値型に変換してJSON形式で送信
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('result').innerText = `Lucas Number L${n} = ${data.result}`;
                    document.getElementById('time').innerText = `Time: ${(data.process_time / 1000).toFixed(3)} sec`;
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    </script>
</body>

</html>
```

### 動作確認

1. **サーバーの起動**:

   コマンドラインで`go run main.go`を実行してEchoサーバーを起動します。

   ```bash
   go run main.go
   ```

2. **ブラウザでアクセス**:

   ブラウザで `http://localhost:3000/ajax.html` にアクセスします。`ajax.html`の画面で数値を入力してCalculateボタンをクリックすると、バックエンドのEchoアプリケーションにPOSTリクエストが送信され、計算結果が表示されるはずです。

この方法で、JavaScriptとEchoを使ってフロントエンドとバックエンドの通信を確立し、Lucas数を計算して結果を表示することができます。

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
