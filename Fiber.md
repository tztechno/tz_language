###
# Fiber
###


---

`myblog`フォルダ内のファイル階層は、以下のように構成されると良いでしょう。これにより、プロジェクトの管理がしやすくなります。

```
myblog/
├── main.go
├── go.mod
├── go.sum
├── blog.db
├── handlers/
│   ├── post.go
├── models/
│   ├── post.go
├── database/
│   ├── database.go
└── .env
```

### 各ファイル・ディレクトリの役割

- **main.go**: アプリケーションのエントリーポイント。サーバーのセットアップやルーティングの設定を行います。
- **go.mod**: Goモジュールファイル。依存関係を管理します。
- **go.sum**: 依存関係のバージョン情報を保持します。
- **blog.db**: SQLiteのデータベースファイル。データはここに保存されます。
- **handlers/**: ハンドラ関数を格納するディレクトリ。各ハンドラ関数は対応するルートの処理を行います。
  - **post.go**: 投稿に関連するハンドラ関数を定義します。
- **models/**: データモデルを定義するディレクトリ。
  - **post.go**: 投稿データのモデルを定義します。
- **database/**: データベース接続や設定を管理するディレクトリ。
  - **database.go**: データベース接続の初期化を行います。
- **.env**: 環境変数を定義するファイル（必要に応じて使用します）。

### 詳細なコード例

以下に、各ファイルのコード例を示します。

#### main.go

```go
package main

import (
	"log"
	"github.com/gofiber/fiber/v2"
	"myblog/database"
	"myblog/handlers"
)

func main() {
	app := fiber.New()

	// データベース接続の初期化
	database.InitDB()

	// ルーティングの設定
	app.Get("/", handlers.GetPosts)
	app.Post("/post", handlers.CreatePost)
	app.Get("/post/:id", handlers.GetPost)
	app.Delete("/post/:id", handlers.DeletePost)

	// サーバーの起動
	log.Fatal(app.Listen(":3000"))
}
```

#### database/database.go

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

#### models/post.go

```go
package models

type Post struct {
	ID      int    `json:"id"`
	Title   string `json:"title"`
	Content string `json:"content"`
}
```

#### handlers/post.go

```go
package handlers

import (
	"database/sql"
	"github.com/gofiber/fiber/v2"
	"myblog/database"
	"myblog/models"
	"strconv"
)

func GetPosts(c *fiber.Ctx) error {
	rows, err := database.DB.Query("SELECT id, title, content FROM posts")
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}
	defer rows.Close()

	var posts []models.Post
	for rows.Next() {
		var post models.Post
		if err := rows.Scan(&post.ID, &post.Title, &post.Content); err != nil {
			return c.Status(500).SendString(err.Error())
		}
		posts = append(posts, post)
	}

	return c.JSON(posts)
}

func CreatePost(c *fiber.Ctx) error {
	var post models.Post
	if err := c.BodyParser(&post); err != nil {
		return c.Status(400).SendString(err.Error())
	}

	stmt, err := database.DB.Prepare("INSERT INTO posts (title, content) VALUES (?, ?)")
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}
	defer stmt.Close()

	result, err := stmt.Exec(post.Title, post.Content)
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}

	id, err := result.LastInsertId()
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}
	post.ID = int(id)

	return c.JSON(post)
}

func GetPost(c *fiber.Ctx) error {
	id := c.Params("id")
	var post models.Post

	row := database.DB.QueryRow("SELECT id, title, content FROM posts WHERE id = ?", id)
	if err := row.Scan(&post.ID, &post.Title, &post.Content); err != nil {
		if err == sql.ErrNoRows {
			return c.Status(404).SendString("Post not found")
		}
		return c.Status(500).SendString(err.Error())
	}

	return c.JSON(post)
}

func DeletePost(c *fiber.Ctx) error {
	id := c.Params("id")

	stmt, err := database.DB.Prepare("DELETE FROM posts WHERE id = ?")
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}
	defer stmt.Close()

	result, err := stmt.Exec(id)
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		return c.Status(500).SendString(err.Error())
	}

	if rowsAffected == 0 {
		return c.Status(404).SendString("Post not found")
	}

	return c.SendStatus(204)
}
```

### 実行

上記のディレクトリ構造とファイルをセットアップし、`main.go`を実行します。

```bash
go run main.go
```

これで、FiberフレームワークとSQLiteを使用したブログアプリケーションが動作するはずです。APIエンドポイントを使用して投稿の作成、取得、削除が可能になります。

---

GoのFiberフレームワークを使用して、SQLiteをデータベースとして利用するブログを作成する方法を説明します。

### 前提条件
- Goがインストールされていること
- `go`コマンドが動作すること

### 1. プロジェクトのセットアップ

まず、新しいプロジェクトディレクトリを作成し、その中に移動します。

```bash
mkdir fiber_blog
cd fiber_blog
```

次に、Goモジュールを初期化します。

```bash
go mod init fiber_blog
```

### 2. 必要なパッケージのインストール

FiberフレームワークとSQLiteのドライバをインストールします。

```bash
go get github.com/gofiber/fiber/v2
go get github.com/mattn/go-sqlite3
```

### 3. プロジェクトファイルの作成

`main.go`ファイルを作成し、以下のコードを追加します。

```go
package main

import (
	"database/sql"
	"log"
	"strconv"

	"github.com/gofiber/fiber/v2"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	// Fiberアプリケーションの初期化
	app := fiber.New()

	// SQLiteデータベースの接続
	db, err := sql.Open("sqlite3", "./blog.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// テーブルの作成
	createTable := `
	CREATE TABLE IF NOT EXISTS posts (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT NOT NULL,
		content TEXT NOT NULL
	);
	`
	_, err = db.Exec(createTable)
	if err != nil {
		log.Fatal(err)
	}

	// ルートハンドラ
	app.Get("/", func(c *fiber.Ctx) error {
		rows, err := db.Query("SELECT id, title, content FROM posts")
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}
		defer rows.Close()

		var posts []fiber.Map
		for rows.Next() {
			var id int
			var title, content string
			if err := rows.Scan(&id, &title, &content); err != nil {
				return c.Status(500).SendString(err.Error())
			}
			posts = append(posts, fiber.Map{
				"id":      id,
				"title":   title,
				"content": content,
			})
		}

		return c.JSON(posts)
	})

	// 新規投稿の作成ハンドラ
	app.Post("/post", func(c *fiber.Ctx) error {
		type Request struct {
			Title   string `json:"title"`
			Content string `json:"content"`
		}
		var req Request
		if err := c.BodyParser(&req); err != nil {
			return c.Status(400).SendString(err.Error())
		}

		stmt, err := db.Prepare("INSERT INTO posts (title, content) VALUES (?, ?)")
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}
		defer stmt.Close()

		_, err = stmt.Exec(req.Title, req.Content)
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}

		return c.SendStatus(201)
	})

	// 個別投稿の取得ハンドラ
	app.Get("/post/:id", func(c *fiber.Ctx) error {
		id := c.Params("id")
		var post fiber.Map

		row := db.QueryRow("SELECT id, title, content FROM posts WHERE id = ?", id)
		var title, content string
		if err := row.Scan(&id, &title, &content); err != nil {
			if err == sql.ErrNoRows {
				return c.Status(404).SendString("Post not found")
			}
			return c.Status(500).SendString(err.Error())
		}

		post = fiber.Map{
			"id":      id,
			"title":   title,
			"content": content,
		}

		return c.JSON(post)
	})

	// 投稿の削除ハンドラ
	app.Delete("/post/:id", func(c *fiber.Ctx) error {
		id := c.Params("id")
		stmt, err := db.Prepare("DELETE FROM posts WHERE id = ?")
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}
		defer stmt.Close()

		result, err := stmt.Exec(id)
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}

		rowsAffected, err := result.RowsAffected()
		if err != nil {
			return c.Status(500).SendString(err.Error())
		}

		if rowsAffected == 0 {
			return c.Status(404).SendString("Post not found")
		}

		return c.SendStatus(204)
	})

	// サーバーの起動
	log.Fatal(app.Listen(":3000"))
}
```

### 4. 実行

上記のコードを保存し、以下のコマンドで実行します。

```bash
go run main.go
```

### 5. 使用方法

ブラウザやAPIクライアント（Postmanなど）を使用して以下のエンドポイントにアクセスします：

- **全ての投稿の取得**: `GET http://localhost:3000/`
- **新規投稿の作成**: `POST http://localhost:3000/post`  
  JSONボディ：
  ```json
  {
      "title": "新しい投稿",
      "content": "これは新しいブログ投稿の内容です"
  }
  ```
- **個別投稿の取得**: `GET http://localhost:3000/post/:id`
- **投稿の削除**: `DELETE http://localhost:3000/post/:id`

これで、FiberとSQLiteを使用した基本的なブログが完成です。必要に応じて機能を拡張してください。

---
