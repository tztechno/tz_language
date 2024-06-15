# React
### 


---
3.5

```
blog/
├── backend/
│   ├── server.js
│   ├── database.js
│   └── routes/
│       └── posts.js
└── frontend/
    ├── public/
    ├── src/
    ├── package.json
    └── ...
```

この構成では、`blog` という親フォルダ内に `backend` と `frontend` という2つのサブフォルダがあります。それぞれが別々のサーバーで動作し、連携してブログアプリケーションを構築することができます。

### 手順の概要

1. **バックエンドの設定 (`backend/`)**:
   - `backend/` ディレクトリ内に Express サーバーを設定し、データベースとの接続、API の作成を行います。具体的には、`server.js` で Express アプリケーションを起動し、`database.js` でデータベースの設定を行います。`routes/` 内のファイルでAPIのエンドポイントを管理します。

2. **フロントエンドの設定 (`frontend/`)**:
   - `frontend/` ディレクトリ内に React アプリケーションをセットアップします。`src/` 内にコンポーネントやページを作成し、必要に応じて `axios` などのライブラリを使用してバックエンドのAPIと通信します。

3. **両者の連携**:
   - フロントエンドからバックエンドのエンドポイントに対して、HTTPリクエストを送信してデータの取得や操作を行います。例えば、ブログ記事の一覧表示や投稿作成などを行います。

### 実行手順

1. **バックエンドの起動**:
   - ターミナルで `backend/` ディレクトリに移動し、Express サーバーを起動します。

   ```bash
   cd blog/backend
   node server.js
   ```

2. **フロントエンドの起動**:
   - 別のターミナルウィンドウを開き、`frontend/` ディレクトリに移動して React アプリケーションを起動します。

   ```bash
   cd blog/frontend
   npm start
   ```

3. **ブラウザでアプリケーションにアクセス**:
   - ブラウザで `http://localhost:3000` にアクセスし、React アプリケーションが表示されることを確認します。

4. **動作確認**:
   - ブログの記事一覧を表示したり、新しい記事を投稿したりする機能が正常に動作するかどうかを確認します。フロントエンドからバックエンドへのリクエストが期待通りに処理されているか、データが正しく表示されているかを確認します。

このように、`backend` と `frontend` を同一の親フォルダ内に配置して、それぞれ別のサーバーとして独立して動作させることは一般的であり、複数の開発者やチームがそれぞれの領域で作業を進めやすくする利点があります。

---
```
2024-06-15

cd blog

cd frontend 
use port3000

cd backend
use port3001

cd myblog/backend
node server.js

cd myblog/frontend
npm start

Add Postボタンが有効ではない
おそらく3.5では解決しない課題

```
---
3.5

`addpost`（投稿追加機能）を実装するには、フロントエンドとバックエンドの両方でいくつかのステップを踏む必要があります。以下に、それぞれのステップを示します。

### バックエンドの実装

#### 1. ExpressサーバーでのPOSTリクエストの処理

バックエンドの `server.js` ファイルで、POSTリクエストを処理するエンドポイントを作成します。

```javascript
// server.js

app.post('/api/posts', (req, res) => {
  const { title, content } = req.body;
  db.run("INSERT INTO posts (title, content) VALUES (?, ?)", [title, content], function (err) {
    if (err) {
      res.status(400).json({ error: err.message });
      return;
    }
    res.json({
      message: "success",
      data: { id: this.lastID }
    });
  });
});
```

#### 2. フロントエンドとの連携

フロントエンドからこのエンドポイントにPOSTリクエストを送信するために、`axios`を使用します。

### フロントエンドの実装

#### 1. フォームの作成とデータの管理

`PostForm.js` ファイルで投稿フォームを作成し、入力されたデータを管理します。

```javascript
// PostForm.js

import React, { useState } from 'react';
import axios from 'axios';

function PostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/posts', { title, content })
      .then(response => {
        console.log(response.data); // 成功した場合の処理
        // 投稿後にフォームをクリアするなどの処理を追加することもできます
        setTitle('');
        setContent('');
      })
      .catch(error => {
        console.error('There was an error creating the post!', error); // エラーハンドリング
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title</label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label>Content</label>
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
      </div>
      <button type="submit">Add Post</button>
    </form>
  );
}

export default PostForm;
```

