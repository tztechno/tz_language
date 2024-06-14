
###
# Hexo
###


---

Hexoは高速で簡単に使える静的サイトジェネレーターで、特にブログサイトの作成に適しています。以下に、Hexoをインストールして新しいブログサイトを作成する手順を示します。

### 前提条件

- Node.jsがインストールされていることを確認してください。
- npm (Node Package Manager) がインストールされていることを確認してください。

### 1. Hexoのインストール

まず、Hexoをグローバルにインストールします。ターミナルやコマンドプロンプトを開いて、以下のコマンドを実行してください。

```bash
npm install -g hexo-cli
```

### 2. 新しいHexoプロジェクトの作成

次に、新しいHexoプロジェクトを作成します。以下のコマンドを実行してプロジェクトディレクトリを作成します。

```bash
hexo init my-blog
cd my-blog
npm install
```

`my-blog` はプロジェクトの名前です。任意の名前に変更できます。

### 3. 開発サーバーの起動

Hexoの開発サーバーを起動し、ブログをローカルでプレビューします。

```bash
hexo server
```

ターミナルに `INFO  Hexo is running at http://localhost:4000` と表示されたら、ブラウザで `http://localhost:4000` にアクセスして、ブログの初期セットアップが正しく行われているか確認できます。

### 4. 記事の作成

ブログの記事を作成するには、以下のコマンドを実行します。

```bash
hexo new post "My First Post"
```

これにより、`source/_posts/` ディレクトリに `my-first-post.md` というMarkdownファイルが作成されます。ファイルを開いて、記事の内容を編集します。

### 5. サイトのビルド

サイトをビルドして静的ファイルを生成するには、以下のコマンドを実行します。

```bash
hexo generate
```

これにより、`public` ディレクトリに静的ファイルが生成されます。

### 6. デプロイ

Hexoにはデプロイ機能が組み込まれており、GitHub Pagesや他のホスティングサービスに簡単にデプロイできます。デプロイの設定を行うには、`_config.yml` ファイルを編集します。以下はGitHub Pagesにデプロイする例です。

```yaml
deploy:
  type: git
  repo: https://github.com/username/username.github.io.git
  branch: main
```

設定を保存したら、以下のコマンドでデプロイします。

```bash
npm install hexo-deployer-git --save
hexo deploy
```

これで、Hexoのインストールから新しいブログサイトの作成、そしてデプロイまでの基本的な流れが完了です。Hexoには多くのテーマやプラグインが用意されているので、必要に応じてカスタマイズし、自分だけのブログを作り上げてください。

---
