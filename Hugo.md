###
# Hugo
###


---
```
mdで記事を追加してから、ビルドし直す必要
TOPページは記事が数行テキストで表示される
各記事へ飛ぶと、markdownが有効に表示される
手動でアップロードできるか、gitを使わないといけないかは不明
deployまでは確認しておきたい
```
---

Hugoを使用して新しいブログを立ち上げる手順は以下の通りです。これには、新しいHugoサイトの作成、テーマの追加、およびサイトの構築が含まれます。

### ステップ 1: 新しいHugoサイトを作成
ターミナルを開き、以下のコマンドを実行して新しいHugoサイトを作成します。ここでは、新しいサイトの名前を `myblog` としています。

```sh
hugo new site myblog
```

### ステップ 2: テーマの追加
Hugoには多くのテーマが用意されており、[Hugo Themes](https://themes.gohugo.io/) から選ぶことができます。ここでは例として、`ananke` テーマを使用します。

まず、テーマディレクトリに移動します。

```sh
cd myblog/themes
```

次に、`ananke` テーマをGitHubからクローンします。

```sh
git clone https://github.com/theNewDynamic/gohugo-theme-ananke.git
```

### ステップ 3: テーマを設定ファイルに追加
`config.toml` ファイルを開いて、テーマを設定します。

```sh
echo 'theme = "gohugo-theme-ananke"' >> ../config.toml
```

### ステップ 4: 初めてのコンテンツを作成
新しいブログ投稿を作成します。

```sh
cd ../
hugo new posts/my-first-post.md
```

生成された `my-first-post.md` ファイルを編集して、内容を追加します。エディタを使用して以下の内容を追加できます。

```markdown
---
title: "My First Post"
date: 2024-06-14T12:00:00+09:00
draft: false
---

This is my first post using Hugo!
```

### ステップ 5: ローカルサーバーを起動して確認
以下のコマンドを実行して、ローカルサーバーを起動し、ブログを確認します。

```sh
hugo server -D
```

ブラウザで `http://localhost:1313/` にアクセスすると、ブログのトップページが表示されるはずです。

### ステップ 6: ブログをビルド
サイトをビルドして静的ファイルを生成します。

```sh
hugo
```

このコマンドにより、 `public` ディレクトリに静的ファイルが生成されます。このファイルをウェブサーバーにアップロードすることで、ブログを公開できます。

以上がHugoを使用して新しいブログを立ち上げる基本的な手順です。質問や追加の設定が必要な場合は、お知らせください。

---

Hugoを使ってブログを作る準備をするためには、以下のステップに従うと良いでしょう。

### 1. Hugoのインストール

まずはじめに、Hugoをインストールします。Hugoは、オープンソースの静的サイトジェネレータで、インストールが比較的簡単です。

- **Windows**:
  Hugoの公式サイト（https://gohugo.io/getting-started/installing/#windows）から、Windows用のインストーラをダウンロードしてインストールします。

- **Mac**:
  Homebrewを使って簡単にインストールできます。
  ```
  brew install hugo
  ```

- **Linux**:
  ディストリビューションによって方法が異なりますが、一般的にはパッケージマネージャーを使ってインストールできます。例えば、UbuntuやDebianでは次のコマンドでインストールできます。
  ```
  sudo apt-get install hugo
  ```

インストールが完了したら、以下のコマンドでバージョンを確認してみてください。
```
hugo version
```
バージョンが表示されれば、インストールは成功しています。

### 2. 新しいHugoプロジェクトの作成

次に、Hugoで新しいプロジェクトを作成します。

```
hugo new site myblog
cd myblog
```

`myblog` の部分は任意のプロジェクト名に置き換えてください。

### 3. テーマの選択と設定

Hugoには多くのテーマが用意されています。好みのテーマを選び、プロジェクトに設定します。例えば、テーマを `hugo-theme-cactus-plus` として設定する場合は、以下のようにします。

```
git init
git submodule add https://github.com/nodejh/hugo-theme-cactus-plus.git themes/hugo-theme-cactus-plus
echo 'theme = "hugo-theme-cactus-plus"' >> config.toml
```

### 4. コンテンツの作成

ブログの記事を作成するには、以下のようにコマンドを実行します。

```
hugo new posts/my-first-post.md
```

これにより、`content/posts/my-first-post.md` というマークダウン形式の新しい記事が作成されます。

### 5. ローカルサーバーで確認

ブログのプレビューをローカルで確認するには、次のコマンドを実行します。

```
hugo server -D
```

これにより、ブログがビルドされてローカルのWebサーバーで実行され、`http://localhost:1313` でアクセスできるようになります。

### 6. デプロイ

最後に、ブログを実際のウェブサーバーにデプロイする方法を選択し、設定します。Hugoで生成されるファイルは静的なHTMLなので、どんなウェブホスティングサービスでも簡単にデプロイできます。

以上で、基本的なHugoの使い方とブログの作成手順が完了します。必要に応じて、テーマのカスタマイズや詳細な設定を行いながら、自分だけのブログを完成させてください。

---
