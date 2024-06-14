###
# Hugo
###

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
