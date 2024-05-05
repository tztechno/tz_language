# prettier


https://www.youtube.com/watch?v=zoaIv5ifoPI

---


PrettierをVS Codeで自動フォーマットとして使うためには、いくつかの手順を確認する必要があります。

まず、以下のステップを試してみてください：

### VS CodeにPrettier拡張機能をインストール：
VS Codeの拡張機能マーケットプレイスからPrettierを検索してインストールします。

### VS Codeの設定でPrettierを有効にする：
VS Codeの設定で、Prettierを有効にするために以下のような設定を追加します。

```
"editor.defaultFormatter": "esbenp.prettier-vscode",
"[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[javascriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
"[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
},
```

### Prettierの設定：
プロジェクトルートに.prettierrcやprettier.config.jsなどのPrettierの設定ファイルを作成して、好みのフォーマット設定を行います。

---

Prettier は独自のコードフォーマッタです。 
コードを解析し、行の最大長を考慮した独自のルールで再出力し、必要に応じてコードを折り返すことで、一貫したスタイルを強制します。

---

