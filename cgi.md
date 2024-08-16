

---

CGI (Common Gateway Interface) は、Webサーバーが外部のプログラムを呼び出して動的にコンテンツを生成するためのインターフェースです。CGIスクリプトを作成することで、HTMLページに動的な機能を追加することができます。

以下は、CGIスクリプトの基本的な作成方法を紹介します。

### 1. スクリプトを書く
CGIスクリプトは、通常、Perl、Python、Ruby、Shellスクリプトなどで書かれます。ここでは、Pythonでの基本的なCGIスクリプトの例を示します。

#### Pythonの例:
```python
#!/usr/bin/env python3

import cgi
import cgitb

# エラーを表示するための設定
cgitb.enable()

# Content-typeヘッダーの出力
print("Content-Type: text/html\n")

# フォームデータを取得
form = cgi.FieldStorage()

# フォームにフィールドが含まれているかチェック
if "name" not in form or not form["name"].value:
    print("<h1>名前を入力してください。</h1>")
else:
    print(f"<h1>こんにちは、{form['name'].value}さん！</h1>")
```

### 2. ファイルの配置
1. 上記のスクリプトを `hello.py` という名前で保存します。
2. スクリプトをサーバーのCGIディレクトリ（通常は `/cgi-bin/`）に配置します。

### 3. パーミッションの設定
スクリプトに実行権限を付与します。コマンドラインで次のようにします:

```bash
chmod +x /path/to/cgi-bin/hello.py
```

### 4. Webサーバーの設定
CGIを有効にするためには、Webサーバー（例えばApacheやNginx）の設定を変更する必要があります。

#### Apacheの例:
`httpd.conf` または `apache2.conf` ファイルに以下の設定を追加します。

```apache
<Directory "/path/to/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .py
</Directory>
```

### 5. CGIスクリプトの実行
Webブラウザで次のようにURLにアクセスします。

```
http://yourdomain.com/cgi-bin/hello.py
```

これで、フォームに名前を入力して送信すると、Pythonスクリプトが実行され、動的に生成されたHTMLが表示されます。

### 追加情報
- **セキュリティ**: CGIスクリプトは、直接サーバー上で実行されるため、セキュリティに注意が必要です。外部からの入力を信頼せず、適切な入力バリデーションを行いましょう。
- **パフォーマンス**: CGIは各リクエストごとに新しいプロセスを生成するため、パフォーマンスの面では不利です。モダンなWebアプリケーションでは、FastCGIやWSGIなど、より効率的なインターフェースが使用されることが多いです。

CGIの基礎は以上です。どの言語で実装するか、またどのWebサーバーを使用するかによって手順は若干異なりますが、基本的な流れは同じです。

---
