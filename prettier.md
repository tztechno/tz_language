

https://www.youtube.com/watch?v=zoaIv5ifoPI

---

Prettierのインストール:
最初に、Prettierをプロジェクトにインストールします。npmを使ってインストールする場合は、次のコマンドを実行します。
```
npm install --save-dev --save-exact prettier
```
または、yarnを使用してインストールする場合は、次のようにします。
```
yarn add --dev --exact prettier
```
設定:
Prettierには、デフォルトの設定がありますが、プロジェクトに合わせてカスタマイズすることもできます。
プロジェクトのルートディレクトリに.prettierrcやprettier.config.jsなどの設定ファイルを作成し、設定を定義します。
例えば、.prettierrcファイルには以下のような設定を記述できます。
```
{
  "semi": false,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "all",
  "printWidth": 80
}
```
この設定は、セミコロンの有無、シングルクォートの使用、タブの幅、行の長さなどを指定します。
実行:
Prettierを実行してコードを整形します。コマンドラインでファイルやディレクトリを指定してPrettierを実行することができます。
```
npx prettier --write "src/**/*.js"
```
上記のコマンドでは、srcディレクトリ以下のすべてのJavaScriptファイルが整形されます。
--writeオプションを使用することで、ファイルが直接書き換えられます。
また、--checkオプションを使用すると、フォーマットされていないファイルがあるかどうかを確認できます。

---
---
```

Prettierは、コードフォーマッターの1つです。
コードフォーマッターは、プログラミング言語のコードを自動的に整形して、一貫性のあるスタイルで表示するツールです。
PrettierはJavaScriptやTypeScript、HTML、CSSなど、さまざまな言語に対応しています。
コードのレイアウトやインデント、スペースの数など、様々なスタイルを設定でき、プロジェクト全体で一貫性のあるコードスタイルを保つのに役立ちます。
```
---
