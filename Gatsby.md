###
# Gatsby
###

---

Gatsbyは、Reactベースのフレームワークで、静的サイトジェネレーターとして非常に強力です。以下に、Gatsbyをインストールして新しいプロジェクトを作成する手順を示します。

### 前提条件

- Node.jsがインストールされていることを確認してください。
- npm (Node Package Manager) またはyarnがインストールされていることを確認してください。

### 1. Gatsby CLIのインストール

まず、Gatsby CLIをグローバルにインストールします。これにより、新しいGatsbyプロジェクトを簡単に作成できるようになります。

```bash
npm install -g gatsby-cli
```

### 2. 新しいGatsbyプロジェクトの作成

次に、Gatsby CLIを使用して新しいプロジェクトを作成します。以下のコマンドを実行してプロジェクトディレクトリを作成します。

```bash
gatsby new my-gatsby-site
cd my-gatsby-site
```

`my-gatsby-site` はプロジェクトの名前です。任意の名前に変更できます。

### 3. 開発サーバーの起動

Gatsbyの開発サーバーを起動し、サイトをローカルでプレビューします。

```bash
gatsby develop
```

開発サーバーが起動すると、ブラウザで `http://localhost:8000` にアクセスすることで、Gatsbyサイトの初期セットアップが正しく行われているか確認できます。

### 4. プロジェクトの構成

新しく作成されたGatsbyプロジェクトのディレクトリ構成は以下のようになっています：

```
my-gatsby-site/
├── node_modules/
├── src/
│   ├── images/
│   ├── pages/
│   │   └── index.js
├── .gitignore
├── gatsby-config.js
├── package.json
└── README.md
```

- `src/`: ソースコードが格納されるディレクトリ。
- `src/pages/`: 各ページのコンポーネントを格納するディレクトリ。
- `gatsby-config.js`: Gatsbyの設定ファイル。

### 5. 新しいページの作成

新しいページを作成するには、`src/pages/` ディレクトリに新しいJavaScriptファイルを追加します。例えば、`src/pages/about.js` を作成し、以下のように記述します。

```javascript
import React from "react"

const AboutPage = () => (
  <main>
    <h1>About Us</h1>
    <p>Welcome to the about page of our Gatsby site.</p>
  </main>
)

export default AboutPage
```

これにより、`http://localhost:8000/about` でアクセスできる新しいページが作成されます。

### 6. プラグインの追加

Gatsbyはプラグインによって機能を拡張できます。例えば、ファイルシステムからデータを読み込むためのプラグインを追加するには、以下のコマンドを実行します。

```bash
npm install gatsby-source-filesystem
```

次に、`gatsby-config.js` ファイルにプラグインの設定を追加します。

```javascript
module.exports = {
  siteMetadata: {
    title: `My Gatsby Site`,
    description: `A simple description about pandas eating lots...`,
    author: `@gatsbyjs`,
  },
  plugins: [
    {
      resolve: `gatsby-source-filesystem`,
      options: {
        name: `src`,
        path: `${__dirname}/src/`,
      },
    },
  ],
}
```

### 7. サイトのビルドとデプロイ

サイトをビルドして静的ファイルを生成するには、以下のコマンドを実行します。

```bash
gatsby build
```

これにより、`public` ディレクトリに静的ファイルが生成されます。

### まとめ

以上で、Gatsbyの基本的なインストールと設定が完了しました。Gatsbyは非常に強力で柔軟な静的サイトジェネレーターであり、多くのプラグインやテーマを利用して、自分のサイトをカスタマイズできます。公式ドキュメントやチュートリアルを参考にしながら、さらにサイトを発展させてください。

---
