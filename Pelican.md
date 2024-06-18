###
# Pelican
###


---

GitHub Pagesへのデプロイに関して、`python -m http.server`は必要ありません。これはローカル環境でサイトの動作を確認するためのコマンドです。したがって、GitHub Pagesにサイトを公開する手順には含まれません。

以下に、GitHub Pagesへのデプロイ手順をまとめます。

### 1. GitHub リポジトリを作成

GitHub上で新しいリポジトリを作成します。このリポジトリは後で`output`ディレクトリの内容をホストするためのものです。

### 2. Pelicanサイトをビルド

Pelicanの設定ファイル（`pelicanconf.py`）を確認し、`SITEURL`をGitHub PagesのURLに設定します。

```python
# pelicanconf.py
SITEURL = 'https://<your-username>.github.io/<your-repo>'
RELATIVE_URLS = False
```

`<your-username>`と`<your-repo>`をあなたのGitHubユーザー名とリポジトリ名に置き換えます。

その後、Pelicanでサイトをビルドします。

```bash
pelican content
```

### 3. `output` ディレクトリをGitリポジトリに初期化

`output`ディレクトリに移動し、Gitリポジトリを初期化します。

```bash
cd output
git init
```

### 4. リモートリポジトリを追加

リモートリポジトリを追加します。

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git
```

### 5. コミットとプッシュ

`output`ディレクトリの内容をコミットしてGitHubにプッシュします。

```bash
git add .
git commit -m "Initial commit"
git push -u origin master
```

### 6. GitHub Pagesの設定確認

GitHubリポジトリの設定ページに移動し、「Pages」セクションで`master`ブランチが選択されていることを確認します。

これで、GitHub Pagesに公開されているはずです。

### 7. オプション: ローカルでの確認

公開前にローカル環境でサイトを確認したい場合は、`python -m http.server`を使用してローカルサーバーを起動し、ブラウザで確認することができます。

```bash
cd output
python -m http.server
```

ただし、これはローカル確認用の手順であり、GitHub Pagesへのデプロイには直接関係しません。

### まとめ

- `python -m http.server`はローカル確認用であり、GitHub Pagesへのデプロイには不要です。
- Pelicanでサイトをビルドし、`output`ディレクトリをGitHubにプッシュするだけでGitHub Pagesに公開できます。

この手順に従ってデプロイを試してみてください。それでも表示に問題がある場合は、具体的なエラーメッセージや現象を教えていただければ、さらに詳細なサポートを提供できます。

---

Pelicanで生成した `output` ディレクトリの内容をGitHubリポジトリの `master` ブランチにプッシュする方法は、以下の手順になります。

1. **GitHub リポジトリを作成する**
   - GitHub 上で新しいリポジトリを作成します。このリポジトリは後で `output` ディレクトリの内容をホストするためのものです。

2. **ローカルでの作業準備**
   - ローカル環境で `output` ディレクトリにPelicanで生成したファイルが含まれていることを確認します。

3. **Git の初期化とリモートリポジトリの設定**
   - `output` ディレクトリ内で以下のコマンドを実行して、Git の初期化とリモートリポジトリの設定を行います。

   ```bash
   cd /path/to/output
   git init
   git remote add origin <GitHubリポジトリのURL>
   ```

   - `<GitHubリポジトリのURL>` には、作成したGitHubリポジトリのURLを指定します。

4. **コミットとプッシュ**
   - 以下のコマンドを使って、ファイルをコミットし、GitHubの`master`ブランチにプッシュします。

   ```bash
   git add .
   git commit -m "Initial commit"
   git push -u origin master
   ```

   - `git add .` は、全てのファイルをステージングエリアに追加します。
   - `git commit -m "Initial commit"` は、ステージングエリアの内容をコミットします。コミットメッセージは任意ですが、ここでは "Initial commit" としています。
   - `git push -u origin master` は、ローカルの `master` ブランチの内容をリモートの `master` ブランチにプッシュします。

これにより、Pelicanで生成した `output` ディレクトリの内容がGitHubの `master` ブランチにプッシュされ、ホスティングされるようになります。

---

Pelicanは、Pythonで書かれた静的サイトジェネレーターです。以下の手順に従ってPelicanをインストールし、新しいブログサイトを作成する方法を紹介します。

### 前提条件

- Pythonがインストールされていることを確認してください。
- pip (Python Package Installer) がインストールされていることを確認してください。

### 1. 仮想環境の設定

まず、新しいプロジェクトディレクトリを作成し、仮想環境を設定します。

```bash
mkdir my-pelican-site
cd my-pelican-site
python -m venv venv
source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
```

### 2. PelicanとMarkdownのインストール

次に、PelicanとMarkdownのパッケージをインストールします。

```bash
pip install pelican markdown
```

### 3. 新しいPelicanプロジェクトの作成

Pelicanプロジェクトを初期化します。

```bash
pelican-quickstart
```

このコマンドを実行すると、いくつかの質問が表示されます。以下は、一般的な回答例です。

1. Where do you want to create your new web site? (in the current directory, just hit Enter)
2. What will be the title of this web site? (My Pelican Site)
3. Who will be the author of this web site? (Your Name)
4. What will be the default language of this web site? (en)
5. Do you want to specify a URL prefix? (e.g., https://example.com) (hit Enter for no)
6. Do you want to enable article pagination? (Y/n) (hit Enter for default)
7. How many articles per page do you want? (default is 10) (hit Enter for default)
8. What is your time zone? (e.g., Europe/Paris) (You can specify your timezone, e.g., America/New_York)
9. Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n) (Y)
10. Do you want to upload your website using FTP? (y/N) (N)
11. Do you want to upload your website using SSH? (y/N) (N)
12. Do you want to upload your website using Dropbox? (y/N) (N)
13. Do you want to upload your website using S3? (y/N) (N)
14. Do you want to upload your website using Rackspace Cloud Files? (y/N) (N)

これにより、プロジェクトの基本構成が作成されます。

### 4. コンテンツの作成

ブログの記事を作成するには、`content` ディレクトリ内にMarkdownファイルを追加します。例えば、`content/my-first-post.md` を作成します。

```markdown
Title: My First Post
Date: 2023-06-14
Category: Blog
Tags: pelican, static site generator
Slug: my-first-post
Authors: Your Name
Summary: This is my first post using Pelican.

This is the content of my first post.
```

### 5. サイトのビルド

サイトを生成するには、以下のコマンドを実行します。

```bash
pelican content
```

これにより、`output` ディレクトリに静的ファイルが生成されます。

### 6. サイトのプレビュー

生成されたサイトをローカルでプレビューするには、簡易HTTPサーバーを使用します。Pythonには簡易HTTPサーバーが組み込まれています。

```bash
cd output
python -m http.server
```

これで、ブラウザで `http://localhost:8000` にアクセスして、サイトを確認できます。

### 7. デプロイ

サイトをホスティングサービスにデプロイする方法は多岐にわたりますが、GitHub PagesやNetlifyを使用すると簡単です。GitHub Pagesを使用する場合、生成された `output` ディレクトリの内容をGitHubリポジトリの `gh-pages` ブランチにプッシュするだけです。

### まとめ

これで、Pelicanの基本的なインストールと設定が完了しました。Pelicanは柔軟で拡張性の高い静的サイトジェネレーターであり、プラグインやテーマを利用して、自分のニーズに合わせてカスタマイズすることができます。公式ドキュメントやコミュニティリソースを参考にしながら、さらにサイトを発展させてください。

---