#### 2. フォームの表示

`App.js` ファイルで投稿フォームを表示します。

```javascript
// App.js

import React from 'react';
import PostList from './PostList';
import PostForm from './PostForm';

function App() {
  return (
    <div className="App">
      <h1>Blog</h1>
      <PostForm />
      <PostList />
    </div>
  );
}

export default App;
```

### 確認とテスト

1. バックエンドサーバー (`node server.js`) とフロントエンドサーバー (`npm start`) を起動します。
2. ブラウザでアプリケーションにアクセスし、投稿フォームが表示されることを確認します。
3. フォームにタイトルとコンテンツを入力し、「Add Post」ボタンをクリックします。
4. コンソールログやデータベースの内容を確認して、投稿が正しく追加されていることを確認します。

これにより、フロントエンドからバックエンドにデータを送信し、データベースに新しい投稿を追加する機能が実装されます。


---
3.5

確かに、バックエンドとフロントエンドを同時に立ち上げる場合は、別々のターミナルセッションを使用する必要があります。また、ポートが同じ場合には衝突が発生しますので、異なるポート番号を使用する必要があります。

以下は、正しい手順です。

### 1. バックエンドサーバーの起動

まず、バックエンドサーバーを起動します。この例ではポート番号3000を使用します。

```bash
cd myblog/backend
node server.js
```

### 2. フロントエンドサーバーの起動

別のターミナルウィンドウを開いて、フロントエンドサーバーを起動します。通常はポート番号3000が使用されるため、フロントエンドは異なるポート番号（例えば3001）を使用します。

```bash
cd myblog/frontend
npm start
```

### 注意点

- バックエンドとフロントエンドが別々のポートで起動するようにします（通常、バックエンドが3000、フロントエンドが3001など）。
- `cd ../` を使用するのは、現在の作業ディレクトリから親ディレクトリに移動するためですが、それぞれのターミナルセッションで適切なディレクトリに移動してからコマンドを実行する必要があります。
- バックエンドとフロントエンドのポート番号を設定するには、それぞれのプロジェクトの設定ファイル（例えばExpressの設定ファイルやReactの設定ファイル）を変更する必要があります。

これにより、バックエンドとフロントエンドが同時に立ち上がり、正常に連携できる状態になります。

---
4.0

ReactでSQLiteを使ってブログを作るプロジェクトでは、以下の主要なステップが必要です。

1. **環境設定**
2. **バックエンドの構築**
3. **フロントエンドの構築**
4. **デプロイメント**

### 1. 環境設定

- Node.jsとnpmをインストールします。
- SQLiteをインストールします。

### 2. バックエンドの構築

バックエンドはNode.jsを使い、ExpressフレームワークとSQLiteデータベースを利用します。

#### 必要なパッケージをインストール

```bash
npm install express sqlite3
```

#### ディレクトリ構成

```plaintext
blog-app/
├── backend/
│   ├── database.js
│   ├── server.js
│   └── routes/
│       ├── posts.js
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
```

#### `database.js`の設定

SQLiteデータベースをセットアップします。

```javascript
const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database(':memory:');

db.serialize(() => {
  db.run("CREATE TABLE posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT)");

  const stmt = db.prepare("INSERT INTO posts (title, content) VALUES (?, ?)");
  stmt.run("First Post", "This is the content of the first post.");
  stmt.run("Second Post", "This is the content of the second post.");
  stmt.finalize();
});

module.exports = db;
```

#### `server.js`の設定

Expressサーバーを設定し、APIエンドポイントを定義します。

