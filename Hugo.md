###
# Hugo
###

---
```
mkdir myblog
cd myblog
hugo server -D

静生成
cd myblog
hugo
http://localhost:1313/

静確認
cd public
python -m http.server
http://0.0.0.0:8000/
```
---

はい、Hugoを使って生成された `public` ディレクトリの内容をGitHub Pagesで公開することは可能です。以下はその手順です：

1. **Hugoサイトをビルド**:
    ```sh
    hugo
    ```
    これにより、 `public` ディレクトリに静的ファイルが生成されます。

2. **GitHubリポジトリを作成**:
    - GitHubで新しいリポジトリを作成します。
    - リポジトリ名は、ユーザー名に合わせるか、特定のプロジェクト名にします。

3. **publicディレクトリをGitリポジトリに変換**:
    `public` ディレクトリ内に移動して、Gitリポジトリとして初期化します。
    ```sh
    cd public
    git init
    ```

4. **GitHubリポジトリをリモートに追加**:
    ```sh
    git remote add origin https://github.com/USERNAME/REPOSITORY.git
    ```

5. **ファイルをコミットしてプッシュ**:
    ```sh
    git add .
    git commit -m "Initial commit"
    git push -u origin main
    ```

6. **GitHub Pagesの設定**:
    - GitHubのリポジトリページに移動し、設定(Settings)に進みます。
    - 「Pages」セクションで、ソース(Source)を `main` ブランチ（または適切なブランチ）に設定します。

これで、しばらく待つと、指定されたURL（通常は `https://username.github.io/repository`）でサイトが公開されます。

もし、ルートディレクトリに対してではなく、サブディレクトリとして公開する場合は、Hugoの `config.toml` ファイルの `baseURL` を適切に設定することを忘れないでください。例えば：

```toml
baseURL = "https://username.github.io/repository/"
```

この方法で、 `public` ディレクトリの内容をGitHub Pagesで公開することができます。

---

Hugoの `public` フォルダに生成された静的ファイルが正しく生成されているかどうかを確認するために、ローカルで簡単に確認する方法があります。以下の手順を試してみてください：

1. **Hugoサイトのビルド**:
    ```sh
    hugo
    ```
    これにより、最新の静的ファイルが `public` フォルダに生成されます。

2. **ローカルサーバーで公開**:
    `public` フォルダの内容をローカルサーバーで確認するために、簡単なHTTPサーバーを起動します。以下のコマンドを使用します：

    **Python 3.xを使用する場合**:
    ```sh
    cd public
    python -m http.server
    ```
    これにより、ローカルホストのポート8000でサーバーが起動します。

    ブラウザで `http://localhost:8000` にアクセスして、生成された静的サイトが正しく表示されるかを確認します。

3. **問題がある場合の確認点**:
    - `config.toml` ファイルの `baseURL` が正しく設定されていることを確認します。GitHub Pagesで公開する場合、`baseURL` はリポジトリのURLに設定する必要があります。
    - テーマや設定が正しく適用されているか確認します。テーマの設定やカスタマイズに誤りがないか見直します。
    - カスタムドメインを使用している場合、ドメインの設定が正しく行われているか確認します。

4. **リポジトリのクリーンアップと再プッシュ**:
    必要に応じて、`public` フォルダをクリーンアップし、再度ビルドとプッシュを行います。

    ```sh
    rm -rf public
    hugo
    cd public
    git add .
    git commit -m "Rebuild site"
    git push origin main
    ```

これで、ローカルでの確認とGitHub Pagesでの公開の両方を正しく行えるようになるはずです。問題が解決しない場合、Hugoの設定ファイルやテーマのドキュメントを再度確認することをお勧めします。

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
