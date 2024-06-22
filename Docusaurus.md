###
# Docusaurus
###

---

Docusaurusは、静的なウェブサイトやドキュメンテーションサイトを作成するためのツールで、Reactで構築されています。Docusaurusのインストール方法を以下に示します。

### Docusaurusのインストール手順

1. **Node.jsとnpmのインストール**

   最初に、Node.jsとnpm（Node Package Manager）がインストールされていることを確認してください。これらはDocusaurusの実行に必要です。

   - Node.jsの公式ウェブサイトから最新バージョンをダウンロードしてインストールします。[Node.js 公式ウェブサイト](https://nodejs.org/)
   - npmはNode.jsをインストールすると一緒に付属しています。

2. **Docusaurusのインストール**

   ターミナル（コマンドプロンプト）を開いて、次のコマンドを実行してください。

   ```bash
   npm install -g docusaurus-init
   ```

   これにより、グローバルにDocusaurusの初期化コマンドがインストールされます。

3. **新しいプロジェクトの作成**

   Docusaurusを使用して新しいプロジェクトを作成するには、適当な場所で以下のコマンドを実行します。

   ```bash
   docusaurus-init
   ```

   このコマンドを実行すると、プロンプトが表示されますので、プロジェクトの設定を行います（プロジェクト名、テンプレートなどを選択できます）。

4. **プロジェクトのセットアップ**

   プロジェクトが作成されたら、そのディレクトリに移動して依存関係をインストールします。

   ```bash
   cd <プロジェクト名>
   npm install
   ```

5. **ローカルサーバーの起動**

   依存関係がインストールされたら、次のコマンドでDocusaurusのローカルサーバーを起動します。

   ```bash
   npm start
   ```

   デフォルトでは、サーバーは`http://localhost:3000`で実行されます。ブラウザでこのURLを開くと、Docusaurusの初期画面が表示されるはずです。

6. **ドキュメントの追加と編集**

   Docusaurusのセットアップが完了したら、`docs`ディレクトリ内にMarkdown形式でドキュメントを追加し、必要に応じて`sidebars.js`を編集してナビゲーションを設定します。

### その他の情報

- Docusaurusの詳細な設定やカスタマイズについては、公式ドキュメントを参照してください。[Docusaurus 公式ドキュメント](https://docusaurus.io/docs/)
- デプロイに関する情報やビルドのカスタマイズについても、ドキュメントに記載されています。

これで、基本的なDocusaurusのインストールとプロジェクトのセットアップが完了しました。

---

Docusaurusは、Reactを使用して構築された静的サイトジェネレーターで、特にドキュメントサイトを作成するのに便利です。Docusaurusをインストールして、新しいプロジェクトを作成する手順は以下の通りです。

### 前提条件

- Node.js (バージョン16.14以上)がインストールされていることを確認してください。
- npmまたはyarnがインストールされていることを確認してください。

### 1. Docusaurusプロジェクトの作成

まず、Docusaurusをインストールし、新しいプロジェクトを作成します。Docusaurusはnpmとyarnの両方でインストールできますが、ここではnpxを使用したインストール方法を紹介します。

#### npmを使用する場合:

```bash
npx create-docusaurus@latest my-website classic
cd my-website
```

#### yarnを使用する場合:

```bash
yarn create docusaurus my-website classic
cd my-website
```

`my-website` の部分は、あなたのプロジェクト名に置き換えてください。`classic` はDocusaurusの公式テンプレートの名前です。

### 2. 開発サーバーの起動

プロジェクトのディレクトリに移動し、開発サーバーを起動します。

#### npmを使用する場合:

```bash
npm run start
```

#### yarnを使用する場合:

```bash
yarn start
```

開発サーバーが起動すると、ブラウザで `http://localhost:3000` にアクセスすることで、Docusaurusの初期サイトを確認できます。

### 3. サイトの構造

Docusaurusプロジェクトのディレクトリ構造は以下のようになっています：

```
my-website/
  ├── blog/
  ├── docs/
  ├── src/
  ├── static/
  ├── docusaurus.config.js
  ├── sidebars.js
  └── package.json
```

- `blog/`: ブログ記事を格納するディレクトリ。
- `docs/`: ドキュメントを格納するディレクトリ。
- `src/`: カスタムReactコンポーネントやページを格納するディレクトリ。
- `static/`: 静的ファイルを格納するディレクトリ（例：画像、ファビコンなど）。
- `docusaurus.config.js`: サイト全体の設定ファイル。
- `sidebars.js`: ドキュメントのサイドバー構成ファイル。
- `package.json`: プロジェクトの依存関係とスクリプトを管理するファイル。

### 4. ドキュメントの追加

ドキュメントを追加するには、`docs/` ディレクトリにMarkdownファイルを作成します。例えば、`docs/intro.md` を作成し、以下のように記述します。

```markdown
---
id: intro
title: Introduction
---

# Welcome to Docusaurus

This is the introduction to your documentation!
```

### 5. サイドバーの更新

ドキュメントのサイドバーを更新するには、`sidebars.js` ファイルを編集します。

```javascript
module.exports = {
  docs: [
    {
      type: 'category',
      label: 'Introduction',
      items: ['intro'],
    },
    // 他のセクションを追加
  ],
};
```

### 6. ビルドとデプロイ

サイトをビルドしてデプロイする準備ができたら、以下のコマンドを実行します。

#### ビルド:

```bash
npm run build
```

#### デプロイ:

DocusaurusはGitHub Pagesへのデプロイをサポートしています。デプロイ用のスクリプトを実行する前に、`docusaurus.config.js` ファイルで `url` と `baseUrl` を正しく設定してください。

```bash
npm run deploy
```

これで、Docusaurusのインストールと基本的なセットアップは完了です。これを基に、自分のニーズに合わせてドキュメントサイトをカスタマイズしていきましょう。

---