```javascript
const express = require('express');
const bodyParser = require('body-parser');
const db = require('./database');

const app = express();
app.use(bodyParser.json());

app.get('/api/posts', (req, res) => {
  db.all("SELECT * FROM posts", [], (err, rows) => {
    if (err) {
      res.status(400).json({error: err.message});
      return;
    }
    res.json({
      data: rows
    });
  });
});

app.post('/api/posts', (req, res) => {
  const {title, content} = req.body;
  db.run("INSERT INTO posts (title, content) VALUES (?, ?)", [title, content], function(err) {
    if (err) {
      res.status(400).json({error: err.message});
      return;
    }
    res.json({
      message: "success",
      data: {id: this.lastID}
    });
  });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

### 3. フロントエンドの構築

Reactでフロントエンドを構築します。

#### Create React Appのセットアップ

```bash
npx create-react-app frontend
cd frontend
```

#### 必要なパッケージをインストール

```bash
npm install axios
```

#### フロントエンドの構成

`src/`ディレクトリ内に以下のコンポーネントを作成します。

- `App.js`
- `PostList.js`
- `PostForm.js`

##### `App.js`

```javascript
import React from 'react';
import PostList from './PostList';
import PostForm from './PostForm';

function App() {
  return (
    <div className="App">
      <h1>Blog</h1>
      <PostForm />
      <PostList />
    </div>
  );
}

export default App;
```

##### `PostList.js`

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PostList() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get('/api/posts')
      .then(response => {
        setPosts(response.data.data);
      })
      .catch(error => {
        console.error('There was an error fetching the posts!', error);
      });
  }, []);

  return (
    <div>
      <h2>Posts</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;
```

##### `PostForm.js`

```javascript
import React, { useState } from 'react';
import axios from 'axios';

function PostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/api/posts', { title, content })
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('There was an error creating the post!', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title</label>
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>
      <div>
        <label>Content</label>
        <textarea
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
      </div>
      <button type="submit">Add Post</button>
    </form>
  );
}

export default PostForm;
```

### 4. デプロイメント

バックエンドとフロントエンドのサーバーを起動し、接続を確認します。

```bash
# backend
node backend/server.js

# frontend
cd frontend
npm start
```

以上の手順に従って、ReactとSQLiteを使ったシンプルなブログアプリケーションを作成することができます。

---

Reactアプリケーションのディレクトリには、以下のような構造が作成されます：

```
my-app/
├── node_modules/
├── public/
├── src/
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   └── serviceWorker.js
├── .gitignore
├── package.json
├── README.md
└── yarn.lock
```

---

Reactをインストールする前に、Node.jsとnpmをインストールする必要があります。

### Node.jsのインストール

Node.jsの公式サイト( https://nodejs.org/en/ )にアクセスします。
ご利用のOSに合わせた推奨バージョンのNode.jsをダウンロードします。
ダウンロードしたインストーラーを実行し、指示に従ってNode.jsをインストールします。

### Reactのインストール

Node.jsとnpmがインストールされたら、次のようにReactをインストールできます。

コマンドプロンプト(Windows)またはターミナル(Mac/Linux)を開きます。
新しいReactプロジェクトを作成したい場所に移動します。
次のコマンドを実行して、新しいReactアプリをセットアップします。

```
npx create-react-app my-app
```

my-appの部分は、お好みのプロジェクト名に置き換えてください。

インストールが完了したら、次のコマンドでプロジェクトディレクトリに移動します。
```
cd my-app
```
最後に、次のコマンドでReactの開発サーバーを起動します。
```
npm start
```
これで、ブラウザで http://localhost:3000 にアクセスすると、Reactアプリが表示されるはずです。

Reactのインストールが完了しました。必要に応じて、さらにReact Routerなどの追加パッケージをインストールできます。npm installコマンドを使ってパッケージをプロジェクトに追加できます。
```
npm install react-router-dom
```


---

## React18

Reactの最新バージョンは現在、2022年3月29日にリリースされた React 18です。
React 18の主な新機能は以下の通りです:

### コンカレントレンダリング - 
新しいレンダリングエンジンにより、レンダリングプロセスの途中経過をストリーミングできるようになりました。結果としてアプリの読み込み時間が短縮され、レスポンシブ性が向上します。
### Automatic Batching - 
複数の状態更新がある場合、Reactが自動的にそれらをバッチ処理するようになりました。これにより無駄なレンダリングが回避されパフォーマンスが向上します。
### StartTransition API - 
高優先度と低優先度のstate更新を明示的に分けられるようになりました。これによりユーザー体験を優先しつつ、バックグラウンド処理もスムーズに行えます。
### Suspense on Server Rendering - 
サーバーサイドレンダリングでもSuspenseを使用できるようになり、データフェッチ中の描画の最適化が可能になりました。
Automatic Static Optimization - アプリのパフォーマンスを向上させる、Reactの自動最適化の改善が行われました。
### Stricter Concurrency - 
より厳格な並行性制御が導入され、レースコンディションのリスクが低減しました。

その他にもHooksの改善、開発者体験の向上など、多岐にわたる変更が加えられています。
Reactチームは18がメジャーアップグレードと位置づけており、新機能を活用するには既存のコンポーネントを一部書き換える必要があります。そのためReact 18への移行は徐々に進められていますが、長期的にはほとんどのReactアプリがReact 18に移行していくことが予想されています。

---

はい、Vue.jsとReactは共存することができます。両方のフレームワークは、JavaScriptに基づいており、ウェブアプリケーションの開発に使用されますが、異なる構文やアーキテクチャを持っています。

いくつかのシナリオで、Vue.jsとReactを同じプロジェクト内で共存させることができます。

### 部分的な統合:
例えば、既存のVue.jsアプリケーションにReactコンポーネントを追加する場合、Vue.jsアプリケーションの一部にReactを統合することができます。
### マイクロフロントエンド:
マイクロフロントエンドアーキテクチャでは、複数のフロントエンド技術を組み合わせて、複雑なUIを構築します。このような場合、Vue.jsとReactを別々のマイクロフロントエンドに組み込むことができます。
### 異なる機能領域:
大規模なアプリケーションでは、異なる機能領域ごとに異なるフレームワークを使用することがあります。例えば、一部の部分はVue.jsで開発し、他の部分はReactで開発することができます。

ただし、このようなアプローチを採用する場合、コンポーネント間のコミュニケーションやスタイルの統一など、いくつかの課題が発生する可能性があります。それでも、Vue.jsとReactを共存させることは完全に可能であり、プロジェクトの要件や開発者の好みに応じて柔軟に選択することができます。

---


Reactは、Facebookによって開発されたJavaScriptライブラリで、UIの構築に特化しています。以下に、Reactの主な特徴をいくつか挙げてみましょう。

### 仮想DOM (Virtual DOM):
Reactは、仮想DOMを使用して高速なUIのレンダリングを実現します。実際のDOMの変更を行う前に、Reactは変更が必要な部分の仮想DOMをメモリ上で計算し、最小限のDOM操作を行うことでパフォーマンスを向上させます。
### コンポーネントベースのアーキテクチャ:
Reactは、UIを独立した小さな部品であるコンポーネントに分割するアーキテクチャを採用しています。このコンポーネントベースのアーキテクチャにより、UIを再利用可能な部品に分割し、保守性や拡張性を向上させることができます。
### JSX (JavaScript XML):
Reactでは、JSXと呼ばれるJavaScriptの拡張構文を使用してUIを記述します。JSXは、HTMLのような記法でコンポーネントを記述することができ、UIの構造とロジックを1つのファイルにまとめることができます。
### 単方向データフロー:
Reactでは、データの流れが一方向であるというコンセプトを重視しています。親コンポーネントから子コンポーネントへのデータの伝播が一方向であるため、データフローが予測可能で、デバッグやテストが容易になります。
### 豊富なコミュニティとエコシステム:
Reactは非常に人気のあるライブラリであり、広範なコミュニティとエコシステムが存在します。これにより、多くのサードパーティライブラリやツールが利用可能で、Reactアプリケーションの開発をサポートしています。

Reactのこれらの特徴により、モダンなWebアプリケーションの開発が容易になり、パフォーマンスやメンテナンス性の向上が期待できます。


---
